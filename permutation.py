''' ideas for the permutation

1) taking user input: 
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

#selects the pair with the correct starting number
def select(lis, i):
	for p in range(len(lis)):
		if str(i) == lis[p][0]:
			return lis[p]
	return None		

def goodi(i, lis, m):
	for t in range(m):
		if str(i) in lis[t]:
			i += 1
			goodi(i, lis, m)
	return i		
	
def isgood(i, lis, m):
	for t in range(m):
		if str(i) in lis[t]:
			return False
	return True
	

# split the two strings into pairs of two
s2 = splitting(a)
s1 = splitting(b)
r = None
m = 0
i = 1
result = [None] * len(a + b)

while int(i) <= 9:
	print(result)	
	#if the current number is in the right string then select the correct pair
	if str(i) in b:
		l = select(s1, i) 
		print(f'l: {l}')
		#if then the right number is in the left string, then we have the middleman case	
		if select(s2, l[1]) is not None:
			l_a = select(s2, l[1]) 
			l = l[0] + l_a[1]
		#in both the cases, we have obtained a correct pair, if it is the first, then set r	
		if r == None:
			r = l
		#if r is already set, then check if we are done and update result, resetting r which is the kind of working memory
		else:
			if r[0] == l[1]:
				result[m] = r
				m += 1	
				r = None
				print(f' 67 is {i}')
				i = goodi(i, result, m)
			#add the digit to r	
			else:
				r = r + l[1]
				result[m] = r
				i = int(result[m][len(result[m]) - 1]) 
				print(f' 73 is {i}')		
	#if the current number is not in the left string and only in the right string, then select the right pair and save it to r			
	elif str(i) in a:
		l = select(s2, i)
		if r == None:
			r = l
		#if r is already set, then check if we are done and update result, resetting r which is the kind of working memory
		else:
			if r[0] == l[1]:
				result[m] = r
				m += 1	
				r = None
				print(f' 86 is {i}')
				i = goodi(i, result, m)
			#add the digit to r	and chose i to be the last number
			else:
				r = r + l[1]
				result[m] = r
				i = int(result[m][len(result[m]) - 1])
				print(f' 91 is {i}')
	#if i is not in the right nor in the left string, then			
	else:
		i = goodi(1, result, m)
		m += 1
		result[m] = i		


			
print(result)				




