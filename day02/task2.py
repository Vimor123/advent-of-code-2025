input_file = open("input.txt")

id_ranges = []

for line in input_file:
    id_ranges.extend([tuple(x.split("-")) for x in line.strip().split(",")])

input_file.close()

s = 0

for id_range in id_ranges:
    numbers = []
    for sequences in range(2, (len(id_range[1])) + 1):
        start = ''
        if len(id_range[0]) % sequences == 0:
            start = id_range[0][0:(len(id_range[0]) // sequences)]
        else:
            start = '1' + '0' * (len(id_range[0]) // sequences)
        finished = False
        while not finished:
            number = int(start * sequences)
            if number > int(id_range[1]):
                finished = True
                break
            if number >= int(id_range[0]):
                if number not in numbers:
                    s += number
                    numbers.append(number)
            start = str(int(start) + 1)

print(s)
