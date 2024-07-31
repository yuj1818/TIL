def solution(numbers):
    numbers = map(str, numbers)
    return str(int(''.join(sorted(numbers, reverse=True, key= lambda x: x*3))))