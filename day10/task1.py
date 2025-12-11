input_file = open("input.txt")

def get_minimal_number_of_presses(machine):
    start = [0] * len(machine["lights"])
    visited = [tuple(start)]
    queue = [(tuple(start), 0)]
    while len(queue) > 0:
        current_state, presses = queue.pop(0)
        for button in machine["buttons"]:
            new_state = list(current_state)
            for light in button:
                if new_state[light] == 0:
                    new_state[light] = 1
                else:
                    new_state[light] = 0
            new_state = tuple(new_state)
            if new_state == machine["lights"]:
                return presses + 1
            if new_state not in visited:
                new_state_in_queue = False
                for current_state_x, presses_x in queue:
                    if current_state_x == new_state:
                        new_state_in_queue = True
                        break
                if not new_state_in_queue:
                    queue.append((new_state, presses + 1))
    return 0

machines = []

for line in input_file:
    segments = line.strip().split()
    machine = {}

    lights = tuple([0 if x == "." else 1 for x in segments[0][1:-1]])
    machine["lights"] = lights

    buttons = tuple([tuple([int(y) for y in x[1:-1].split(",")]) for x in segments[1:-1]])
    machine["buttons"] = buttons

    joltage = tuple([int(x) for x in segments[-1][1:-1].split(",")])
    machine["joltage"] = joltage

    machines.append(machine)

input_file.close()

s = 0
for i, machine in enumerate(machines):
    s += get_minimal_number_of_presses(machine)
print(s)
