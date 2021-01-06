#fermat number
p = 2**16 + 1


#gcd
def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd (b % a, a)    
number = int(input("Insert a number between 1 and Fermat's prime: "))
if number > p or number < 1:
    print("invalid number")
    exit()

grand = gcd(number, p)
print(grand)