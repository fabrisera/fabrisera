t = int(input())
#iterate over the test cases
for t_case in range(t):
    times = []
    c_free = 0
    j_free = 0
    var = True
    n = int(input())
    #initialize the result list with n list of "C" which will be modified while iterating over the slots
    result = ["C"] * n
    for i in range(n):
        times.append((list(map(int,input().strip().split()))))
        #append the index in each array to keep track of the original position after sorting
        times[i].append(i)
    times.sort()
    #iterate over each slot and verity whether it can be assigned, else impossible and break
    for slot in times:
        #if c is free then his name is already in the result list, just update the free will be time
        if slot[0] >= c_free:
            c_free = slot[1]
        #if j is free then change the list within the result list from C to J and update the will be free time
        elif slot[0] >= j_free:
            result[slot[2]] = "J"
            j_free = slot[1]
        #if both c and j are already busy, then print IMPOSSIBLE and break   
        else:
            print("Case #{}: IMPOSSIBLE".format(t_case + 1))
            var = False
            break      
    #if everything is possible then print the result      
    if var:
        string = ""
        for char in result:
            string += char
        print("Case #{}: {}".format(t_case + 1, string))