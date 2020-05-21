def finddiv(i):
    list = []
    for p in range(1, i + 1):
        if i % p == 0:
            list.append(p)
    return(list)  

#takes the coprime and the original number
def comp_order(i, q):
    temp = i
    order = 1
    while i != 1:
        i = (i * temp) % q
        order += 1
    return(order)    

#q is the integer from the user
q = int(input("Insert an integers 0 < q < 50: "))
#checks that q is valid
if q < 1 or q >=50:
    print("int out of range")
    exit()  


#finding the list of all the divisors the  numbers <= q the list has [0] and then all the other numbers in the correct location
divisors = [[0]]   
for i in range(1, q + 1):
    list = finddiv(i)
    divisors.append(list)

#creates a list of coprimes
coprimes = {}
orders = [0]
#boolean to decide whether to add to the coprime list
add = True
#iterates over every list linked to each number
for element in divisors:
#iterates over every i
# nt of each list
    for number in element:
        if number != 1 and number in divisors[q]:
            add = False
    if add == True and number != 0:     
        #adds the coprime in the dict with the relative order and creates a list of orders       
        coprimes.update({divisors.index(element): comp_order(divisors.index(element), q)})
    else:
        add = True           

coprimes_values = (coprimes.keys())  
print(coprimes_values)     

#initialize a dict of totorders and frequency of those orders
frequency = {}
values = (coprimes.values())
for i in values:
    totorders = (frequency.keys())
    if i in totorders:
        frequency[i] += 1
    else:
        frequency.update({i: 1})    

for element in frequency:
    print(f"There is/are {frequency[element]} element/s of order {element}")


#create a two dimetnional list with the multiplications in modulo 
row = []
table = []
for left in coprimes_values:
    for right in coprimes_values:
        row.append((left * right) % q)
    table.append(row)
    row = []    

print(end = "   | ")
for i in table[0]:
    if i < 10:
        print(f"{i}  |", end = " ")
    else:
        print(f"{i} |", end = " ") 


print()
print("-" * len(table[0] * 6))
c = True
for i in table:
    for t in i:
        if c == True:
            if t < 10:
                print(f"{t}  |", end = " ")
            else:
                print(f"{t} |", end = " ")    
            c = False
        if t < 10:
            print(f"{t}  |", end = " ")
        else:
            print(f"{t} |", end = " ")  
    print()
    print("-" * len(table[0] * 6))   
    c = True

