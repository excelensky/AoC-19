#import input, strip commas and split lines
input_file = open(r"AoC_3\input_day3.txt", "r")
input_data = input_file.read()
wire_one = (input_data.splitlines()[0]).split(",")
wire_two = (input_data.splitlines()[1]).split(",")

wire_one, wire_two = input_data.splitlines()
wire_one = wire_one.split(",")
wire_two = wire_two.split(",")

def pathfinder(wire):
    x_value = 0
    y_value = 0
    path = [[x_value, y_value]]
    i = 0
    for 
    while i <= (len(wire)-1):
        if wire[i][0] == "R":
            x_value = x_value + int(wire[i][1:])
            print("R")
            print(i)
        elif wire[i][0] == "L":
            x_value = x_value - int(wire[i][1:])
            print("L")
            print(i)
        elif wire[i][0] == "U":
            y_value = y_value + int(wire[i][1:])
            print("U")
            print(i)
        elif wire[i][0] == "D":
            y_value = y_value - int(wire[i][1:])
            print("D")
            print(i)
        else:
            print("error")
        path.append([x_value, y_value])
        i += 1
    print (path)
    return path

#Test Data
wire = ["R75","D30","R83","U83","L12","D49","R71","U7","L72"]
wire_2 = ["U62","R66","U55","R34","D71","R55","D58","R83"]
distance_wire_1_wire_2 = 159



def stepfinder(path):
    i = 0
    x_lines = []
    y_lines = []
    while i < len(path):
        x_lines.append([path[i][0] + path[i+1][0],path[i][1]])
        y_lines.append([path[i][1],[path[i][1] + path[i+1][1]]])
    return x_lines
    return y_lines    


# listen vs. sets --> duplikate erkennen etc. mengenlehre (intersect)
# extend statt append: extend packt range als elemente in liste, append nicht
def stepfinder_pro(wire):
    x_value = 0
    y_value = 0
    steps = []
    i = 0
    for step in wire:
        direction = step[0]
        num_steps = int(step[1:])
        if direction == "R":
            ...
    while i < len(wire):
        if wire[i][0] == "R":
            steps.append([range(x_value, x_value + int(wire[i][1:]) + 1,1),[y_value]])
            x_value = x_value + int(wire[i][1:])
        elif wire[i][0] == "L":
            steps.append([range(x_value, x_value - int(wire[i][1:]) - 1,1),[y_value]])
            x_value = x_value - int(wire[i][1:])
        elif wire[i][0] == "U":
            steps.extend(itertools.product([x_value], range(y_value, y_value + int(wire[i][1:]) + 1)])
            y_value = y_value + int(wire[i][1:])
        elif wire[i][0] == "D":
            steps.append([[x_value], range(y_value, y_value - int(wire[i][1:]) - 1,1)])
            y_value = y_value - int(wire[i][1:])
        else:
            print("error")
        i += 1
    
    print(f"steps: {steps}")
    return steps


steps_wire_1 = stepfinder_pro(wire)
steps_wire_2 = stepfinder_pro(wire_2)

def wire_compare(steps_wire_1, steps_wire_2):
    i = 0
    j = 0
    crosses = []
    while i < len(wire_1):
        while j < len(wire_2):
            if steps_wire_1[i][0] in steps_wire_2[j][0] and steps_wire_1[i][1] in steps_wire_2[j][0]:
                crosses.append(object)
                


