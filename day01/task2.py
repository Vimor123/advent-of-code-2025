input_file = open("input.txt")

dial = 50
counter = 0

for line in input_file:
    value = int(line.strip()[1:])
    if line[0] == "L":
        value *= -1
    
    dial = dial + value
    new_value_set = False
    while not new_value_set:
        if dial >= 0 and dial <= 99:
            new_value_set = True
            break
        if dial < 0:
            dial += 100
            counter += 1
        elif dial > 99:
            dial -= 100
            counter += 1

input_file.close()

print(counter)
