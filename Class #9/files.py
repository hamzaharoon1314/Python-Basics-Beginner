# open/open modes
animals = open('animals.txt', 'a+')
# r  = open for read (default)
# w  = open for write, truncate
# r+ = open for read/write
# a+ = open for read/append
# w+ = open for read/write, truncate

# read
text = animals.read()
print text
animals.seek(0)

# read lines
for animal in animals:
	print animal,

# write/append
animals.write('Mouse\n')
animals.write('Fish\n')

# close
animals.close()
