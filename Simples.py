# Integrantes: Matheus Partika Orzechowski, Leonardo Pães, Piasinho
from tkinter.tix import MAX
import numpy as np


# Fase I : Leitura dos dados

# 1 : Determine inicialmente uma partição básica factível

def leitura():
    
    lin = 0 
    funcao_grudada = []
    funcao = []

    print('leituras de meu pau: ')
    
    print('linhas da matriz A' )
    lin = int(input())

    for i in range(lin):
        print("digite a funcao boco: ")
        funcao_grudada.append(input())
        funcao.append(funcao_grudada[i].split(' '))
    return funcao


def attBasica(A, b):
    # calculo da matriz basica
    basica = []
    for i in range(len(A)):
        lin = []
        for j in b:
            lin.append(A[i][j])
        basica.append(lin)
    return basica


def attNaoBasica(A, n):
    # calculo da matriz nao basica
    naoBasica = []
    for i in range(len(A)):
        lin = []
        for j in n:
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
    # basicamente um vetor nulo
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
    # criacao inicial da transposta
    for i in range(tam):
        lin.append(0)
    for i in range(tam):
        transp.append(lin)
    # calculo da transposta
    for i in range(tam):
        for j in range(tam):
            transp[j][i] = mat[i][j]
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
    inv = inversa(B)
    transp = transposta(c)
    lambida = multMat(inv, transp)
    return lambida

    # 2.2 : custos relativos


def custoRelativo(custo_naoB, lamb, nao_basico):
    custo_relativo_naoB = []
    tam = len(custo_naoB)
    naoBasico = transposta(nao_basico)
    # itera pela coluna
    for i in range(tam):
        custo_relativo_naoB.append(
            custo_naoB[i] - multMat(lamb, transposta(naoBasico[i])))
    return custo_relativo_naoB

    # 2.3 : determinação da variavel a entrar na base


def custoMinimo(CN):
    # retorna indice minimo da funcao anterior
    menor = min(CN)
    return CN.index(menor)

    # Passo 3 : teste de otimalidade


def otimalidade(k, custoRelativo):
    # se k maior que 0, ta tudo bem
    if custoRelativo[k] > 0:
        return True
    else:
        return False

    # Passo 4 : calculo da direcao simplex


def calculoDeY(B, A, n, k):
    inv = inversa(B)
    a = []
    # coluna k da matriz nao basica
    for i in range(len(A)):
        a.append(A[i][n[k]])
    y = multMat(inv, a)
    return y

    # Passo 5 : determinacao do passo e variavel a sair da base


def passoEL(y, xRelativo):
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
    for i in range(len(y)):
        if(y <= 0):
            vet.append(MAX)
            continue
        vet.append(xRelativo[i]/y[i])
    # selecao do passo
    passo = min(vet)
    # qual a posicao do passo?
    l = vet.index(passo)
    return True, passo, l


def calculoDeL():

    return

    # Passo 6 : nova partição básica, troque a coluna l de B pela coluna k de N


def troca(B, N, l, k):
    swap(B[l], N[k])
    return

# 3 : Calcule o valor da função objetivo
