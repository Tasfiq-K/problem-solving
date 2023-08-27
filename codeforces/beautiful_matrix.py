# 263A beautiful matrix


def beautiful_matrix(matrix: list, mid: int):

    """ function for the beautiful matrix problem """

    for row, elem in enumerate(matrix):
        for col in range(len(elem)):
            if matrix[row][col] > 0:

                return (abs(mid - row) + abs(mid - col))


def main():

    """ main function for the program """

    n_rows = 5
    mid = 2
    mat = [list(map(int,input().split())) for i in range(n_rows)]
    distance = beautiful_matrix(mat, mid)
    print(distance)


if __name__ == "__main__":
    main()
