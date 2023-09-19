from collections import deque

T = int(input())

def merge_sort(m_list):
    if len(m_list) == 1:
        return m_list
    left = []
    right = []
    mid = len(m_list) // 2
    for el in m_list[:mid]:
        left.append(el)
    for el in m_list[mid:]:
        right.append(el)
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    global cnt
    result = []
    left = deque(left)
    right = deque(right)
    if left and right and left[-1] > right[-1]:
        cnt += 1
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.popleft())
            else:
                result.append(right.popleft())
        elif len(left) > 0:
            result.append(left.popleft())
        elif len(right) > 0:
            result.append(right.popleft())
    return result


for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    nums = merge_sort(nums)
    ans = nums[N // 2]
    print(f'#{tc} {ans} {cnt}')