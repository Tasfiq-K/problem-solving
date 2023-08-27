# 112A petya and strings

def compare_string(str1: list):
    """compare two strings and outputs 1 if str1 is greater than str2, -1 if str1 < str2
    and 0 if they are equal
    """

    if str1[0].lower() > str1[1].lower():
        return 1

    if str1[0].lower() < str1[1].lower():
        return -1

    return 0

def main():
    """main function of the program"""

    input_string = []
    # take input
    for _ in range(2):
        input_string.append(input())
    print(input_string)
    comparison = compare_string(input_string)

    print(comparison)


if __name__ == "__main__":
    main()
