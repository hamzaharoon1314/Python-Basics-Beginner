# definition
def my_fn():
	# your code
	print 'Hello! Hamza'

# arguments/return
def add(num1, num2):
	return num1 + num2

# multiple return
def square(num1, num2):
	return num1**2, num2**2

# calling
my_fn()
result = add(num2=1, num1=2)
print result
result1, result2 = square(1, 2)
print result1, result2
