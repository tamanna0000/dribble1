#""
# CS1026A 2023
#Assignment 01 Project 01 - Part B
#Tamanna Anandan Nair
#tnair2@uwo.ca
#5/10/2023
#""
#finds whether the number inputted by the user is prime or not

def check_prime(n):#function to check if a number is prime
    if n<= 1: # if n is less than or equal to 1 its not prime
        return False
    if n<=3: # if n is less than 3 its prime
        return True
    if n % 2 == 0 or n% 3 == 0: #if n is divisible by 2 or 3 its not prime
        return False
    i=5
    while i*i <=n:# check divisibility upto the square root of n
        if n% i ==0 or n% (i+2) ==0:# if n is divisible by i or i+2, its not prime
            return False
        i+=6
    return True # if none of the above conditions are met n is prime
#function to find prime numbers in a given range    
def find_Prime(start,end):
    primes=[]
    for num in range(start, end+1):
        if check_prime(num):# check if num is prime using check_prime function
            primes.append(num)# if num is prime add it to the list of prime numbers
    return primes
print("Part one - Project B: Prime Choice\n")

try:
    start = int(input("Prime Numbers starting with:"))
    end= int(input("and ending with:"))
    print() # check if the start if greater than end and swap them if needed

    if start > end:
       print(f"Incorrect input: {start} is greater than {end}\nThe numbers have been automatically switched.")
       start,end=end,start

    primes= find_Prime(start,end)#find prime numbers in the given range
    print(f"Prime numbers in the range from: {start} and {end} are:")
    for prime in primes:
       print(f"{prime} is prime")#printing each prime number

except:
    ValueError:print("Please enter valid integers")#handle the case where non integer inputs are provided
    #(I can add pass if I have no except condition code will run(for my refrence))

print("\nEnd part one (01) - Project B")
print("Tamanna Nair tnair2 251311049")
