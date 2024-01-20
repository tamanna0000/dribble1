#library of all books currently stored
allBooks = [
                ['9780596007126',"The Earth Inside Out","Mike B",2,['Ali']],
                ['9780134494166',"The Human Body","Dave R",1,[]],
                ['9780321125217',"Human on Earth","Jordan P",1,['David','b1','user123']]
           ]
#List that will hold borrowed isbns
borrowedISBNs = []

list = ['a', 'r', 't', 'l', 'x'] #list of acceptable characters
def start(): #def start function
    printMenu()
    #Asks for user input and chooses the correct option based off user
    user = input("Your selection> ")
    while True:
        #checks for characters first
        if(user.lower() in list):
            if(user.lower() == list[0]):
                addBook()
                printMenu()
                user = input("Your selection> ")
            elif(user.lower() == list[1]):
                borrowBook()
                printMenu()
                user = input("Your selection> ")
            elif(user.lower() == list[2]):
                returnBook()
                printMenu()
                user = input("Your selection> ")
            elif(user.lower() == list[3]):
                listBooks()
                printMenu()
                user = input("Your selection> ")
            elif(user.lower() == list[4]):
                exit()
                break
            #if no characters then asks again
            else:
                print("Wrong selection! Please selection a valid option.")
                printMenu()
                user = input("Your selection> ")  
        #checks for integers if a character is not inputted 
        else:
            try: #checks if character is inputted and catches the error
                if(int(user) == 1):
                    addBook()
                    printMenu()
                    user = input("Your selection> ")
                elif(int(user) ==2):
                    borrowBook()
                    printMenu()
                    user = input("Your selection> ")
                elif(int(user) == 3):
                    returnBook()
                    printMenu()
                    user = input("Your selection> ")
                elif(int(user) == 4):
                    listBooks()
                    printMenu()
                    user = input("Your selection> ")
                elif(int(user) == 5):
                    exit()
                    break
                else:
                    print("Wrong selection! Please selection a valid option.") 
                    printMenu()
                    user = input("Your selection> ")
            #catches the error and prints wrong selection
            except(ValueError):
                print("Wrong selection! Please selection a valid option.")
                printMenu()
                user = input("Your selection> ") 






    

#Adds the book name
def bookName():
    bookName=input("Book Name> ")
    while "*" in bookName or  "%" in bookName:#validates the book name 
        print("Invalid book name!")
        bookName=input("Book Name>")
    return bookName

#adds the Author
def authorName():
    author=input("Author name> ") 
    return author #no validation required
    
#adds the editon
def edition():
    while True:     
        try:#validates if an integer is inputted
            edition=int(input("Edition> "))
        #if non integer is inputted it catches the error
        except ValueError:
            print("Invalid edition!") 
            continue
        else:
            break
    return edition #returns the edition

#chekcs if the isbn value is valid 
def isbnVal(isbn):
    sum = 0
    strIsbn = str(isbn)
    for i in range(0, len(strIsbn)): 
        if (i % 2 == 0):
            sum += int(strIsbn[i])
        else:
            sum += int(strIsbn[i])*3

    return sum

#adds the isbn value
def isbn():
    while True:
        try:#checks if the ISBN value is only integer 
            isbn=int(input("ISBN>"))  
            while len(str(isbn)) < 13 or len(str(isbn))>13:
                print("Invalid ISBN!")
                isbn=int(input("ISBN>"))  
        except ValueError:#catches the error if non integer
            print("Invalid ISBN!") 
            continue
        else:
            break
    
    sum = isbnVal(isbn)#gets the ISBN value back from the isbnVal() 
    if(sum%10!=0): #checks if its a multiple of 10
        return 0 
    else:  
        return str(isbn)




# adds the book if not already in the library 
def addBook():
    #gets all information to add a book 
    bookName1 = bookName()
    authorName1 = authorName()
    edition1 = edition()
    isbn1 = isbn()
    #adds the information into a list called one new book 
    oneNewBook = [str(isbn1), bookName1, authorName1, edition1,[]]
    for i in range (0, len(allBooks)):
        if(isbn1 != 0):#checks if the ISBN value is valid 
            if(oneNewBook[0] != allBooks[i][0]):#checks to see if the ISBN value is already in the library
                isAdded = False
            else:
                isAdded = True
                break
        else:
            isAdded = True
        
    if(not isAdded):#if the ISBN is not added then it adds the book 
        allBooks.append(oneNewBook)
        print("A new book is added successfully.")
    elif(isbn1 == 0):#if the ISBN value is invalid
        print("Invalid ISBN!")
    else:#if its duplicate
        print("Duplicate ISBN is found! Cannot add the book.")


def containsMethod(term): #checks if the term is found anywhere in the book name 
    contains = []
    for i in range (0, len(allBooks)):
        if(term.lower() in (allBooks[i][1]).lower()):#goes through the whole library to see if the book is in the library
            if(allBooks[i][0] not in borrowedISBNs):#checks if the book is available
                contains.append(allBooks[i][1])
    if(len(contains) == 0):#if no books found prints no books 
        print("No books found!")
    return contains     
    
def startsMethod(term):#checks if the term is found in the beginning of  the book name
    starts=[]
    for i in range (0,len(allBooks)):
        firstWord=(allBooks[i][1]).split()#splits the book name to get just the first word
        if(term.lower() in (firstWord[0]).lower()):
            if(allBooks[i][0] not in borrowedISBNs):#checks if the book is available
                starts.append(allBooks[i][1])
    if (len(starts)==0):
        print("No books Found!")
    return(starts)   


def exactMethod(term):#searches for exact matches in the library
    exact=[]
    for i in range (0,len(allBooks)):
        if (term.lower() ==(allBooks[i][1]).lower()):#lowers the book name to check with the library
            if(allBooks[i][0] not in borrowedISBNs):#checks if the book is borrowed
                exact.append(allBooks[i][1])
    if(len(exact)==0): 
        print("No books found!")
    return(exact)     


 
def borrowBook():#function that borrows a book
    user = input("Enter the borrower name> ")
    term = input("Search term> ")
    if "*" in term:#searches to see if * is in the term search
        term = term.replace("*","")
        contains= containsMethod(term.lower())#calls the contains method to get the appropriate books 
        for i in range(0, len(allBooks)):
            for j in contains:
                if(j == allBooks[i][1]): #if the book name is found adds the borrowers name  and records the borrowed isbn
                    allBooks[i][4].append(user)
                    borrowedISBNs.append(allBooks[i][0])   

        for i in range(0,len(contains)):
            print('- "{}" is borrowed!'.format(contains[i]))

    elif("%" in term):#searches to see if there is a % sign in the term search
        term=term.replace("%","")
        starts=startsMethod(term.lower())#calls the starts method to get the appropriate book name 
        for i in range(0, len(allBooks)):
            for j in starts:
                if(j == allBooks[i][1]):#checks if the bookname is in the library
                    allBooks[i][4].append(user)
                    borrowedISBNs.append(allBooks[i][0])        
        for i in range(0,len(starts)):
            print('- "{}" is borrowed!'.format(starts[i]))

    else:
        exact=exactMethod(term.lower())#calls the exact method to get the appropriate book name
        for i in range(0, len(allBooks)):
            for j in exact:
                if(j == allBooks[i][1]):#if the book name is found adds the borrowed user and borrowed ISBN
                    allBooks[i][4].append(user)
                    borrowedISBNs.append(allBooks[i][0])
        for i in range(0,len(exact)):
            print('- "{}" is borrowed!'.format(exact[i]))


def returnBook():#function that returns a book
    return_isbn = input("ISBN> ")#asks user for the ISBN
    if return_isbn in borrowedISBNs:#if the ISBN is in the borrowed ISBN then return the book
        borrowedISBNs.remove(return_isbn)
        for i in range(0 , len(allBooks)):
            if(return_isbn in allBooks[i]):#gets the name of the borrowed ISBn
                name = allBooks[i][1]
        print(' "{}" is returned.'.format(name))#prints that the book is returned 
    else:
        print("No book is found!")


def listBooks():#fucntion for listing all the books 
    if(len(allBooks) != 0):
        for i in range(0, len(allBooks)):
            print("---------------")
            if(allBooks[i][0] in borrowedISBNs):#checks if the book is available or not
                print("[Unavailable]")
            else:
                print("[Available]")
            print(allBooks[i][1] + " - " + allBooks[i][2])#prints the book name and the author
            print("E: " + str(allBooks[i][3]) + " ISBN: " + allBooks[i][0])#prints the addition and ISBN
            print("borrowed by: " + str(allBooks[i][4]))#prints the name of those who borrowed the book
    else:
        print("")
    
def exit():#fucntion that exits 
    print("")
    print("$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")
    listBooks()#prints final list of books 
    


    
def printMenu():#prints the menu for the library
     print('\n######################')
     print('1: (A)dd a new book.')
     print('2: Bo(r)row books.') 
     print('3: Re(t)urn a book.') 
     print('4: (L)ist all books.') 
     print('5: E(x)it.') 
     print('######################\n')

start()
