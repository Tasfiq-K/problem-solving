def string_reverse(s: str) -> str:
    """
    Reverse a string recursively.
    
    Args: 
        s: str: A string
    
    returns: str: Reversed form of the input string, outputs None if the string is empty.
    """

    if len(s) == 1:
        return s
    elif len(s) == 0:
        return 
    
    return s[-1] + string_reverse(s[:-1])

def main():

    user_input = input("Enter a string: ")
    print(string_reverse(user_input))

    return

if __name__ == "__main__":
    main()