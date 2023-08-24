T = int(input())
codes = {
    '211': 0,
    '221': 1,
    '122': 2,
    '411': 3,
    '132': 4,
    '231': 5,
    '114': 6,
    '312': 7,
    '213': 8,
    '112': 9
}

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    b_codes = list(set([('0'+format(int(input(), 16), 'b')).rstrip('0') for _ in range(N)]))
    b_codes.pop(0)
    converted_codes = []
    ans = 0
    for b_code in b_codes:
        converted = []
        counts = [0, 0, 0]
        for i in range(len(b_code) - 1, -1, -1):
            if b_code[i] == '1' and not counts[1]:
                counts[2] += 1
            elif b_code[i] == '0' and not counts[0] and counts[2]:
                counts[1] += 1
            elif b_code[i] == '1' and counts[1]:
                counts[0] += 1
            else:
                if sum(counts) > 0:
                    converted.append(codes[''.join(map(str, [count//min(counts) for count in counts]))])
                    counts = [0, 0, 0]
                if len(converted) == 8:
                    converted_codes.append(tuple(converted[::-1]))
                    converted = []
    converted_codes = set(converted_codes)
    for converted_code in converted_codes:
        even = [converted_code[i] for i in range(1, 7, 2)]
        odd = [converted_code[i] for i in range(0, 7, 2)]
        if not (sum(odd) * 3 + sum(even) + converted_code[-1]) % 10:
            ans += sum(converted_code)
    print(f'#{tc} {ans}')