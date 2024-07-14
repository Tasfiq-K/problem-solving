def design_door_mat(n, m):
    # cols = 3 * rows

    # mid = rows // 2 + 1
    # des_1 = ".|."
    # des_2 = "-"
    # design = ""
    # welcome_len = len("welcome")

    # des_1_len = len(des_1)
    # nums = []
    
    
    # for i in range(1, mid):

    #     des_1_amnt = (2 * i - 1)
    #     des_2_amnt = ((cols) - des_1_amnt * des_1_len) // 2
    #     design += f"{(des_2_amnt) * des_2}{des_1_amnt * des_1}{des_2_amnt * des_2}\n"

    #     nums.append((des_2_amnt, des_1_amnt))

    # design += f"{((cols - welcome_len) // 2) * des_2}WELCOME{((cols - welcome_len) // 2) * des_2}\n"
    
    # for i in nums[::-1]:
    #     design += f"{(i[0]) * des_2}{i[1] * des_1}{i[0] * des_2}\n"

    # n, m = map(int,input().split())
    pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
    print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

    
    # return design

if __name__ == "__main__":

    n, m = map(int, input().split())

    # design = design_door_mat(n, m)
    design_door_mat(n, m)
    # print(design)

