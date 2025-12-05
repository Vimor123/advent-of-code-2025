input_file = open("input.txt")

def put_new_range(id_ranges, new_id_range):
    new_id_ranges = []
    new_range_start = new_id_range[0]
    new_range_end = new_id_range[1]
    range_put = False
    for i in range(len(id_ranges)):
        if range_put:
            new_id_ranges.append(id_ranges[i])
            continue

        next_old_range_start = id_ranges[i][0]
        next_old_range_end = id_ranges[i][1]

        if new_range_start <= next_old_range_start:
            if new_range_end <= next_old_range_start:
                new_id_ranges.append((new_range_start, new_range_end))
                range_put = True
                new_id_ranges.append(id_ranges[i])
            else:
                if new_range_end <= next_old_range_end:
                    new_id_ranges.append((new_range_start, next_old_range_end))
                    range_put = True
                else:
                    new_id_ranges.append((new_range_start, next_old_range_end))
                    new_range_start = next_old_range_end
        else:
            if new_range_start <= next_old_range_end:
                if new_range_end <= next_old_range_end:
                    new_id_ranges.append(id_ranges[i])
                    range_put = True
                else:
                    new_id_ranges.append((next_old_range_start, next_old_range_end))
                    new_range_start = next_old_range_end
            else:
                new_id_ranges.append(id_ranges[i])

    if not range_put:
        new_id_ranges.append((new_range_start, new_range_end))

    new_new_id_ranges = []
    helper = (0, 0)
    helper_active = False
    for i in range(len(new_id_ranges)):
        if i == len(new_id_ranges) - 1:
            if helper_active:
                new_new_id_ranges.append(helper)
            else:
                new_new_id_ranges.append(new_id_ranges[i])
        else:
            if new_id_ranges[i+1][0] - new_id_ranges[i][1] <= 1:
                if not helper_active:
                    helper = (new_id_ranges[i][0], new_id_ranges[i+1][1])
                    helper_active = True
                else:
                    helper = (helper[0], new_id_ranges[i+1][1])
            else:
                if helper_active:
                    new_new_id_ranges.append(helper)
                    helper_active = False
                else:
                    new_new_id_ranges.append(new_id_ranges[i])

    return new_new_id_ranges


valid_ids = []
phase = "valid"
for line in input_file:
    if (line.strip() == ""):
        phase = "ingredients"
    elif phase == "valid":
        new_valid_id_range = tuple([int(x) for x in line.strip().split("-")])
        valid_ids = put_new_range(valid_ids, new_valid_id_range)

input_file.close()

total = 0
for id_range in valid_ids:
    total += id_range[1] - id_range[0] + 1

print(total)
