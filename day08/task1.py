import math

input_file = open("input.txt")

def distance(junction1, junction2):
    distance = (junction1[0] - junction2[0]) ** 2
    distance += (junction1[1] - junction2[1]) ** 2
    distance += (junction1[2] - junction2[2]) ** 2
    return math.sqrt(distance)

junctions = []
for line in input_file:
    junctions.append(tuple([int(x) for x in line.strip().split(",")]))

input_file.close()


min_pairs = []

print("Part 1:")
iterations = 1000
for iteration in range(iterations):
    min_distance = -1
    min_pair = (0, 0)
    for i in range(len(junctions)):
        for j in range(i + 1, len(junctions)):
            x = distance(junctions[i], junctions[j])
            if (x < min_distance or min_distance < 0) and (i, j) not in min_pairs:
                min_distance = x
                min_pair = (i, j)
    min_pairs.append(min_pair)
    print("{:6.2f}%".format((iteration + 1)/iterations * 100))

print("Part 2:")
circuits = []
for iteration, min_pair in enumerate(min_pairs):
    new_circuits = []
    circuit1 = [min_pair[0]]
    circuit2 = [min_pair[1]]
    in_same_circuit = False
    for circuit in circuits:
        if min_pair[0] in circuit and min_pair[1] in circuit:
            new_circuits.append(circuit)
            in_same_circuit = True
        elif min_pair[0] in circuit:
            circuit1 = circuit
        elif min_pair[1] in circuit:
            circuit2 = circuit
        else:
            new_circuits.append(circuit)
    if not in_same_circuit:
        new_circuit = []
        for junction in circuit1:
            new_circuit.append(junction)
        for junction in circuit2:
            new_circuit.append(junction)
        new_circuit.sort()
        new_circuits.append(new_circuit)
    circuits = new_circuits
    print("{:6.2f}%".format((iteration + 1)/len(min_pairs) * 100))

lengths = []
for circuit in circuits:
    lengths.append(len(circuit))

lengths.sort()

print("")
print(lengths[-1] * lengths[-2] * lengths[-3])
