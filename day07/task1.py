input_file = open("input.txt")

start_column = 0
splitter_columns = []
for line in input_file:
    splitter_columns.append([])
    for index, char in enumerate(list(line)):
        if char == "S":
            start_column = index
        elif char == "^":
            splitter_columns[-1].append(index)

input_file.close()

split_count = 0

beams = [start_column]
for row in splitter_columns:
    new_beams = []
    for beam in beams:
        beam_split = False
        for splitter in row:
            if beam == splitter:
                beam_split = True
                split_count += 1
                if (beam - 1) not in new_beams:
                    new_beams.append(beam - 1)
                if (beam + 1) not in new_beams:
                    new_beams.append(beam + 1)
        if not beam_split:
            if beam not in new_beams:
                new_beams.append(beam)
    beams = new_beams

print(split_count)
