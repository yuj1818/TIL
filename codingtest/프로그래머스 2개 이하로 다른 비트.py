def solution(numbers):
    ans = []
    for number in numbers:
        number = list(bin(number))
        for i in range(len(number) - 1, 1, -1):
            if number[i] == '0':
                number[i] = '1'
                break
        else:
            number.insert(2, '1')

        if i < len(number) - 1:
            number[i + 1] = '0'
                
        ans.append(int(''.join(number), 2))
        
    return ans