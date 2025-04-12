from datetime import datetime
today = datetime(*map(int, input().split()))
dday = datetime(*map(int, input().split()))
if today.year + 1000 < dday.year: print('gg')
elif today.year + 1000 == dday.year and (today.month, today.day) <= (dday.month, dday.day): print('gg')
else: print(f'D-{(dday - today).days}')