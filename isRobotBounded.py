from typing import List
def isRobotBounded(commands: str):
    if "L" not in commands and "R" not in commands:
        return False
    if "G" not in commands:
        return True
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    x, y = 0, 0
    idx = 0 # idx 0 = north, idx 1 = east, idx 2 = south, idx 3 = west
    for c in commands:
        if c == "G":
            x += directions[idx][0]
            y += directions[idx][1]
        elif c == "L":
            idx = (idx + 3) % 4
        else:
            idx = (idx + 1) % 4
        
    return True if ((x == 0 and y == 0) or idx != 0) else False

def run_commands(commands: List[str]):
    for i in range(n):
        if isRobotBounded(commands[i]):
            print("YES")
        else:
            print("NO")

n = 3
c1 = "G"
c2 = "L"
c3 = "RGRG"
#isRobotBounded(c3)
run_commands([c1, c2, c3])