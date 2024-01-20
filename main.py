from sentiment_analysis import *
#imports all method from sentiment analysis



def main():#defining main function
    #ask the user for all 3 file names
    key_file=input("Input keyword Filename (.tsv file): ")
    tweet_file=input("Input tweet filename (.csv file): ")
    report_file=input("Input filename to output report in (.txt file): ")
     
     #makes sure if the file extensions are correct 
    if '.tsv' not in key_file:
        raise Exception(" Must have tsv file extension !")
    if '.csv' not in tweet_file:
        raise Exception(" Must have csv file extension !")
    if '.txt' not in report_file:
        raise Exception(" Must have txt file extension !")
    if read_keywords(key_file)=={} or read_tweets(tweet_file)==[]:
        raise Exception("Tweet list or keyword dictionary is empty!")
        
    reading=read_tweets(tweet_file)#reads tweets from file
    report=make_report(reading,key_file)#makes report based off of the tweet list
    write_report(report,report_file)#writes the report to the given file name


    
    
main()#calls the main function
    
