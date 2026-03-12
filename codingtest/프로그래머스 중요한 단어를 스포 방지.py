def solution(message, spoiler_ranges):
    words = []
    idx = 0
    for w in message.split():
        s = message.find(w, idx)
        e = s + len(w) - 1
        idx = e + 1
        words.append((w, s, e))
    spoiled = set()
    normal = set()
    for w, s, e in words:
        sig = 0
        for l, r in spoiler_ranges:
            if e >= l and s <= r:
                sig = 1
                break
        if sig:
            spoiled.add(w)
        else:
            normal.add(w)
    return len(spoiled - normal)
