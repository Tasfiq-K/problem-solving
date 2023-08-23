# codeforces A. watermelon

def watermelon(x):
    w = x
    if w % 2 == 0 and w != 2:
        print("YES")
    else:
        print("NO") 

watermelon(int(input()))
