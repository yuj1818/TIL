for i in range(3):
    s = input()
    if s.isdigit():
        result = int(s) + (3 - i)
        if result % 15 == 0:
            print('FizzBuzz')
        elif result % 3 == 0:
            print('Fizz')
        elif result % 5 == 0:
            print('Buzz')
        else:
            print(result)
        break