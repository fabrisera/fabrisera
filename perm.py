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
b_1 = b	

#splits a string into pairs
def splitting(a, reverse):
	new = []
	pair = [None] * len(a)
	for i in range(len(a)):
		pair[i] = [None] * len(a[i])
		if reverse == False:
			for t in range(len(a[i])):
				pair[i][t] = a[i][t] + a[i][(t + 1) % len(a[i])]
		else:
			for t in range(len(a[i])):
				pair[i][t] = a[i][::-1][t] + a[i][::-1][(t + 1) % len(a[i])]					
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


def multiply(a, b, left = splitting(a, reverse = False), right = (splitting(b, reverse = False)), i = righti(used), n = 0):
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
	#delete from result the one cyle permutations and return		
	for r in reversed(result):
		if len(r) <= 1:
			result.remove(r)		
	return(result)		

def printing(result, a):
	#if no cycle, then we have the identity
	if len(result) == 0:
		 print(f"{a}: I")
	else:
		print(f'{a}: ' , end = '')
		for r in result:
			print(f'({r})', end = '')
		print()	
	return



#normal multiplication ab
first = multiply(a, b)
printing(first, a = 'ab')

used = []
#normal multiplication ba
second = multiply(b, a, left = splitting(b, reverse = False), right = splitting(a, reverse = False), i = righti(used), n = 0)
printing(second, a = 'ba')

used = []
#special multiplication aba^(-1)
#a_1 must be a list, not
third = multiply(first, a_1[0][::-1], left = splitting(first, reverse = False), right = splitting(a_1, reverse = True), i = righti(used), n = 0)
printing(third, a = 'aba^(-1)')

used = []
#special multiplication bab^(-1)
forth = multiply(second, b_1[0][::-1], left = splitting(second, reverse = False), right = splitting(b_1, reverse = True), i = righti(used), n = 0)
printing(forth, a = 'bab^(-1)')
