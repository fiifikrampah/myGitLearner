def collatz(num):
    # if num is even
    while (num > 1):
        if num % 2 == 0:
            num = num / 2 
            print(num)
        # else num is odd
        else:
            num = (3 * num) + 1
            print(num)

collatz(10)