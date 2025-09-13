#Find the Sum of the Numbers in a Given Interval in Python Language

num1, num2 = int(input('Enter Starting Number')),int(input('Enter Last Number'))
sum = 0
for i in range(num1,num2+1):
  sum+=i
print(sum)