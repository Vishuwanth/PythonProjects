N  = int(input())

matrix_list = []
for row in range(N):
    row_input = input().split()
    row = []
    for each in row_input:
        row.append(int(each))
    matrix_list.append(row)
#print(matrix_list)

inputs = []
while True:
    try:
        inp = input().split()
        if inp == "":
            break
        inputs.append(inp)
    except:
        break

def rotationMatix(matrix_list,S):
    count = 0
    rot_times = (int(int(S)/ 90 ) % 4)
    new_matrix = matrix_list
    
    while ( count < rot_times):
        global rot_matrix
        rot_matrix = []
        for i in range(N):
            row= []
            for j in range(N,0,-1):
                row.append(new_matrix[j-1][i])
            rot_matrix.append(row)
        new_matrix = rot_matrix
        count += 1
    return new_matrix
        
def queryIndex(matrix_list,K,L):
    return matrix_list[K][L]

def updateMatrix(matrix_list):
    matrix_list[X][Y] = int(Z)
    return matrix_list
    
S = 0
for operation in inputs[:-1]:
    if operation[0] == "R":
        S += int(operation[1])
        #print("S:",S)
        rot_list = rotationMatix(matrix_list,S)
    elif operation[0] == "Q":
        K = int(operation[1])
        L = int(operation[2])
        try:
            print(queryIndex(rot_list,K,L))
        except NameError:
            print(queryIndex(matrix_list,K,L))
        
    elif operation[0]=="U":
        #print(S)
        #print(matrix_list)
        X = int(operation[1])
        Y = int(operation[2])
        Z = int(operation[3])
        new_s = S
        updated_matrix = updateMatrix(matrix_list)
        updated_matrix = rotationMatix(matrix_list,new_s)
        rot_list = updated_matrix
        