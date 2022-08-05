# Integrantes: Matheus Partika Orzechowski, Leonardo Pães, Piasinho
import numpy as np


# Fase I : Leitura dos dados

# 1 : Determine inicialmente uma partição básica factível

def leitura():
    return

def attBasica(A,B):
    basica=[]
    for i in range(len(A)):
        lin=[]
        for j in B:
            lin.append(A[i][j])
        basica.append(lin)
    return basica

def attNaoBasica(A,N):
    naoBasica=[]
    for i in range(len(A)):
        lin=[]
        for j in N:
            lin.append(A[i][j])
        naoBasica.append(lin)
    return naoBasica

# 2 : Faça iteração ← 1

# Fase II : início da iteração simplex

    # Passo 1 : calculo da solucao basica


def XRelativoBasico(mat, b):
    xRelativo = []
    tam = len(mat)
    # calcula a inversa
    inv = inversa(mat)
    # multiplica inversa por vetor de termos independentes
    for i in range(tam):
        for k in range(tam):
            xRelativo[i] += inv[i][k] * b[k]
    return xRelativo


def XRelativoNaoBasico(tam):
    relativoN = []
    for i in range(tam):
        relativoN.append(0)
    return relativoN

    # Passo 2 : calculo dos custos relativos

    # 2.1 : vetor multiplicador simplex


def swap(a, b):
    aux = b
    b = a
    a = aux


def inversa(mat):
    # verificacao do determinante
    if(np.linalg.det(mat) == 0):
        return False
    inv = [[1, 0, 0][0, 1, 0][0, 0, 1]]
    tam = len(mat)
    # eliminacao de gauss jordan
    for i in range(tam):
        # escolha do pivo / pivot nao sei
        if(mat[i][i] == 0):
            c = 1
            while ((i + c) < tam and mat[i + c][i] == 0):
                c += 1
            if((i + c) == tam):
                return False
            for k in range(tam):
                swap(mat[i][k], mat[i+c][k])
        # escalonamento
        for j in range(tam):
            if(i == j):
                continue
            mul = mat[j][i]/mat[i][i]
            for k in range(tam):
                mat[j][k] = mat[j][k]-(mat[i][k])*mul
                inv[j][k] = inv[j][k]-(mat[i][k])*mul
    # fazendo a "principal virar a identidade" para que a auxiliar vire a inversa
    for i in range(tam):
        for j in range(tam):
            inv[i][j] = inv[i][j]/mat[i][i]
    return True, inv


def transposta(mat):
    transp = []
    lin = []
    tam = len(mat)
    for i in range(tam):
        lin.append(0)
    for i in range(tam):
        transp.append(lin)
    for i in range(tam):
        for j in range(tam):
            transp[j][i] = mat[i][j]
    return transp


def multMat(A, B):
    c = []
    tam = len(A)
    tam2 = len(B)
    lin = []
    for i in range(tam):
        lin.append(0)
    for j in range(tam2):
        c.append(lin)
    for i in range(tam):
        for k in range(tam):
            for j in range(tam2):
                c[i][j] += A[i][k] * B[k][j]
    return c


def calculaLambda(B, c):
    inv = inversa(B)
    transp = transposta(c)
    lambida = multMat(inv, transp)
    return lambida

    # 2.2 : custos relativos


def custoRelativo():
    return

    # 2.3 : determinação da variavel a entrar na base


def custoMinimo():
    return

    # Passo 3 : teste de otimalidade


def otimalidade():
    return

    # Passo 4 : calculo da direcao simplex


def calculoDeY():
    return

    # Passo 5 : determinacao do passo e variavel a sair da base


def calculoDeL():
    return

    # Passo 6 : nova partição básica, troque a coluna l de B pela coluna k de N


def troca(B, N, l, k):
    swap(B[l], N[k])
    return

# 3 : Calcule o valor da função objetivo
