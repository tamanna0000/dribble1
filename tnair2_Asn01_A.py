#""
# CS1026A 2023
#Assignment 01 Project 01 - Part A
#Tamanna Anandan Nair
#tnair2@uwo.ca
#5/10/2023
#""
#calcualtes the fibonacci sequence upto user inputted digit

print("Project One (01) - Part A : Fibonacci Sequence")
user=int(input("Sequence ends at: "))  #ask user to input the number of terms they want in sequence
num_0=0 #initialize the first  number in the sequence
num_1=1#initialize the second number in the sequence
total=0# initialize variables to keep track of the total sum 
count=0# to store the value of number of terms
for i in range(user+1): #loop to generate and print the sequence 
    if i==0:# for the first term(0), print it and its count
        print(str(count)+": 0 0")
    elif i==1:# for the second term(1), print it and its count
        count+=1
        print(str(count)+": 1 1")
    else:# for the rest of terms , calculate the next term and update variables
        num_2=num_0+num_1
        num_0=num_1
        num_1=num_2
        count=count+1
        print(str(count)+": "+ str(num_2), f'{num_2:,}')
print("\nEND: Project one (01) -  Part A") # print a message indicating the end of the project
print("Tamanna Nair tnair2 251311049")        
