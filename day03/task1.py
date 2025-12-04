input_file = open("input.txt")

def largest_joltage(bank_string):
    bank = [int(x) for x in bank_string]
    digit1 = max(bank[:-1])
    digit2 = max(bank[bank.index(digit1)+1:])
    return int(str(digit1) + str(digit2))

s = 0

for line in input_file:
    s += largest_joltage(line.strip())

input_file.close()

print(s)
