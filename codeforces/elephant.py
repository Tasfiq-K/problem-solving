def main():
    coords = int(input())
    if coords > 0 and coords < 5:
        print(1)
    elif coords % 5 != 0:
        print(coords // 5 + 1)
    else:
        print(coords // 5)

if __name__ == "__main__":
    main()