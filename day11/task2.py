input_file = open("input.txt")

def number_of_paths_to_node(node, end_node):
    global visited_nodes
    visited_nodes = {}
    return number_of_paths_to_node_r(node, end_node)

visited_nodes = {}
def number_of_paths_to_node_r(node, end_node):
    global visited_nodes
    next_nodes = device_outputs[node]
    s = 0
    for next_node in next_nodes:
        if next_node == end_node:
            visited_nodes[next_node] = 1
            return 1
        elif next_node not in device_outputs:
            continue
        elif next_node in visited_nodes:
            s += visited_nodes[next_node]
        else:
            x = number_of_paths_to_node_r(next_node, end_node)
            visited_nodes[next_node] = x
            s += x
    return s


device_outputs = {}

for line in input_file:
    segments = line.strip().split(":")
    source = segments[0]
    outputs = segments[1].strip().split()
    device_outputs[source] = tuple(outputs)

input_file.close()

paths1 = (number_of_paths_to_node("svr", "dac") *
          number_of_paths_to_node("dac", "fft") *
          number_of_paths_to_node("fft", "out"))

paths2 = (number_of_paths_to_node("svr", "fft") *
          number_of_paths_to_node("fft", "dac") *
          number_of_paths_to_node("dac", "out"))

print(paths1 + paths2)
