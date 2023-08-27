# 339A Helpful maths

def summation(x: list):
    """returns the sorted summation form of the given list"""

    print("+".join(sorted(x)))


def main():
    """"The main function of the program"""

    list_input = input().split("+")
    summation(list_input)


if __name__ == "__main__":
    main()
