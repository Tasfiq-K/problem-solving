

numOfCases = int(input())

cases = [ int(input()) for _ in range(numOfCases) ]

for case in cases:
    i = 1
    non_divisible = []
    while i != case:
        if i % 3 != 0:
            non_divisible.append(i)
        i += 1
    
    found = []

    for x in non_divisible:
        for y in non_divisible[1:]:
            for z in non_divisible[2:]:
                if (x != y != z) and x + y + z == case:
                    found.append((x, y, z))
                    break


    if len(found) > 0:
        print("YES")
        print(*found[0])
    else:
        print("NO")
    

