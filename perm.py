''' For the program I need:
i = number which I am iterating
result[n]= the list of all the results
used = list of all the used values of i 


'''
while True:
	a = input('Input first permutation: ')
	b = input('Input second permutation: ')
	if a.isdigit() or b.isdigit():
		break
	print("can only insert digits")	
#splits a string into pairs
def splitting(a):
	pair = [None] * len(a)
	for i in range(len(a)):
		pair[i] = a[i] + a[(i + 1) % len(a)]
	return(pair)

def select(lis, i):
	for p in range(len(lis)):
		if str(i) == lis[p][0]:
			return int(lis[p][1])
	return print("select returns None")		

used = []
#selects the correct value for i
def righti(used):
	i = 1
	while i in used:
		i += 1
	used.append(i)
	return(i)			


def multiply(a, b, left = splitting(a), right = (splitting(b)), i = righti(used), n = 0):
	result = []
	for p in range(9):
		result.append('')
	while i <= 9:
		#if i is in b then since it is right it can be immediatly written into result, and then we can select the new i
		if str(i) in b:
			if len(result[n]) == 0:	
				result[n] += str(i)	
			i = select(right, i)
			#if the newi is in a, then we have to pick the newnew i
			if str(i) in a:
				i = select(left, i)
				#if the newnew i is the same as the original i, then we have just to close result and pick a new good i, else we just insert in in result and repeat
				if result[n][0] == str(i):
					for p in result[n]:
						used.append(int(p))
					n += 1
					i = righti(used)
				else:
					result[n] += str(i)
			#id new i is not in a, then we have to pick the newnew i in b and chech whether it is the same as result		
			else:
				if result[n][0] == str(i):
					for p in result[n]:
						used.append(int(p))
					n += 1
					i = righti(used)
				else:
					result[n] += str(i)	
		#now, if the new i is not in b but is in a then we have to write it 	
		elif str(i) in a:
				if len(result[n]) == 0:
					result[n] += str(i)
				i = select(left, i)
				if result[n][0] == str(i):
					for p in result[n]:
						used.append(int(p))
					n += 1
					i = righti(used)
				else:
					result[n] += str(i)			
		else:	
			i = righti(used)
	for r in reversed(result):
		if len(r) <= 1:
			result.remove(r)		
	return(result)		

def printing(result, a):
	if len(result) == 0:
		 print(f"{a}: identity")
	else:
		print(f'{a}: ' , end = '')
		for r in result:
			print(f'({r})', end = '')
		print()	
	return



#normal multiplication ab
first = multiply(a, b, left = splitting(a), right = (splitting(b)), i = righti(used), n = 0)
printing(first, a = 'ab')

used = []
#normal multiplication ba
second = multiply(b, a, left = splitting(b), right = (splitting(a)), i = righti(used), n = 0)
printing(second, a = 'ba')




		