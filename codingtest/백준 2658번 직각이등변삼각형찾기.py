def isValid(dsy, dsx, dey, dex, sy, sx, ey, ex, si, ei):
    for i in range(si, ei):
        (csy, csx), (cey, cex) = points[i]
        if sy + dsy != csy or sx + dsx != csx or ey + dey != cey or ex + dex != cex: return False
        sy, sx, ey, ex = csy, csx, cey, cex
    else: corner.update([(sy + 1, sx + 1), (ey + 1, ex + 1)])
    return True

def main():
    global points, corner
    arr = [list(map(int, input())) for _ in range(10)]
    corner = set()
    points = []
    minX, minY, maxX, maxY = 10, 10, 0, 0
    for i in range(10):
        if sum(arr[i]) == 0: continue
        if minY < 10: pass
        else: minY = i
        maxY = i
        sy, sx, ey, ex = 0, 0, 0, 0
        for j in range(10):
            if arr[i][j]:
                sy, sx = i, j
                break
        for j in range(9, -1, -1):
            if arr[i][j]:
                ey, ex = i, j
                break
        for j in range(sx, ex + 1):
            if arr[i][j] == 0: return 0
        points.append([(sy, sx), (ey, ex)])
        minX = min(minX, sx)
        maxX = max(maxX, ex)

    w = maxX - minX
    h = maxY - minY
    if len(points) < 1: return 0
    if w == 0 or h == 0: return 0

    if w // h == 2:
        (sy, sx), (ey, ex) = points[0]
        corner.update([(sy + 1, sx + 1), (ey + 1, ex + 1)])
        if sx == ex:
            if not isValid(1, -1, 1, 1, sy, sx, ey, ex, 1, len(points)): return 0
        else:
            if not isValid(1, 1, 1, -1, sy, sx, ey, ex, 1, len(points)): return 0
        return corner
    elif h // w == 2:
        (sy, sx), (ey, ex) = points[0]
        corner.update([(sy + 1, sx + 1), (ey + 1, ex + 1)])
        if arr[minY][minX]:
            if not isValid(1, 0, 1, 1, sy, sx, ey, ex, 1, w + 1) or not isValid(1, 0, 1, -1, sy + w, minX, sy + w, maxX, w + 1, len(points)): return 0
            corner.remove((sy + w + 1, minX + 1))
        else:
            if not isValid(1, -1, 1, 0, sy, sx, ey, ex, 1, w + 1) or not isValid(1, 1, 1, 0, sy + w, minX, sy + w, maxX, w + 1, len(points)): return 0
            corner.remove((sy + w + 1, maxX + 1))
        return corner
    elif w == h:
        (sy, sx), (ey, ex) = points[0]
        corner.update([(sy + 1, sx + 1), (ey + 1, ex + 1)])
        if arr[minY][maxX] == 0:
            if not isValid(1, 0, 1, 1, sy, sx, ey, ex, 1, len(points)): return 0
        elif arr[minY][minX] == 0:
            if not isValid(1, -1, 1, 0, sy, sx, ey, ex, 1, len(points)): return 0
        elif arr[maxY][minX] == 0:
            if not isValid(1, 1, 1, 0, sy, sx, ey, ex, 1, len(points)): return 0
        else:
            if not isValid(1, 0, 1, -1, sy, sx, ey, ex, 1, len(points)): return 0
        return corner
    else: return 0

if __name__ == '__main__':
    ans = main()
    if ans == 0: print(0)
    elif len(ans) != 3: print(0)
    else: print('\n'.join([' '.join(map(str, x)) for x in sorted(ans)]))