# 118A String Task


# deletes all the vowels,
# inserts a character "." before each consonant,
# replaces all uppercase consonants with corresponding lowercase ones. 

# Vowels are letters "A", "O", "Y", "E", "U", "I", and the rest are consonants. The program's input is exactly one string, 
# it should return the output as a single string, resulting after the program's processing the initial string.

def modify_string(s: str):

    """ modify the string inplace"""

    new_string = ''
    for c in s.lower():
        if c in "aeiouy":
            s = s.replace(c, "")
        else:
            new_string += '.' + c
    print(new_string)


def main():
    """main function of the program"""

    input_string = input()
    modify_string(input_string)

if __name__ == "__main__":
    main()
