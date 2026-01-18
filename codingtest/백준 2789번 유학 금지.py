import re, sys
s = sys.stdin.readline().rstrip()
p = r"[CAMBRIDGE]"
print(re.sub(p, '', s, flags=re.IGNORECASE))