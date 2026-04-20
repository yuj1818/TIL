def trans(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

def solution(book_time):
    reservations = sorted([(trans(s), trans(e) + 10) for s, e in book_time])
    rooms = []
    for s, e in reservations:
        for i in range(len(rooms)):
            if rooms[i] <= s:
                rooms[i] = e
                break
        else: rooms.append(e)
        rooms.sort()
    return len(rooms)

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
# 3
