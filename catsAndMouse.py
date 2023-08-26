from typing import List


def catchMouse(locations: List[int]):
    cat_a = locations[0]
    cat_b = locations[1]
    mouse = locations[2]

    if abs(cat_a - mouse) > abs(cat_b - mouse):
        print("CAT B")
    elif abs(cat_a - mouse) < abs(cat_b - mouse):
        print("CAT A")
    elif abs(cat_a - mouse) == abs(cat_b - mouse):
        print("MOUSE C")


inputs = [
    [1, 2, 3],
    [1, 3, 2]
]

if __name__ == "__main__":
    for locations in inputs:
        catchMouse(locations)
