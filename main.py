with open('Whole mogus external perim only.txt') as f:
    lines = f.readlines()

# subtract 125 from X and 105 from Y

relevant_lines_list = []
layer_in_construction = []
body_in_construction = []
relevant_line = False
split_line = []
for line in lines:
    filtered_line = ("", "")
    if line == "G1 F8640\n":
        relevant_line = False
    elif line == "G1 F900\n":
        relevant_line = True
        layer_in_construction.append(body_in_construction)
        body_in_construction = []
    elif line == ";LAYER_CHANGE\n":
        relevant_lines_list.append(layer_in_construction)
        layer_in_construction = []
    if relevant_line:
        split_line = line.split(" ")
        for i in range(len(split_line)):
            if split_line[i][0] == "X" and split_line[i + 1][0] == "Y":
                body_in_construction.append(((float(split_line[i][1:]))-125,(float(split_line[i+1][1:]))-105))



layer_in_construction.append(body_in_construction)
relevant_lines_list.append(layer_in_construction)

print(len(relevant_lines_list))

for a in relevant_lines_list:
    print("\nlayer change\n")
    for b in a:
        print("\nbody change\n")
        for c in b:
            print(c)

