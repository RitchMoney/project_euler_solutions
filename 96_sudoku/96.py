line_list = []
txt_file = open("96_sudoku/p096_sudoku.txt", "r")

# open and add each line into line_list
for line in txt_file:
    cleaned = line.strip()
    line_list.append(cleaned)

txt_file.close()

puzzle_number = 0
line_count = 0
grid_dict = {}

# parse into lists of lines in dictionary by id number
for line in line_list:
    if "Grid" in line:
        puzzle_number += 1

        grid_dict[puzzle_number] = []

        line_count = 0
    else:
        grid_dict[puzzle_number].append([])
        for char in line:
            grid_dict[puzzle_number][line_count].append(char)
        
        line_count += 1
    
for i in range(len(grid_dict[1])):
    print(grid_dict[1][i])