#Find the Sum of the First N Natural Numbers in Python
num = int(input('Enter the Natural Number'))
sum = 0
for i in range(num+1):
  sum+=i
print(sum)