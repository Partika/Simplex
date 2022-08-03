def getcofactor(m, i, j):
    return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]


def determinantOfMatrix(mat):
    # nao tinha pra matriz (1,1)
    if(len(mat) == 1):
        return mat[0]
    # fim adicao
    if(len(mat) == 2):
        value = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
        return value
    Sum = 0
    for current_column in range(len(mat)):
        sign = (-1) ** (current_column)
        sub_det = determinantOfMatrix(getcofactor(mat, 0, current_column))
        Sum += (sign * mat[0][current_column] * sub_det)
    return Sum
# acabo o laplace do geeks for geeks


def pivot(mat, col):
    if(mat[col][col] == 0):
        tam = len(mat)
        sel = col
        for i in range(col+1, tam):
            if(mat[i][col] != 0):
                sel = i
                break
        if(sel != col):
            aux = mat[col]
            mat[col] = mat[sel]
            mat[sel] = aux


def aumenta(mat, tam):
    for i in range(tam):
        for j in range(tam):
            if(i == j):
                mat[i].append(1)
            else:
                mat[i].append(0)
    for i in range(tam):
        mat.append([0]*tam)
    return mat


def escalonamento(mat, tam):
    for i in range(tam):
        if(mat[i][i]):
            pivot(mat, i)
        for j in range(tam):
            if(i == j):
                continue
            mul = mat[j][i]/mat[i][i]
            for k in range(tam*2):
                mat[j][k] = mat[j][k]-(mat[i][k])*mul
    return mat


def arruma(mat, tam):
    for i in range(tam):
        aux = mat[i][i]
        for j in range(tam*2):
            mat[i][j] = mat[i][j]/aux
    return mat


def inversa(mat):
    if(determinantOfMatrix(mat) == 0):
        return [False]
    tam = len(mat)
    mat = aumenta(mat, tam)
    mat = escalonamento(mat, tam)
    mat = arruma(mat, tam)

    return [True, mat]


mat = []
tam = int(input("tamanho da matriz?"))
#tam = int(input())
for i in range(tam):
    lin = []
    ent = input(f'linha {i+1}: ').split(' ')
    for j in ent:
        lin.append(float(j))
    mat.append(lin)
result = inversa(mat)
if(not(result[0])):
    print("a matriz nao eh inversivel")
else:
    mat = result[1]
    for i in range(tam):
        for j in range(tam, tam*2):
            if(mat[i][j] == 0):
                mat[i][j] = float(0)
            print(round(mat[i][j], 3), end=' \t')
        print()

'''
resumido

def Inversa(mat):
    if(np.linalg.det(mat) == 0):
        return False
    inversa = [[1, 0, 0][0, 1, 0][0, 0, 1]]
    tam = len(mat)
    for i in range(tam):
        if(mat[i][i] == 0):
            c = 1
            while ((i + c) < tam and mat[i + c][i] == 0):
                c += 1
            if((i + c) == tam):
                return False
            for k in range(tam):
                swap(mat[i][k], mat[i+c][k])
        for j in range(tam):
            if(i == j):
                continue
            mul = mat[j][i]/mat[i][i]
            for k in range(tam):
                mat[j][k] = mat[j][k]-(mat[i][k])*mul
                inversa[j][k] = inversa[j][k]-(mat[i][k])*mul
    for i in range(tam):
        for j in range(tam):
            inversa[i][j] = inversa[i][j]/mat[i][i]
    return True, inversa
'''