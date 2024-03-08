from collections import deque

tc = int(input())

for i in range(tc):
  s = input()
  l = deque()
  r = deque()
  for c in s:
    if c == '-':
      if l:
        l.pop()
    elif c == '<':
      if l:
        r.appendleft(l.pop())
    elif c == '>':
      if r:
        l.append(r.popleft())
    else:
      l.append(c)
  print(''.join(l+r))
