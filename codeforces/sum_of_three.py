def sumOfThree():

    for _ in range(int(input())):
        n = int(input())
        if n <= 6 or n == 9:
            print("NO")
            continue
        
        if (n - 3) % 3:
            print("YES")
            print(n - 3, 2, 1)
        elif (n - 5) % 3:
            print("YES")
            print(n - 5, 4, 1)
        else:
            print("NO")

if __name__ == "__main__":
    sumOfThree()