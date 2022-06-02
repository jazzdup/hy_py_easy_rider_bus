for i in range(1, 101):
    ans = i
    if i % 3 == 0:
        ans = "Fizz"
    if i % 5 == 0:
        ans = "Buzz"
    if i % 3 == 0 and i % 5 == 0:
        ans = "FizzBuzz"
    print(f"{ans}")
