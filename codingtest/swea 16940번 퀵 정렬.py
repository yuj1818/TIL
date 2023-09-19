T = int(input())

def quick_sort(left, right):
    if left >= right:
        return
    p = partition(left, right)
    quick_sort(left, p - 1)
    quick_sort(p + 1, right)

def partition(left, right):
    p = nums[left]
    i = left
    j = right

    while i <= j:
        while i <= j and nums[i] <= p:
            i += 1
        while i <= j and nums[j] >= p:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[left], nums[j] = nums[j], nums[left]
    return j

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    quick_sort(0, N - 1)
    ans = nums[N // 2]
    print(f'#{tc} {ans}')