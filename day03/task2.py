input_file = open("input.txt")

def largest_joltage(bank_string):
    bank = [int(x) for x in bank_string]
    start_index = 0
    digit = max(bank[start_index:-11])
    number = str(digit)
    for i in range(11):
        start_index = bank[start_index:].index(digit) + start_index + 1
        end_index = len(bank) - (10 - i)
        digit = max(bank[start_index:end_index])
        number += str(digit)

    return int(number)

s = 0

for line in input_file:
    s += largest_joltage(line.strip())

input_file.close()

print(s)
