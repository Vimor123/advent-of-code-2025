input_file = open("input.txt")

dial = 50
counter = 0

for line in input_file:
    value = int(line.strip()[1:])
    if line[0] == "L":
        value *= -1
    dial = (dial + value) % 100
    if dial == 0:
        counter += 1

input_file.close()

print(counter)
