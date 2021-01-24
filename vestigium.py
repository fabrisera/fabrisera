def checkrepeat (arr):
    if len(arr) == len(set(arr)):
        return 0
    else:
        return 1    

t = int(input())
# iterating over all the test cases
for case in range(t):
    trace = 0
    row_repeat = 0
    col_repeat = 0
    columns = []
    n = int(input())
    # creating all the column arrays to prepare checkrepeat
    for _ in range(n):
        columns.append([])    
    for i in range(n):
        row = (list(map(int,input().strip().split())))
        check = []
        skip = False
        for index in range(n):
            if not skip:               
                if row[index] in check:
                    row_repeat += 1
                    skip = True
            check.append(row[index])
            columns[index].append(row[index])    
    # iterating over the columns and checking for repetitions and computing the trace        
    for index in range(len(columns)):
        col_repeat += checkrepeat(columns[index])
        trace += columns[index][index]
    print("Case #{}: {} {} {}".format(case + 1, trace, row_repeat, col_repeat))