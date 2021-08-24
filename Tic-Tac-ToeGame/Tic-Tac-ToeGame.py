game_matrix = []
for each in range(3):
    input_1 = input().split()
    game_row_matrix = []
    for each in input_1:
        if each == "X":
            game_row_matrix.append(1)
        elif each == "O":
            game_row_matrix.append(0)
    game_matrix.append(game_row_matrix)
#print(game_matrix)

def checkRows(game_matrix):
    for each_row in game_matrix:
        if sum(each_row) == 3:
            print("Anjali Wins")
            break;
        elif sum(each_row) == 0:
            print("Abhinav Wins")
            break;
    else:
        checkColums(game_matrix)
def checkColums(game_matrix):
    transpose_matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(game_matrix[j][i])
        transpose_matrix.append(row)
    #print(transpose_matrix)  
    
    for each_row in transpose_matrix:
        if sum(each_row) == 3:
            print("Anjali Wins")
            break;
        elif sum(each_row) == 0:
            print("Abhinav Wins")
            break;
    else:
        checkDiagonals(game_matrix)
def checkDiagonals(game_matrix):
    count = 0
    principle_diagonal_elements = []
    row = []
    for i in range(3):
        row.append(game_matrix[i][i])
    principle_diagonal_elements.append(row)
    another_dia = [game_matrix[2][0],game_matrix[1][1],game_matrix[0][2]]
    principle_diagonal_elements.append(another_dia)
    #print(principle_diagonal_elements)
    for each_row in principle_diagonal_elements:
        if sum(each_row) == 3:
            print("Anjali Wins")
            break;
        elif sum(each_row) == 0:
            print("Abhinav Wins")
            break;
    else:
        print("Tie")
checkRows(game_matrix)