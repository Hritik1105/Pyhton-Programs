# method to print the divisors
def printDivisors(n) :
    i = 1
    while i <= n :
        if (n % i==0) :
            print (i,end=" ")
        i = i + 1
         
num= int(input("Enter the Number: "))
print (f'The divisors of {num} are: ')
printDivisors(num)