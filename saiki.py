def saiki_x(x):
	b = 0
	if x == 0:
		return 1
	else:
		b = x * saiki_x(x-1)
	return b

a = input("type a num:")
a = int(a)

a = saiki_x(a)
print(a)
