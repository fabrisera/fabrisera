def open(n):
    print("(" * n, end ="")

def close(n):
    print(")" * n, end="")    

def split(str):
    return [int(char) for char in str]

t = int(input())
for t_case in range(t):
    str = input()
    string = split(str)
#    string = (list(map(int,input().strip().split())))
    print("Case #{}: ".format(t_case + 1), end="")
    open(string[0])
    print(string[0], end="")
    for index in range(1, len(string)):
        current = string[index - 1]
        nxt = string[index]
        delta = nxt - current
        if delta >= 0:
            open(delta)
            print(nxt, end="")
        if delta < 0:    
            close(-delta)
            print(nxt, end="")
    close(string[len(string) - 1])
    print()