from scipy.optimize import linprog
import pulp as pl

input_file = open("input.txt")

def get_minimal_number_of_presses(machine):
    problem = pl.LpProblem("minimal_number_of_presses", pl.LpMinimize)

    variables = []
    for i in range(len(machine["buttons"])):
        var_name = "x" + str(i + 1)
        variables.append(pl.LpVariable(var_name, 0, None, pl.LpInteger))

    problem += pl.lpSum(variables[i] for i in range(len(machine["buttons"])))
    for i in range(len(machine["lights"])):
        a = []
        for button in machine["buttons"]:
            if i in button:
                a.append(1)
            else:
                a.append(0)
        problem += pl.lpSum(variables[i] * a[i] for i in range(len(machine["buttons"]))) == machine["joltage"][i]
    problem.solve(pl.PULP_CBC_CMD(msg = 0))

    return int(problem.objective.value())


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
