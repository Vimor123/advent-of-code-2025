input_file = open("input.txt")

def no_of_touching_rolls(grid, row, column):
    rolls = 0
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                  (1, 0), (1, -1), (0, -1), (-1, -1)]
    for direction in directions:
        if row + direction[0] in range(len(grid)) and column + direction[1] in range(len(grid[0])):
            if grid[row + direction[0]][column + direction[1]] == "@":
                rolls += 1
    return rolls


grid =[]

for line in input_file:
    grid.append(list(line.strip()))

input_file.close()

total = 0
rolls_can_be_moved = True
while rolls_can_be_moved:
    moves = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                if no_of_touching_rolls(grid, i, j) < 4:
                    total += 1
                    moves.append((i, j))
    for move in moves:
        grid[move[0]][move[1]] = "."
    if len(moves) == 0:
        rolls_can_be_moved = False

print(total)
