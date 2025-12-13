input_file = open("input.txt")

def number_of_paths_to_out(node):
    next_nodes = device_outputs[node]
    s = 0
    for next_node in next_nodes:
        if next_node == "out":
            return 1
        else:
            s += number_of_paths_to_out(next_node)
    return s


device_outputs = {}

for line in input_file:
    segments = line.strip().split(":")
    source = segments[0]
    outputs = segments[1].strip().split()
    device_outputs[source] = tuple(outputs)

input_file.close()

print(number_of_paths_to_out("you"))
