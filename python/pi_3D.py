import random

#doing the cool youtube question in 3D by using the volume of the sphere and the volume of the cube
def approximate_pi(n):
    points_in_circle = 0
    points_total = n
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        z = random.uniform(0,1)
        if x ** 2 + y ** 2 + z ** 2 <= 1:
            points_in_circle += 1
    return 6 * points_in_circle / points_total

#having some fun to understand whether the error goes down by multiplying the number of iterations
n = 1
for i in range(6):
    a = approximate_pi(n)          
    delta = a - 3.141592
    print(f"{a} result") 
    print(f"{delta} delta")
    n = n * 10