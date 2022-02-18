import pygame as pg

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

# def generate():

def make_map(product):
    # product = parsed_map
    # TODO: make map use new map coords set only on first load.
    level = load_map(0)   # temp 
    current_column = 0
    ratio = 10
    # product = []
    size = 0  # (height / width) * (ratio * 10)
    blockw = 0  # size
    blockh = 0  # blockw
    blockx = 0  # (width / len(column)) * current_block
    blocky = 0  # (height / len(column)) * current_column
    color = (255, 0, 0)# (100, 100, 100)
    for column in level:
    # print(column)
        current_block = 0
        for block in column:
        # print(block)
        # print(height/width)
            if block != 0:
                # size = (height / width) * (ratio * 10)
                size = 100
                blockw = size
                blockh = blockw
                blockx = (500 / len(column)) * current_block
                blocky = (500 / len(column)) * current_column
                color = (100, 100, 100)
            elif block == 0:
                size = 0  # (height / width) * (ratio * 10)
                blockw = 0  # size
                blockh = 0  # blockw
                blockx = 0  # (width / len(column)) * current_block
                blocky = 0  # (height / len(column)) * current_column
                color = (255, 0, 0)# (100, 100, 100)
                # pg.draw.rect(screen, color, [blockx, blocky, blockw, blockh])
            # print(blockx, blocky)
            current_block += 1
            product.append([[block, column], [blockx, blocky, blockw, blockh], [size, color]])
        # print(parsed_map)
        current_column += 1
    return product


parsed_map = []
def init_map():     # basically the exact same thing as init_map, but it returns the value
    global parsed_map
    make_map(parsed_map)
    print(parsed_map)

map_loaded = False
def load(screen):
    global map_loaded, current_sector, parsed_map
    if map_loaded == False:
        init_map()
        map_loaded = True
        # del self.map_loaded
    else:
        pass

    current_sector = 0
    for sector in parsed_map:
        if sector[0][0] != 0:   # Redundant
            # [[block, column], [blockx, blocky, blockw, blockh], [size, color]]
            pg.draw.rect(screen, sector[2][1], sector[1])
        current_sector += 1
