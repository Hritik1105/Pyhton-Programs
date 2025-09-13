# Find The Sum OF Digit Of A Number

num = int(input("Enter the Number"))  #Take Integer Input From The User
sum = 0      #Assigning The Sum Variable To Zero

while num!=0:
	digit = int(num%10)
	sum += digit
	num = num/10

print(sum)