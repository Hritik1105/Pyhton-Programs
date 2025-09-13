# Abundant Number: A Number that is smaller than the sum of all it's factors except the number itself is known as an Abundant number.

n = int(input("Enter the number: "))

sum=1 

for i in range(2,n):
  if(n%i==0):  
   sum=sum+i

if(sum>n):
  print(n,'is Abundant Number')

else:
  print(n,'is not Abundant Number')