# To find the AutoMorphic Number
# AutoMorphic Number: A number whose square ends with the same number is known as an Automorphic number.
number = int(input('Enter The Number: '))
square = pow(number, 2)
mod = pow(10, len(str(number)))


if square % mod == number:
    print("It's an Automorphic Number")
else:
    print("It's not an Automorphic Number")