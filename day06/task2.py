input_file = open("input.txt")

problem_matrix_chars = []

for line in input_file:
    problem_matrix_chars.append(list(line[:-1]))

input_file.close()

total = 0
numbers = []
for column in range(len(problem_matrix_chars[0])-1, -1, -1):
    number_string = ""
    for row in range(len(problem_matrix_chars)):
        if problem_matrix_chars[row][column].isdigit():
            number_string += problem_matrix_chars[row][column]
    if number_string != "":
        numbers.append(int(number_string))
    if problem_matrix_chars[-1][column] == "*":
        s = 1
        for number in numbers:
            s *= number
        total += s
        numbers = []
    elif problem_matrix_chars[-1][column] == "+":
        s = 0
        for number in numbers:
            s += number
        total += s
        numbers = []

print(total)
