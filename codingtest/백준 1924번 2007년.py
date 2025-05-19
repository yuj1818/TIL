from datetime import datetime
x, y = map(int, input().split())
print(datetime(2007, x, y).strftime("%A")[:3].upper())