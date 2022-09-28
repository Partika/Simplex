# invntegrantes: Matheus Partika Orzechowski, Jose Leonardo Machado Pães, Samuel Piasinho
from xmlrpc.client import MAXINT
import numpy as np


# Fase inv : Leitura dos dados

# 1 : Determine inicialmente uma partição básica factível

def leitura():
    # ler funcao z,
    # ler matriz das funcoes (multiplicador das variaveis basicas e nao basicas),
    # ler matriz b (um vetor / uma coluna)
    mat = []
    B = []
    b = []
    n = []
    z = []
    diff = []
    z = input("digite a funcao z separada por espacos (2 -4 3): ")
    z = z.split(' ')
    minMax=input('digite min para minimizar e max para maximizar')
    for i in range(len(z)):
        z[i] = float(z[i])
    maxMin = 0
    while(True):
        maxMin = input('digite min para minimizar ou max para maximizar')
        if(maxMin == 'min' or maxMin == 'max'):
            break
    if(maxMin == 'max'):
        for i in range(len(z)):
            z[i] = z[i]*-1
    print(z)
    num = int(input("qual o numero de funcoes? "))
    print("insira as funcoes separadas por enter")
    # gera mat (matriz das funcoes) e B (matriz dos termos independentes)
    for i in range(num):
        new = input(
            f"digite a funcao {i+1} separada por espacos (2 -4 3 <= 5): ").split()
        independente = False
        lin = []
        for j in range(len(new)):
            if(new[j] == '<=' or new[j] == '>=' or new[j] == '='):
                diff.append(new[j])
                independente = True
            elif(independente):
                B.append(float(new[j]))
            else:
                lin.append(float(new[j]))
        mat.append(lin)
    # completa mat
    for i in range(len(diff)):
        valor = 0
        if(diff[i] == '<='):
            valor = 1
        elif(diff[i] == '>='):
            valor = -1
        for j in range(len(diff)):
            if(j == i):
                mat[i].append(valor)
            else:
                mat[i].append(0)
    # completa z
    for i in range(len(diff)):
        z.append(0)
    # gera o vetor basico
    for i in range(0, len(z)):
        n.append(i)
    """ print(f'mat = {mat}')
    print(f'B = {B}')
    print(f'b = {b}')
    print(f'n = {n}')
    print(f'z = {z}') """
    return mat, B, [3,5,4], [1,2], z, minMax


def attBasica(mat, b):
    # calculo da matriz basica
    basica = []
        if i < num:
            b.append(i)
    # gera o vetor nao basico
    for i in range(len(b)):
        n.remove(b[i])
    # arruma as basicas para ter inversa
    for i in range(num,len(z)):
        if(inversa(attSubMatriz(mat,b))):
            break
        n.append(b[num-1])
        b[num-1]=i
        n.remove(i)
        n.sort()
    # print(f'mat = {mat}')
    # print(f'B = {B}')
    # print(f'b = {b}')
    # print(f'n = {n}')
    # print(f'z = {z}')
    return mat, B, b, n, z


def attSubMatriz(mat, v):
    # calculo da submatriz
    subMatriz = []
    for i in range(len(mat)):
        lin = []
        for j in v:
            lin.append(mat[i][j])
        subMatriz.append(lin)
    #print(f'subMatriz: {subMatriz}')
    return subMatriz


# 2 : Faça iteração ← 1

# Fase invinv : início da iteração simplex

    # Passo 1 : calculo da solucao basica


# por algum motivo ele ta usando a identidade
def multMatVet(A, v):
    c = []
    tam = len(A)
    # print(f'A={A}')
    # criacao do c
    for i in range(tam):
        c.append(0)
    # multiplicacao em si
    for i in range(tam):
        for k in range(tam):
            #print(f'{c[i]} += {A[i][k]} * {v[k]}')
            c[i] += A[i][k] * v[k]
    #print(f'resultado da multiplicacao: {c}')
    return c


def XRelativoBasico(mat, b):
    #print("++ Entrando na funcao do Xrel ++")
    xRelativo = []
    xRelativo = multMatVet(mat, b)
    #print(f' Na funcao xrel: {xRelativo}')
    #print("++ Saindo da funcao do Xrel ++")
    return xRelativo

    # Passo 2 : calculo dos custos relativos

    # 2.1 : vetor multiplicador simplex


def custoBasico(z, b):
    #print("++ Entrando na funcao do custo basico ++")
    custoB = []
    for i in b:
        custoB.append(z[i])
    #print(f"custo basico: {custoB}")
    #print("++ Saindo da funcao do custo basico ++")
    return custoB


def swap(a, b):
    aux = b
    b = a
    a = aux


def inversa(mat):
    # verificacao do determinante
    if(np.linalg.det(mat) == 0):
        return False
    tam = len(mat)
    inv = np.zeros((tam, tam))
    for i in range(tam):
        inv[i][i] = 1
    # armazena os itens da matriz em uma unica variavel
    indices = list(range(tam))
    for diagonal in range(tam):  # escala fd linha com fd inverso
        # Scale altera intervalo de valores sem alterar o original, normalmente sendo 0 e 1 o intevalo
        diagonalScaler = 1.0 / mat[diagonal][diagonal]
        # ajuda para dimensionamento e padronização
        for j in range(tam):  # J é loop de coluna
            mat[diagonal][j] *= diagonalScaler
            inv[diagonal][j] *= diagonalScaler

        for i in indices[0:diagonal] + indices[diagonal+1:]:  # pula a linha com coluna
            Linha_atual_Scaler = mat[i][diagonal]
            for j in range(tam):  # linhas * coluna uma por vez
                mat[i][j] = mat[i][j] - Linha_atual_Scaler * mat[diagonal][j]
                inv[i][j] = inv[i][j] - Linha_atual_Scaler * inv[diagonal][j]
    return True, inv


def transposta(mat):
    transp = np.transpose(mat)
    return transp


def multMat(A, B):
    c = []
    tam = len(A)
    tam2 = len(B[0])
    lin = []
    # criacao do c
    for i in range(tam):
        lin.append(0)
    for j in range(tam2):
        c.append(lin)
    # multiplicacao em si
    for i in range(tam):
        for k in range(tam):
            for j in range(tam2):
                c[i][j] += A[i][k] * B[k][j]
    return c


def calculaLambda(B, c):
    #print("++ Entrando na funcao da Lambda ++")
    #print(f"inv: {B}")
    #print(f"custo transposto: {c}")
    lambida = multMatVet(B, c)
    #print(f"lambda: {lambida}")
    #print("++ Saindo da funcao da Lambda ++")
    return lambida

    # 2.2 : custos relativos


def multVet(A, B):
    #print("++ Entrando na multiplicacao de vetores++")
    c = 0
    tam = len(A)
    #print(f'vet 1: {A}; vet 2: {B}')
    # multiplicacao em si
    for k in range(len(B)):
        #print(f'{k}) c={c}+{A[k]}*{B[k]}')
        c += A[k] * B[k]
    #print(f"saida: {c}")
    #print("++ Sainda da multiplicacao de vetores ++")
    return c


def custoRelativo(custo_naoB, lamb, nao_basico):
    # print("++ Entrando na funcao do custo relativo ++")
    custo_relativo_naoB = []
    naoBasico = transposta(nao_basico)
    # print(f'matriz nao basica transposta: {naoBasico}')
    tam = len(custo_naoB)
    # itera pela coluna
    for i in range(tam):
        # print(f'custo_naoB[{i}]: {custo_naoB[i]}')
        # print(f'naoBasico[{i}]: {naoBasico[i]}')
        custo_relativo_naoB.append(
            custo_naoB[i] - multVet(lamb, naoBasico[i]))
    # print(f"custo relativo nao basico: {custo_relativo_naoB}")
    # print("++ Saindo da funcao do custo relativo ++")
    return custo_relativo_naoB

    # 2.3 : determinação da variavel a entrar na base


def custoMinimo(CN):
    # retorna indice minimo da funcao anterior
    menor = min(CN)
    return CN.index(menor)

    # Passo 3 : teste de otimalidade


def otimalidade(k, custoRelativo):
    # se k maior que 0, ta tudo bem
    if custoRelativo[k] >= 0:
        return True
    else:
        return False

    # Passo 4 : calculo da direcao simplex


def calculoDeY(B, naoBasica, k):
    # coluna k da matriz nao basica
    naoBasicaT = transposta(naoBasica)
    #print(f'naoBasicaT: {naoBasicaT[k]}')
    y = multMatVet(B, naoBasicaT[k])
    return y

    # Passo 5 : determinacao do passo e variavel a sair da base


def Passo(vet, inicio):
    menor = inicio
    for i in range(len(vet)):
        if(vet[i] == -1):
            continue
        if(vet[i] < vet[menor]):
            menor = i
    return vet[menor]


def CalculoDeL(y, xRelativo):
    # se tem pelo menos 1 y maior que 0
    possivel = False
    for i in y:
        if i > 0:
            possivel = True
            break
    if(not(possivel)):
        return False
    # calculo do vetor das divisoes
    vet = []
    menor = 0
    valido = False
    for i in range(len(y)):
        if(y[i] <= 0):
            vet.append(-1)
            if(not(valido)):
                menor += 1
            continue
        valido = True
        vet.append(xRelativo[i]/y[i])
    # selecao do passo
    passo = Passo(vet, menor)
    # qual a posicao do passo?
    l = vet.index(passo)
    return True, l

    # Passo 6 : nova partição básica, troque a coluna l de B pela coluna k de N


def troca(mat, B, b, N, n, l, k):
    aux = b[l]
    b[l] = n[k]
    n[k] = aux
    B = attSubMatriz(mat, b)
    N = attSubMatriz(mat, n)
    return B, b, N, n


# 3 : Calcule o valor da função objetivo

def valorFuncao(z, x, b):
    resultado = 0
    for i in range(len(x)):
        resultado += z[b[i]]*x[i]
    return resultado


# main
def main():
    mat, B, b, n, z , minMax= leitura()
    func=z
    if(minMax=='max'):
        for i in z: i*=-1
    
    basica = attBasica(mat, b)
    #print(f'basica: {basica}')
    naoBasica = attNaoBasica(mat, n)
    #print(f'nao basica: {naoBasica}')
    print()
    it = 0
    maxit = 10
    possivel = True
    while(True and it < maxit):
        print(f"---------------IT {it+1}-----------")
        inversaBasica = inversa(basica)
        if(not(inversaBasica)):
            possivel = False
            break
        else:
            inversaBasica = inversaBasica[1]
        # print(f'inversa: {inversaBasica}')
        xRelativo = XRelativoBasico(inversaBasica, B)
        #print(f'xrel: {xRelativo}')
        lambida = calculaLambda(inversaBasica, custoBasico(z, b))
        # print(f'lambda: {lambida}')
        cRelativo = custoRelativo(
            custoBasico(z, n), lambida, naoBasica)
        # print(f'crel: {cRelativo}')
        # comentei ate aqui
        min = custoMinimo(cRelativo)
        # print(f'k: {min}')
        if(otimalidade(min, cRelativo)):
            print("otimo")
            break
        print("nao otimo")
        #print(f'{min} {n} {cRelativo}')
        y = calculoDeY(inversaBasica, naoBasica, min)
        #print(f'xrel:{xRelativo},\n y: {y}')
        l = CalculoDeL(y, xRelativo)
        #print(f'passo, l: {passol}')
        if(l):
            l = l[1]
        else:
            possivel = False
            break
        basica, b, naoBasica, n = troca(mat, basica, b, naoBasica, n, l, min)
        #print(f"b: {b}; n: {n}")
        it += 1
    print()
    if(possivel):
        print(
            f'xrel: {xRelativo},\nb: {b},\nz(x): {valorFuncao(func, xRelativo, b)}')
    else:
        print("problema nao tem solucao otima finita ou gera uma matriz sem inversa")


main()
