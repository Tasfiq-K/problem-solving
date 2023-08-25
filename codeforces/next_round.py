# codeforces, 158A next round

def next_round(array, pos, length):

    """ It's just a binary search, with descending order
        returns the right most index if the passed positional number occurs more than once

        Args: array: an array of numbers, e.g. a list
              pos: positon of the number in the array
              length: total length of the array
        
        returns: returns the index of the given positional number (right most number if the number occurs more than once).
    """

    key = array[pos-1]
    begin = 0
    end = length - 1
    index = None
 
    while begin <= end:

        mid = (begin + end) // 2
        # print(f"mid: {mid}")
        if array[mid] == key:
            index = mid
            begin = mid + 1# continue search for the right portion after one occurence is found
        elif array[mid] > key:
            begin = mid + 1
        elif array[mid] < key:
            end = mid - 1

    return index


def main():
    """ Main function of this program, runs the next_round function and performs the countng operation based on the 
        index returned by the next_round function.
        
    """
    length, pos = map(int, input().split(' '))
    count = 0
    array = list(map(int, input().split()))
    print(array)
    idx = next_round(array, pos, length)

    for i in array[:idx + 1]:
        if i > 0:
            count += 1

    print(count)

if __name__ == "__main__":
    main()
