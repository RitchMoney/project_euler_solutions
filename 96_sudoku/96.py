line_list = []
txt_file = open("p096_sudoku.txt", "r")

# open and add each line into line_list
for line in txt_file:
    cleaned = line.strip()
    line_list.append(cleaned)

txt_file.close()

count = 0
line_count = 0
grid_dict = {}

# parse into lists of lines in dictionary by id number
for line in line_list:
    if "Grid" in line:
        count += 1

        grid_dict[count] = []
    else:
        for char in line:
            grid_dict[count][line_count] = []
            grid_dict[count][line_count].append(char)
            line_count += 1

        line_count = 0

