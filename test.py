while True:
	a = input('Input first permutation: ')
	b = input('Input second permutation: ')
	if a.isdigit() or b.isdigit():
		break
	print("can only insert digits")	

print(len(b))
print(b)