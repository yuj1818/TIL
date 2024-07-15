def accumulate(order):
    idx = 0
    box = [i for i in range(len(order), 0, -1)]
    extra = []
    acc = []
    while idx < len(order):
        if extra and extra[-1] == order[idx]:
            acc.append(extra.pop())
        else:
            while box and box[-1] != order[idx]:
                extra.append(box.pop())
            if box:
                acc.append(box.pop())
            else:
                return len(acc)
        idx += 1
    return len(acc)

def solution(order):
    return accumulate(order)