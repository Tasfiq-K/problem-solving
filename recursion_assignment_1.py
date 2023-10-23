
def count_digit(num: int, count=1) -> int:
    """
    Takes a number as input and counts how many digits are there, recursively.
    Args: 
        num: int: an integer number (takes from user)
        count: int: count value, default 1

    returns: int: Total number of digits
    """
    
    floored_num = abs(num) // 10 # 2, 0
    if floored_num == 0:
        return count
    

    count += 1
    return count_digit(floored_num, count)


def main():

    user_input = int(input("Enter an integer number: ")) # well it's going to make it an integer even if it's not, :p
    counting_digits = count_digit(user_input)
    print(counting_digits)

if __name__ == "__main__":
    main()
