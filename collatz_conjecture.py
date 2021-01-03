#this is a super short program that allows to test the Collatz Conjecture
number = int(input("Begin here: "))
count = 0
if number == 4:
    print("Too easy!")
    exit()
while number != 4:
    if number % 2 == 0:
        number = int(number / 2)
    else:
        number = number * 3 + 1
    print(number)
    count += 1 
print("The total number of steps are:")    
print(count) 
