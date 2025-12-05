input_file = open("input.txt")

valid_ids = []
ingredients = []
phase = "valid"
for line in input_file:
    if (line.strip() == ""):
        phase = "ingredients"
    elif phase == "valid":
        valid_ids.append(tuple([int(x) for x in line.strip().split("-")]))
    else:
        ingredients.append(int(line.strip()))

input_file.close()

fresh = 0

for ingredient in ingredients:
    valid = False
    for valid_id_range in valid_ids:
        if ingredient >= valid_id_range[0] and ingredient <= valid_id_range[1]:
            valid = True
            break
    if valid:
        fresh += 1

print(fresh)
