def solution(arr):
    zero, one = 0, 0
    
    def search(x, y, d):
        nonlocal zero, one
        n = arr[y][x]
        
        for i in range(y, y + d):
            for j in range(x, x + d):
                if arr[i][j] != n:
                    hf = d // 2
                    search(x, y, hf)
                    search(x + hf, y, hf)
                    search(x, y + hf, hf)
                    search(x + hf, y + hf, hf)
                    return
        if n:
            one += 1
        else:
            zero += 1
            
    search(0, 0, len(arr))
    
    return [zero, one]