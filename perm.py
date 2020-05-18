''' For the program I need:
i = number which I am iterating
result[n]= the list of all the results
used = list of all the used values of i 
idea is to split them in a nice way? yes
so (12)(34) same priority and so 12 21 34 43 like this (324)(324)(3424)(234)(43)(423)
a and b must be lists of strings they, after splitting, have to turn into pairs so everythin wokrs nicely
'''
import re
a = str(input('Input first permutation: '))
b = str(input('Input second permutation: '))

a=re.split("\)\(", a)
for i in range(len(a)):
	a[i] = re.sub("\)", "", a[i])
	a[i] = re.sub("\(", "", a[i])
a_1 = a
b = re.split("\)\(", b)
for i in range(len(b)):
	b[i] = re.sub("\)", "", b[i])
	b[i] = re.sub("\(", "", b[i])

#splits a string into pairs
def splitting(a):
	new = []
	pair = [None] * len(a)
	for i in range(len(a)):
		pair[i] = [None] * len(a[i])
		for t in range(len(a[i])):
			pair[i][t] = a[i][t] + a[i][(t + 1) % len(a[i])]
	for l in pair:
		for s in l:
			new.append(s)	
	return(new)

def select(lis, i):
	for p in range(len(lis)):
		if str(i) == lis[p][0]:
			return int(lis[p][1])

used = []
#selects the correct value for i
def righti(used):
	i = 1
	while i in used:
		i += 1
	used.append(i)
	return(i)			


def multiply(a, b, left = splitting(a), right = (splitting(b)), i = righti(used), n = 0):
	a = ""	
	b = ""	
	for q in left:
		a += q	
	for q in right:
		b += q	
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
first = multiply(a, b)
printing(first, a = 'ab')
print(first)

used = []
#normal multiplication ba
second = multiply(b, a)
printing(second, a = 'ba')

used = []
#special multiplication aba^(-1)
print(f"here {a_1[0][::-1]}")
third = multiply(first, a_1[0][::-1], left = splitting(first), right = splitting(a_1[0][::-1]), i = righti(used), n = 0)
print(third)
printing(third, a = 'aba')