def fizz_and_buzz():
    for x in range(1,101):
        if (x%3==0):
            print("Fizz")
        elif (x%5==0):
            print("Buzz")
        elif (x == 3*5):
            print("FizzBuzz")
        else:
            print(x)
fizz_and_buzz()