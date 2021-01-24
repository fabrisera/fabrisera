t = int(input())
for t_case in range(t):
    times = []
    c_free = 0
    j_free = 0
    result = ""
    var = True
    n = int(input())
    for i in range(n):
        times.append((list(map(int,input().strip().split()))))
    times.sort()
    for slot in times:
        if slot[0] >= c_free:
            result += "J"
            c_free = slot[1]
        elif slot[0] >= j_free:
            result += "C"
            j_free = slot[1]
        else:
            print("Case #{}: IMPOSSIBLE".format(t_case + 1))
            var = False
            break        
    if var:
        print("Case #{}: {}".format(t_case + 1, result))