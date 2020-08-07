sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

counter = 0
cikti = ""
tire = "- - - - - - - - - - -\n"

for i in sudoku:
    if counter == 0 or counter % 3 == 0:
        cikti += tire
        c = 1
        for a in i:
            if c % 3 == 0 and c != 9:
                cikti += str(a) + " " + "| "
            else:
                cikti += str(a) + " "
            c += 1
        cikti += "\n"
    elif counter == 8:
        c = 1
        for a in i:
            if c % 3 == 0 and c != 9:
                cikti += str(a) + " " + "| "
            else:
                cikti += str(a) + " "
            c += 1
        cikti += "\n" + tire       
    else:
        c = 1
        for a in i:
            if c % 3 == 0 and c != 9:
                cikti += str(a) + " " + "| "
            else:
                cikti += str(a) + " "
            c += 1
        cikti += "\n"

    counter += 1
    
print(cikti)
