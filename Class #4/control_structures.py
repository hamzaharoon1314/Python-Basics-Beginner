# if/else/elif
Age = 21

if Age >= 18:
	print 'is an adult'
elif Age >= 12:
	print 'is a young adult'
elif Age >= 3:
	print 'child'
else:
	print 'baby'

# ternary
if Age >= 21:
	old_enough = True
else:
	old_enough = False

old_enough = True if Age >= 21 else False

# while
while Age < 50:
	print 'Current Age is %d, not Old Eough' % Age
	Age += 1
