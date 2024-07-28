def twfw():
    v = int(input())
    w = int(input())
    
    if w % 2 != 0 or w < 2:
        return 0
    
    for i in range(v + 1):
        if i + (v - i) == v and (i * 2 + (v - i) * 4 == w or i * 4 + (v - i) * 2 == w):
            print(f"TW = {i}, FW = {v - i}")
            return 0
    
    print("No solution found")
    return 0

twfw()

