def main():
    banana_cost, init_money, banana_want = list(map(int, input().split()))

    if banana_want == 0:
        print(0)
    else:
        total_cost = 0
        for i in range(banana_want):
            total_cost += banana_cost * (i + 1) 
        if total_cost > init_money:
            print(total_cost - init_money)
        else:
            print(0)

if __name__ == "__main__":
    main()