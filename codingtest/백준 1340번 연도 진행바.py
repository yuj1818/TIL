month = ["January" , "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
M, D, Y, T = input().split(' ')
M = month.index(M)
D = int(D.rstrip(','))
Y = int(Y)
h, m = map(int, T.split(':'))
days = [31, 29 if Y % 400 == 0 or (Y % 4 == 0 and Y % 100 != 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(((sum(days[:M]) + D - 1) * 24 * 60 + h * 60 + m) / (sum(days) * 24 * 60) * 100)