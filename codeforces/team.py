# # 231A. Team

def team():

    """ Counts the number of times a team can start to solve a problem
        returns the total count

        No argument is passed
    """
    num = int(input())
    count = 0

    for _ in range(num):
        num_list = list(map(int, input().split()))

        if sum(num_list) > 1:
            count += 1
    return count

def main():

    """ The main function of the program"""

    solve_count = team()

    print(solve_count)

if __name__ == "__main__":
    main()
