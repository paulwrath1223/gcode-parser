with open('Whole mogus external perim only.txt') as f:
    lines = f.readlines()

# subtract 125 from X and 105 from Y

relevant_lines_list = []
relevant_line = False
split_line = []
for line in lines:
    filtered_line = ("", "")
    if line == "G1 F8640\n":
        relevant_line = False
    elif line == "G1 F900\n":
        relevant_line = True
        relevant_lines_list.append("change body")
    if relevant_line:
        split_line = line.split(" ")
        for i in range(len(split_line)):
            if split_line[i][0] == "X" and split_line[i + 1][0] == "Y":
                relevant_lines_list.append(((split_line[i][1:]),(split_line[i+1][1:])))
    else:
        if line == ";LAYER_CHANGE\n":
            relevant_lines_list.append("Layer Change")

print (relevant_lines_list)
