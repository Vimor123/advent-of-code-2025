input_file = open("input.txt")

def area_between_tiles(tile1, tile2):
    area = (abs(tile1[0] - tile2[0]) + 1) * (abs(tile1[1] - tile2[1]) + 1)
    return area

def is_edge_in_rectangle(tile1, tile2, edges):
    edges_rectangle_rows = (min(tile1[0], tile2[0]), max(tile1[0], tile2[0]))
    edges_rectangle_cols = (min(tile1[1], tile2[1]), max(tile1[1], tile2[1]))

    for edge in edges:
        if edge[0] == "h":
            if edge[1] > edges_rectangle_rows[0] and edge[1] < edges_rectangle_rows[1]:
                for i in range(edge[2][0], edge[2][1] + 1):
                    if i > edges_rectangle_cols[0] and i < edges_rectangle_cols[1]:
                        return True
        else:
            if edge[1] > edges_rectangle_cols[0] and edge[1] < edges_rectangle_cols[1]:
                for i in range(edge[2][0], edge[2][1] + 1):
                    if i > edges_rectangle_rows[0] and i < edges_rectangle_rows[1]:
                        return True

    return False


red_tiles = []
edges = []

for line in input_file:
    red_tiles.append(tuple([int(x) for x in line.strip().split(",")]))

input_file.close()

for i in range(len(red_tiles)):
    tile1 = red_tiles[i]
    tile2 = red_tiles[(i+1)%len(red_tiles)]
    if tile1[0] == tile2[0]:
        edges.append(("h", tile1[0], (min(tile1[1], tile2[1]), max(tile1[1], tile2[1]))))
    else:
        edges.append(("v", tile1[1], (min(tile1[0], tile2[0]), max(tile1[0], tile2[0]))))

max_area = 0
for i in range(len(red_tiles)):
    for j in range(i+1, len(red_tiles)):
        tile1 = red_tiles[i]
        tile2 = red_tiles[j]
        if not is_edge_in_rectangle(tile1, tile2, edges):
            if area_between_tiles(tile1, tile2) > max_area:
                max_area = area_between_tiles(tile1, tile2)

print(max_area)
