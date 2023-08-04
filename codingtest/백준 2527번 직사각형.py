for _ in range(4):
    points = list(map(int, input().split()))
    x = []
    y = []
    for i in range(len(points)):
        if i % 2 == 0:
            x.append(points[i])
        else:
            y.append(points[i])

    if x[0] > x[2]:
        x3, x4, x1, x2 = x
    else:
        x1, x2, x3, x4 = x

    if y[0] > y[2]:
        y3, y4, y1, y2 = y
    else:
        y1, y2, y3, y4 = y

    if x2 > x3 and y2 > y3:
        print('a')
    elif x2 == x3 and y2 == y3:
        print('c')
    elif (x2 == x3 and y2 > y3) or (y2 == y3 and x2 > x3):
        print('b')
    else:
        print('d')