# Find the n Fibonacci of a number
def fib(n):
	if n < 2:
		return n
	return fib(n - 1) + fib(n - 2)


n = int(input("Enter number to find the Factorial: "))
print(fib(n-1))