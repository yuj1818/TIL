import sys
for s in sys.stdin.readlines():
    err = []
    s = s.rstrip()
    arr = s.split()
    l = len(arr)
    for i in range(l):
        if arr[i] == 'dip':
            if (i > 0 and arr[i - 1] == 'jiggle') or (i > 1 and arr[i - 2] == 'jiggle') or (i + 1 < l and arr[i + 1] == 'twirl'): continue
            arr[i] = 'DIP'
            if not err: err.append('1')
    if not s.endswith('clap stomp clap'): err.append('2')
    if s.find('twirl') >= 0 > s.find('hop'): err.append('3')
    if s.startswith('jiggle'): err.append('4')
    if s.find('dip') < 0: err.append('5')
    out = ' '.join(arr)
    if not err: print('form ok:', s)
    elif len(err) == 1: print(f"form error {err[0]}: {out}")
    else: print(f"form errors {', '.join(err[:-1])} and {err[-1]}: {out}")