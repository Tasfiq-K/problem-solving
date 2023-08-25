# 50A. Domino piling

def pile_domino(m, n, domino_size=2):
    """ Takes two number from users, and with domino size = 2,
        it returns the max number of domino could fit inside the m x n board
    """

    return (m * n) // domino_size

def main():
    """ The main function to take user input and process the 
    domino count using the pile_domino function
    """

    m, n = map(int, input().split())

    count = pile_domino(m, n)

    print(count)

if __name__ == "__main__":
    main()

# solved