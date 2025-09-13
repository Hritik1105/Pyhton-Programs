# To Check Armstrong number in Range

low, high = int(input('Enter Low Number: ')),int(input('Enter High Number: '))

for n in range(low, high + 1):

    # order of number
    order = len(str(n))

    # initialize sum
    sum = 0

    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if n == sum:
        print(n, end=", ")