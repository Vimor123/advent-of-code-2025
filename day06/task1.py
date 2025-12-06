input_file = open("input.txt")

problem_matrix = []

for line in input_file:
    problem_matrix.append([x.strip() for x in line.strip().split()])

input_file.close()

total = 0
for column in range(len(problem_matrix[0])):
    s = 0
    if problem_matrix[-1][column] == '*':
        s = 1
        for row in range(len(problem_matrix) - 1):
            s *= int(problem_matrix[row][column])
    else:
        s = 0
        for row in range(len(problem_matrix) - 1):
            s += int(problem_matrix[row][column])
    total += s

print(total)
