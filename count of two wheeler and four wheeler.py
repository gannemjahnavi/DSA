def twfw():
    v = int(input("Enter the total number of vehicles: "))
    w = int(input("Enter the total number of wheels: "))
    
    if w % 2 != 0 or w < 2:
        return 0
    
    for tw in range(v + 1):
        fw = v - tw
        if (2 * tw + 4 * fw) == w:
            print(f"TW = {tw}, FW = {fw}")
            return 0
    
    print("No solution found")
    return 0

twfw()
