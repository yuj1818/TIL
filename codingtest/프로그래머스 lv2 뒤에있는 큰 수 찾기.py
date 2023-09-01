def solution(numbers):
    result = [-1] * len(numbers)
    max_n = numbers[-1]
    for i in range(len(numbers) - 2, -1, -1):
        if numbers[i] >= max_n:
            max_n = numbers[i]
            continue
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                result[i] = numbers[j]
                break
            if numbers[i] == numbers[j]:
                result[i] = result[j]
                break
    return result

print(solution([2, 3, 3, 5]))

'''
테스트케이스
[2, 3, 3, 5] => [3, 5, 5, -1]
[9, 1, 5, 3, 6, 2]	=> [-1, 5, 6, 6, -1, -1]
'''