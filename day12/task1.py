input_file = open("input.txt")

shapes = []
regions = []

reading_phase = "shapes"

current_shape = []
current_row = 0

for line in input_file:
    if reading_phase == "shapes":
        if "x" in line:
            reading_phase = "regions"
        elif line.strip() == "":
            shapes.append(tuple(current_shape))
            current_shape = []
            current_row = 0
        elif line[0].isnumeric():
            pass
        else:
            for index, character in enumerate(list(line.strip())):
                if character == "#":
                    current_shape.append((current_row, index))
            current_row += 1

    if reading_phase == "regions":
        segments = line.strip().split(":")
        size = tuple([int(x) for x in segments[0].split("x")])
        presents = tuple([int(x) for x in segments[1].strip().split()])

        regions.append({ "size" : size,
                         "presents" : presents })

input_file.close()

s = 0
for region in regions:
    total_area = region["size"][0] * region["size"][1]
    presents_area = 0
    for present_index, no_of_presents_per_shape in enumerate(region["presents"]):
        presents_area += no_of_presents_per_shape * len(shapes[present_index])

    if total_area >= presents_area:
        s += 1
print(s)
