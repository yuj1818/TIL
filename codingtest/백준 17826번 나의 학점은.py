scores = list(map(int, input().split()))
hong = int(input())
grades = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'F']
th = [scores[x] for x in [4, 14, 29, 34, 44, 47, -1]]
for i, t in enumerate(th):
    if hong >= t:
        print(grades[i])
        break