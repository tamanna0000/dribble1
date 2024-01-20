def read_keywords(keyword_file_name):#this functions reads the keyword file and makes a dictionary of the word and its value.
    values = {}
    try:
        if isinstance(keyword_file_name, dict):  # If input is a dictionary
            for key, value in keyword_file_name.items():
                values[key] = int(value)
        elif isinstance(keyword_file_name, str):  # If input is a file name
            with open(keyword_file_name, "r") as openfile:
                for line in openfile.readlines():
                    if line.strip() != "":
                        word = line.strip().split("\t")#strips and slipts the word from the value
                        values[word[0]] = int(word[1])#adds the word and value to the dictionary
        else:
            print("Invalid input type. Expected dictionary or string.")
            return values
        
        return values
    except IOError:
        print(f"Could not open file [{keyword_file_name}]")#if the file couldnt be opened throws exception and returns empty dictionary.
        return values

        


def clean_tweet_text(tweet_text):#this function takes in the tweet and removes any special character
    bad_chars = ['!', '@', '#', '%', '^', '&', '*', '+', '=', '/', '?', '.', ';','"','$','()','_','-',"'",'{','}','~',':','0','1','2','3','4','5','6','7','8','9']
    tweet_text = tweet_text.lower()


    for char in bad_chars:
        if char in tweet_text:
            tweet_text = tweet_text.replace(char, '')  # Update the word without the bad character

    return tweet_text


def calc_sentiment(tweet_text, keyword_dict):#calculates the sentiment value based off of the clean keyword file. 
    clean_keywords= read_keywords(keyword_dict)#cleans keyword file
    sentiment=0
    words = tweet_text.split(" ")#splits the sentence into words
    for word in words:
        if word in clean_keywords:
            sentiment+= clean_keywords[word]#if word is in clean keywords it adds to the sentiment
    return sentiment



def classify(score):#checks if the sentiment score is positive, negative or neutral
    if score>0:
        sentiment_score=('positive')
    elif score<0:
        sentiment_score=('negative')
    else:
        sentiment_score=('neutral') 
    return sentiment_score                   
    

   
def read_tweets(tweet_file_name):#reads the tweet file andmakes every tweet into a dictionary and returns a list of dictionary
    openfile = None#instantiates open file
    try:
        openfile=open(tweet_file_name,'r')
        lists=[]
        for line in openfile.readlines():
            if line != "":#checks if there is a line to read
                line = line.strip()#strips it
                line = line.split(",")#splits the tweet
                tweet = clean_tweet_text(line[1])#cleans the tweet
                dict={}
                #adds all the relevant information in the dictionary
                dict['city']=line[8]
                dict['country']=line[6]
                dict['date']=line[0]
                fav = int(line[4])
                dict['favorite']=fav
                dict['lang']=line[5]
                if line[9] != ('NULL'):
                    latt=float(line[9])
                    dict['lat']=latt
                else:
                    dict['lat']='NULL'

                if line[10] != "NULL":
                    longt=float(line[10])
                    dict['lon']=longt
                else:   
                    dict["lon"]="NULL" 

                if line[3]!="NULL":
                    retweet=int(line[3])
                    dict['retweet']=retweet
                else:
                    dict["retweet"]="NULL"
                dict['state']=line[7]
                dict['text']=tweet
                dict['user']=line[2]
                lists.append(dict)#adds the dictionary to the list
        return lists#returns the list
    except IOError:
        print("Could not open file[%s]"% tweet_file_name) 
        return [] 
    finally:
        if openfile:  # Check if openfile is initialized before trying to close it
            openfile.close()     



def make_report(tweet_list, keyword_dict):#makes a report based off the tweet list
    #initialising all the variables
    num_favorite=0
    num_negative=0
    num_positive=0
    num_neutral=0
    num_retweet=0
    num_tweets=0
    fav_sentiment=0
    retweet_sentiment=0
    total_sentiment=0
    #initialising dictionary
    countries={}
    count={}
    senti_country={}
    report={}


    for tweet in tweet_list:
        sentiment = calc_sentiment(tweet["text"],keyword_dict)#stores sentiment value for the specific tweet 
        num_tweets+=1
        if tweet["favorite"]>0:#checks if favorite is greater than 0
            num_favorite+=1
            fav_sentiment+=sentiment
        if tweet["retweet"]>0:#checks if retweet is greater than 0
            num_retweet+=1
            retweet_sentiment+=sentiment   
        
        total_sentiment+=sentiment
        classified_value=classify(sentiment)#classifies the sentiment values 
        if classified_value==("negative"):
            num_negative+=1
        elif classified_value=="positive":
            num_positive+=1
        else:
            num_neutral+=1
        if tweet["country"]!="NULL":#checks if the country is null 
            if tweet["country"] not in countries:
                countries[tweet["country"]]=sentiment
                count[tweet["country"]]=1

            else:#or else adds to the the current country
                countries[tweet["country"]]+=sentiment
                count[tweet["country"]]+=1

    for country in countries:
        if country not in senti_country:
            senti_country[country] = (countries[country])/(count[country])#calculates the sentiment average for each the country

            

    if num_favorite>0:#checks if the num fav is greater than 0
        avg_favorite=fav_sentiment/num_favorite
    else:
        avg_favorite="NAN"
    if num_retweet>0:#checks if the num retweet is greater than 0
        avg_retweet= retweet_sentiment/num_retweet
    else:
        avg_retweet="NAN"
    if num_tweets>0:#checks if the num tweet is greater than 0
        avg_sentiment=total_sentiment/num_tweets
    else:
        avg_sentiment="NAN"  

    sorted=sort_dict(senti_country,by_key=False,asc=False) #sorts the top five countries by avg sentiment 

    top_five = []
    top_five_copy=[]
    top_five_string = ""
    for countries in sorted:
        top_five.append(countries)
    if len(top_five) > 5:#if the list of countries is greater than 5 it takes the first 5 countries 
        for i in range(5):
            top_five_copy.append(top_five[i])
        top_five_string = ', '.join(top_five_copy)
    else:#else takes whats there
        top_five_string = ', '.join(top_five)
    #adds all the calculated values to a dictionary
    report["avg_favorite"]=round(avg_favorite,2)
    report["avg_retweet"]=round(avg_retweet,2)
    report["avg_sentiment"]=round(avg_sentiment,2)
    report["num_favorite"]=num_favorite
    report["num_negative"]=num_negative
    report["num_neutral"]=num_neutral
    report["num_positive"]=num_positive
    report["num_retweet"]=num_retweet
    report["num_tweets"]=num_tweets
    report["top_five"]=top_five_string
    return report
    #returns a dictionary




def sort_dict(dct,by_key=True,asc=True):#sorts dictionary based off your preference 
    index=1
    if by_key:
        index=0
    return dict(sorted(dct.items(), key=lambda item: item[index],reverse=not asc))    


def write_report(report, output_file):#writes the report basedd of the report made by make report
    try:
        write_file=open(output_file,"w")
        #writes all the values for based off of what they are
        write_file.write("Average sentiment of all tweets: %.2f \n"%report["avg_sentiment"])
        write_file.write("Total number of tweets: %d \n"%report["num_tweets"])
        write_file.write("Number of positive tweets: %d \n"%report["num_positive"])
        write_file.write("Number of negative tweets: %d \n"%report["num_negative"])
        write_file.write("Number of neutral tweets: %d \n"%report["num_neutral"])
        write_file.write("Number of favorited tweets: %d \n"%report["num_favorite"])
        write_file.write("Average sentiment of favorited tweets: %.2f \n"%report["avg_favorite"])
        write_file.write("Number of retweeted tweets: %d \n"%report["num_retweet"])
        write_file.write("Average sentiment of retweeted tweets: %.2f \n"%report["avg_retweet"])
        write_file.write("Top five countries by average sentiment: %s \n"%report["top_five"])
        print("Wrote report to [%s]"%output_file)
    except IOError:
        print("Could not open file [%s]" %output_file)    
    finally:
        write_file.close()

        
                   








