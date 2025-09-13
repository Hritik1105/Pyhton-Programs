# To convert the Binary to a Decimal

num = int(input("Enter The Binary Number"))
binary = num
decimal = 0
base = 1

while num > 0:
    rem = num % 10
    decimal = decimal + rem * base
    num = num // 10
    base = base * 2

print("Binary Number is {}\nDecimal Number is {}".format(binary, decimal))