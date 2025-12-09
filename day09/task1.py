input_file = open("input.txt")

def area_between_tiles(tile1, tile2):
    area = (abs(tile1[0] - tile2[0]) + 1) * (abs(tile1[1] - tile2[1]) + 1)
    return area

red_tiles = []

for line in input_file:
    red_tiles.append(tuple([int(x) for x in line.strip().split(",")]))

input_file.close()

max_area = 0
for i in range(len(red_tiles)):
    for j in range(i+1, len(red_tiles)):
        if area_between_tiles(red_tiles[i], red_tiles[j]) > max_area:
            max_area = area_between_tiles(red_tiles[i], red_tiles[j])

print(max_area)
