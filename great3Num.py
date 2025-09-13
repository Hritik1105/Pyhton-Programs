# Find the Greatest of the Three Numbers​ in Python

num1, num2, num3 = int(input("Enter First Number: ")),int(input("Enter Second Number: ")),int(input("Enter Third Number: "))
max = 0
if num1 >= num2 and num1 >= num3:
  print(num1)
elif num2 >= num1 and num2 >= num3:
  print(num2)
else:
  print(num3)