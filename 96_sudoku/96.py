from typing import List

class Sudoku:
    def __init__(self, number, raw_puzzle):
        self.number = number
        self.puzzle = self.get_puzzle(raw_puzzle)
        self.puzzle_readable = self.get_current_puzzle_readable()

    class Square:
        def __init__(self, x, y, num):
            self.x = x
            self.y = y
            self.boxx = int(x/3)
            self.boxy = int(y/3) 
            self.num = num
            self.candidates = self.get_candidates(num)
            self.solved = False
            if self.num != 0:
                self.solved = True

        def is_solved(self):
            if self.num != 0:
                return True
            else:
                number_of_candidates = 0
                for thing in self.candidates:
                    if thing:
                        number_of_candidates += 1
                if number_of_candidates == 1:
                    for i, cand_bool in enumerate(self.candidates):
                        if cand_bool:
                            self.num = i
                    return True
                else:
                    return False

        def get_candidates(self, number):
            if number == 0:
                return [False, True, True, True, True, True, True, True, True, True]
            else:
                return 

    def get_puzzle(self, raw):
        puzzle = []
        for i, row in enumerate(raw):
            puzzle.append([])
            for j, num in enumerate(row):
                Square = self.Square(j,i,num)
                puzzle[i].append(Square)
                

        return puzzle

    def eliminate_candidates(self, sq: Square):
        if sq.num == 0:
            # row
            for rowmate in self.puzzle[sq.y]:
                if rowmate.num != 0:
                    sq.candidates[rowmate.num] = False
                    sq.is_solved()
                    self.puzzle_readable = self.get_current_puzzle_readable()
                    if sq.num != 0:
                        self.puzzle_readable = self.get_current_puzzle_readable()
                        break
            # column
            for row in self.puzzle:
                if row[sq.x].num != 0:
                    sq.candidates[row[sq.x].num] = False
                    sq.is_solved()
                    self.puzzle_readable = self.get_current_puzzle_readable()
                    if sq.num != 0:
                        self.puzzle_readable = self.get_current_puzzle_readable()
                        break
            # square
            for x in range(sq.boxx * 3, (sq.boxx * 3) + 3):
                for y in range(sq.boxy * 3, (sq.boxy * 3) + 3):
                    if self.puzzle[y][x].num != 0:
                        sq.candidates[self.puzzle[y][x].num] = False
                        sq.is_solved()
                        self.puzzle_readable = self.get_current_puzzle_readable()
                        if sq.num != 0:
                            self.puzzle_readable = self.get_current_puzzle_readable()
                            break
                
    def solve(self):
        while not self.puzzle_solved():
            for row in self.puzzle:
                for x in row:
                    self.eliminate_candidates(x)

    def puzzle_solved(self):
        for row in self.puzzle:
            for x in row:
                if x.num == 0:
                    return False
                else:
                    return True
                
    def print_solved(self):
        rowcount = 0
        colcount = 0
        # if self.puzzle_solved():
        for row in self.puzzle_readable:
            rowcount += 1
            if rowcount % 3 == 1:
                print("- - - - - - - - -")
            for x in row:
                colcount += 1
                if colcount % 3 == 1:
                    print("|", end="")
                print(x, end=" ")
            print()
        print()
        print()

    def get_current_puzzle_readable(self):
        puz = []
        for i, row in enumerate(self.puzzle):
            puz.append([])
            for sqa in row:
                puz[i].append(sqa.num)

        return puz









line_list = []
txt_file = open("96_sudoku/p096_sudoku.txt", "r")

for line in txt_file:
    cleaned = line.strip()
    line_list.append(cleaned)

txt_file.close()

sudoku_number = 0
puzzle_raw = []
line_count = 0

for line in line_list:
    if "Grid 01" in line:
        sudoku_number += 1
        print("Grid ", sudoku_number)
        line_count = 0

    elif "Grid" in line:
        sudoku = Sudoku(sudoku_number, puzzle_raw)
        sudoku.solve()
        sudoku.print_solved()

        #do stuff here!

        # use the following line once itterating
        sudoku_number += 1
        print("Grid ", sudoku_number)
        puzzle_raw = []
        line_count = 0
    else:
        
        puzzle_raw.append([])
        for char in line:
            puzzle_raw[line_count].append(int(char))
        line_count += 1
    