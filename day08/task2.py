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

min_distances = {}

for i in range(len(junctions)):
    min_distances[tuple([i])] = {}

for i in range(len(junctions)):
    for j in range(i + 1, len(junctions)):
        min_distances[tuple([i])][tuple([j])] = distance(junctions[i], junctions[j])
        min_distances[tuple([j])][tuple([i])] = distance(junctions[i], junctions[j])

last_min_distance = 0

while len(min_distances) > 1:
    print(len(min_distances))
    min_min_distance = -1
    min_pair = tuple()
    for circuit1, min_distances_for_circuit in min_distances.items():
        for circuit2, min_distance in min_distances_for_circuit.items():
            if min_distance < min_min_distance or min_min_distance < 0:
                min_min_distance = min_distance
                min_pair = (circuit1, circuit2)
    new_circuit = []
    for junction in min_pair[0]:
        new_circuit.append(junction)
    for junction in min_pair[1]:
        new_circuit.append(junction)
    new_circuit = tuple(new_circuit)
    new_circuit_distances = {}
    min_distances.pop(min_pair[0])
    min_distances.pop(min_pair[1])
    for circuit, min_distances_for_circuit in min_distances.items():
        min_distance_to_new_circuit = min(min_distances_for_circuit[min_pair[0]],
                                          min_distances_for_circuit[min_pair[1]])
        min_distances_for_circuit[new_circuit] = min_distance_to_new_circuit
        min_distances_for_circuit.pop(min_pair[0])
        min_distances_for_circuit.pop(min_pair[1])
        new_circuit_distances[circuit] = min_distance_to_new_circuit
        last_min_distance = min_distance_to_new_circuit
    min_distances[new_circuit] = new_circuit_distances

print("")
for i in range(len(junctions)):
    for j in range(i + 1, len(junctions)):
        if distance(junctions[i], junctions[j]) == last_min_distance:
            print(junctions[i][0] * junctions[j][0])
