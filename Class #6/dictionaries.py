# initialize
my_dicto = {}

# add item
my_dicto['name'] = 'Hamza'
my_dicto['state'] = 'PUNJAB'
my_dicto['age'] = 21

# access item
print my_dicto['name']

# change item
my_dicto['name'] = 'Hamza Haroon'

# remove item by index
del my_dicto['state']

# iterate
for k, v in my_dicto.iteritems():
	print k, '=>', v
