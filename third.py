#fermat number
p = 2**16 + 1

number = int(input("Insert a number between 1 and Fermat's prime"))
if number > p or number < 1:
    print("invalid number")
    exit()
