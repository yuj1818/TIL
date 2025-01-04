def star(n):
    if n == 3: return ['***', '* *', '***']
    pattern = star(n // 3)
    tb = [pattern[i] * 3 for i in range(n // 3)]
    return tb + [pattern[i] + ' ' * (n // 3) + pattern[i] for i in range(n // 3)] + tb

print('\n'.join(star(int(input()))))