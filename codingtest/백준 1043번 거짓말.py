# 인접 행렬 사용
# N, M = map(int, input().split())
# tn, *tp = map(int, input().split())
#
# if tn == 0:
#     print(M)
# else:
#     T = [0] * (N + 1)
#     for p in tp:
#         T[p] = 1
#     connection = [[0] * (N + 1) for _ in range(N + 1)]
#     parties = []
#
#     def connect(s):
#         for node in range(1, N + 1):
#             if node != s and not known[node] and connection[s][node]:
#                 known[node] = 1
#                 connect(node)
#         return
#
#     for _ in range(M):
#         pn, *pp = map(int, input().split())
#         parties.append(pp)
#         if pn > 1:
#             for i in pp:
#                 for j in pp:
#                     if i != j:
#                         connection[i][j] = 1
#                         connection[j][i] = 1
#
#     known = [*T]
#
#     for people in tp:
#         connect(people)
#
#     ans = M
#
#     for party in parties:
#         for guest in party:
#             if known[guest]:
#                 ans -= 1
#                 break
#
#     print(ans)

# union find 사용
N, M = map(int, input().split())
tn, *tp = map(int, input().split())

tp = set(tp)
parties = []

for _ in range(M):
    pn, *pp = map(int, input().split())
    parties.append(set(pp))

for _ in range(M):
    for guests in parties:
        if guests & tp:
            tp = tp.union(guests)

ans = M
for guests in parties:
    if guests & tp:
        ans -= 1

print(ans)