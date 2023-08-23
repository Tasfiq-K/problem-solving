# codeforces 71A. too long words

def long_words(string: list):
    out_list = []
    for s in string:
        if len(s) > 10:
            out_list.append( s[0]+str(len(s[1:-1]))+s[-1] )
        else:
            out_list.append(s)
            
    print(*out_list, sep='\n')

def main():

    num, str_list = int(input()), []

    for n in range(num):
        str_list.append(input())

    long_words(str_list)


if __name__ == "__main__":
    main()

    