def level1():
    l1 = [
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1],
        [0, 0, 1, 1, 1],
        [1, 0, 0, 0, 1]
    ]
    return l1

def level2():
    l2 = [
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0],
        [1, 0, 0, 0, 1]
    ]
    return l2

def load_map(m):
    maps = [level1(), level2()]
    return maps[m]