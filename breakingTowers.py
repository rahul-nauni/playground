# return winner of game
def optimal_play(towers: list, turn: int) -> int:
    x = min(towers)
    y = 1
    while x % y == 0 and 1 <= y < x:
        towers[towers.index(x)] = y
        return 1 - turn
    y += 1


def towerBreakers(n, m) -> int:
    if m == 1 or n % 2 == 0:
        return 2
    return 1


# n: number of towers
# m: height of tower

n = 2
m = 6
print(towerBreakers(n, m))
