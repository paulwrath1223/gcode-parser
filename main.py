with open('Whole mogus external perim only.txt') as f:
    lines = f.readlines()


relevant_lines_list = []
relevant_line = False
for line in lines:
    filtered_line = ""
    if line == "G1 F8640":
        relevant_line = False
    elif line == "G1 F900":
        relevant_line = True
    if relevant_line:



        relevant_lines_list.append(line)


