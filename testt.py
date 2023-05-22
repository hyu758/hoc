lst=[2,3,5,7,11,13,17,19]
for i in range (len(lst)):
    for j in range (len(lst)):
        for k in range (len(lst)):
            if lst[i]+lst[j]==lst[k]:
                print(f"{lst[i]} {lst[j]} {lst[k]}")