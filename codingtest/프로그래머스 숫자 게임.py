import heapq

def solution(A, B):
    A.sort(reverse=True)
    heap = []
    for b in B:
        if b > A[-1]:
            heapq.heappush(heap, -b)
    
    ans = 0
    
    for a in A:
        if heap:
            b = heapq.heappop(heap)
            if -b > a:
                ans += 1
            else:
                heapq.heappush(heap, b)
            
    return ans