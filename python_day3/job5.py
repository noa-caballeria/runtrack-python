def prime_number():
    for i in range(2,1001):
        x = 0
        for j in range(2,i):
            if (i % j == 0) and (j != 0) and (j != 1):
                x = x + 1
        if x == 0:
            print(i)
prime_number()
        