input_file = open("input.txt")

id_ranges = []

for line in input_file:
    id_ranges.extend([tuple(x.split("-")) for x in line.strip().split(",")])

input_file.close()

s = 0

for id_range in id_ranges:
    start = ''
    if len(id_range[0]) % 2 == 0:
        start = id_range[0][0:(len(id_range[0]) // 2)]
    else:
        start = ('1' + '0' * (len(id_range[0]) // 2))
    finished = False
    while not finished:
        number = start * 2
        number = int(number)
        if number > int(id_range[1]):
            finished = True
            break
        if number >= int(id_range[0]):
            s += number
        start = str(int(start) + 1)

print(s)
