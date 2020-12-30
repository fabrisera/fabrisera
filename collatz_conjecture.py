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
    print(f"{number},", end = "")
    count += 1 
print(f"\n{count}")    

            