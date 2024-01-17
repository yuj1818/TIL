n = int(input())
sq = n ** 0.5

def find():
    if sq.is_integer():
        return 1
    else:
        for i in range(1, int(sq) + 1):
            if ((n - i ** 2) ** 0.5).is_integer():
                return 2

        for i in range(1, int(sq) + 1):
            for j in range(1, int((n - i ** 2) ** 0.5) + 1):
                if ((n - i ** 2 - j ** 2) ** 0.5).is_integer():
                    return 3
    return 4

print(find())