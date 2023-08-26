# 282A Bit++

def bit(string_list: list):
    """Increase or decrease variable with given ++ or -- sign"""

    x = 0   # we start at 0

    for s in string_list:
        if "++" in s:
            x += 1
        elif "--" in s:
            x -= 1

    return x


def main():
    """main function of the program"""

    num = int(input())
    input_str = []

    for _ in range(num):
        input_str.append(input())

    count = bit(input_str)

    print(count)

if __name__ == "__main__":
    main()
