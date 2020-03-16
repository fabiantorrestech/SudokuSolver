def print_grid(s_grid):
    rows, cols = 9, 9

    for i in range(cols):
        if(i%3 == 0 and i != 0):
            print("-----------------------------")
        for j in range(rows):
            if(j%3 == 0 and j != 0):
                print("| " + str(s_grid[i][j]) + " ", end="")                
            else:
                print(" " + str(s_grid[i][j]) + " ", end="")
        print("\n")


def main():
    print("Welcome to my Sudoku Solver! ")
    rows, cols = 9, 9
    s_grid = [ [0 for i in range(cols)] for j in range(rows) ]
    print("Tell me what Your Sudoku Puzzle looks like by typing in coordinates on what numbers are at what places")
    print("Example: ")
    print("(1,1) 9")
    print("(9,9) 8")
    print("(3,3) 5")
    print("\n\n")


    print(" 9 0 0 | 0 0 0 | 0 0 0 ")
    print("                        ")
    print("-----------------------------")
    print("                        ")
    print(" 0 0 0 | 0 0 0 | 0 0 0 ")
    print("                        ")
    print("-----------------------------")
    print("                         ")
    print(" 0 0 0 | 0 0 0 | 0 0 8 ")
    print("\n\n")


    print_grid(s_grid)
    

# always include this because it will make sure to run our main.
if __name__ == "__main__":
    main()