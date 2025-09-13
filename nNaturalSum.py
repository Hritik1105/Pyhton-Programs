# Python program to print sum of N natural numbers

number,sum = int(input('Enter The Natural Number:')),0
for i in range(number+1):
  sum+=i
print(sum)