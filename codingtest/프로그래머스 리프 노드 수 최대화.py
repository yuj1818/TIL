def solution(dist_limit, split_limit):
    ans = 1

    def count(cnt2, cnt3):
        leaf = 1
        r_split = dist_limit
        for _ in range(cnt2):
            if r_split >= leaf:
                r_split -= leaf
                leaf *= 2
            else: return leaf + r_split
        for _ in range(cnt3):
            if r_split >= leaf:
                r_split -= leaf
                leaf *= 3
            else: return leaf + r_split * 2
        return leaf

    cnt2 = 0
    while 1:
        cnt3 = 0
        while 1:
            if (2 ** cnt2) * (3 ** cnt3) > split_limit: break
            leaves = count(cnt2, cnt3)
            if ans < leaves: ans = leaves
            cnt3 += 1
        cnt2 += 1
        if 2 ** cnt2 > split_limit: break

    return ans
