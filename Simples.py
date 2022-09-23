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
    for i in range(len(z)):
        z[i] = int(z[i])
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
    for i in range(1, len(mat)+1):
        b.append(i)
    # gera o vetor nao basico
    for i in range(len(mat)+1, len(z)+1):
        n.append(i)
    """ print(f'mat = {mat}')
    print(f'B = {B}')
    print(f'b = {b}')
    print(f'n = {n}')
    print(f'z = {z}') """
    return mat, B, [1, 2, 4], [3, 5], z


def attBasica(mat, b):
    # calculo da matriz basica
    basica = []
    for i in range(len(mat)):
        lin = []
        for j in b:
            lin.append(mat[i][j-1])
        basica.append(lin)
    return basica


def attNaoBasica(mat, n):
    # calculo da matriz nao basica
    naoBasica = []
    for i in range(len(mat)):
        lin = []
        for j in n:
            lin.append(mat[i][j-1])
        naoBasica.append(lin)
    return naoBasica

# 2 : Faça iteração ← 1

# Fase invinv : início da iteração simplex

    # Passo 1 : calculo da solucao basica


def multMatVet(mat, B):
    c = []
    tam = len(mat)
    # criacao do c
    for i in range(tam):
        c.append(0)
    # multiplicacao em si
    for i in range(tam):
        for k in range(tam):
            c[i] += mat[i][k] * B[k]
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
        custoB.append(z[i-1])
    #print(f"custo basico: {custoB}")
    #print("++ Saindo da funcao do custo basico ++")
    return custoB


def swap(a, b):
    aux = b
    b = a
    a = aux


def inversa(mat, independentes):
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
    """ # eliminacao de gauss jordan
    for i in range(tam):
        # escolha do pivo / pivot nao sei
        if(mat[i][i] == 0):
            c = 1
            while ((i + c) < tam and mat[i + c][i] == 0):
                c += 1
            if((i + c) == tam):
                return False
            for k in range(tam):
                aux = mat[i][k]
                mat[i][k] = mat[i+c][k]
                mat[i+c][k] = aux
                aux = inv[i][k]
                inv[i][k] = inv[i+c][k]
                inv[i+c][k] = aux
                # swap(mat[i][k], mat[i+c][k])
                #swap(inv[i][k], inv[i+c][k])
            #swap(independentes[i], independentes[i+c])
            aux = independentes[i]
            independentes[i] = independentes[i+c]
            independentes[i+c] = aux
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
            inv[i][j] = inv[i][j]/mat[i][i] """
    return True, inv


def transposta(mat):
    transp = np.transpose(mat)
    return transp


def multMat(mat, B):
    c = []
    tam = len(mat)
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
                c[i][j] += mat[i][k] * B[k][j]
    return c


def calculaLambda(B, c):
    #print("++ Entrando na funcao da Lambda ++")
    #print(f"inv: {B}")
    #print(f"custo transposto: {transp}")
    lambida = multMatVet(B, c)
    #print(f"lambda: {lambida}")
    #print("++ Saindo da funcao da Lambda ++")
    return lambida

    # 2.2 : custos relativos


def multVet(A, B):
    #print("++ Entrando na multiplicacao de vetores++")
    c = 0
    tam = len(A)
    #print(f'vet 1: {mat}; vet 2: {B}')
    # multiplicacao em si
    for k in range(len(B)):
        #print(f'{k}) c={c}+{A[k]}*{B[k]}')
        c += A[k] * B[k]
    #print(f"saida: {c}")
    #print("++ Sainda da multiplicacao de vetores ++")
    return c


def custoRelativo(custo_naoB, lamb, nao_basico):
    #print("++ Entrando na funcao do custo relativo ++")
    custo_relativo_naoB = []
    naoBasico = transposta(nao_basico)
    #print(f'matriz nao basica transposta: {naoBasico}')
    tam = len(custo_naoB)
    # itera pela coluna
    for i in range(tam):
        #print(f'mult(lamb, colunaN):{multVet(lamb, naoBasico[i])}')
        custo_relativo_naoB.append(
            custo_naoB[i] - multVet(lamb, naoBasico[i]))
    #print(f"custo relativo nao basico: {custo_relativo_naoB}")
    #print("++ Saindo da funcao do custo relativo ++")
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


def calculoDeY(B, mat, n, k):
    a = []
    # coluna k da matriz nao basica
    for i in range(len(mat)):
        a.append(mat[i][n[k]-1])
    y = multMatVet(B, a)
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
        if(y[i] <= 0):
            vet.append(MAXINT)
            continue
        vet.append(xRelativo[i]/y[i])
    # selecao do passo
    passo = min(vet)
    # qual a posicao do passo?
    l = vet.index(passo)
    return True, passo, l

    # Passo 6 : nova partição básica, troque a coluna l de B pela coluna k de N


def troca(mat, B, b, N, n, l, k):
    aux = b[l]
    b[l] = n[k]
    n[k] = aux
    B = attBasica(mat, b)
    N = attNaoBasica(mat, n)
    return B, b, N, n


# 3 : Calcule o valor da função objetivo

def valorFuncao(z, x, b):
    resultado = 0
    for i in range(len(x)):
        resultado += z[b[i]-1]*x[i]
    return resultado


# main
def main():
    mat, B, b, n, z = leitura()
    basica = attBasica(mat, b)
    #print(f'basica: {basica}')
    naoBasica = attNaoBasica(mat, n)
    #print(f'nao basica: {naoBasica}')
    print()
    it = 0
    maxit=10
    possivel = True
    while(True and it < maxit):
        print(f"---------------IT {it+1}-----------")
        inversaBasica = inversa(basica, B)
        if(not(inversaBasica[0])):
            possivel = False
            break
        else:
            inversaBasica = inversaBasica[1]
        #print(f'inversa: {inversaBasica}, independentes: {B}')
        xRelativo = XRelativoBasico(inversaBasica, B)
        #print(f'xrel: {xRelativo}')
        if(xRelativo == False):
            possivel = False
            break
        lambida = calculaLambda(inversaBasica, custoBasico(z, b))
        #print(f'lambda: {lambida}')
        cRelativo = custoRelativo(
            custoBasico(z, n), lambida, naoBasica)
        #print(f'crel: {cRelativo}')
        # comentei ate aqui
        min = custoMinimo(cRelativo)
        #print(f'k: {min}')
        if(otimalidade(min, cRelativo)):
            print("otimo")
            break
        print("nao otimo")
        y = calculoDeY(basica, mat, n, min)
        #print(f'y: {y}')
        passol = passoEL(y, xRelativo)
        #print(f'passo, l: {passol}')
        if(passol):
            passo = passol[1]
            l = passol[2]
        else:
            possivel = False
            break
        basica, b, naoBasica, n = troca(mat, basica, b, naoBasica, n, l, min)
        #print(f"b: {b}; n: {n}")
        it += 1
    print()
    if(possivel):
        print(
            f'xrel: {xRelativo},\nb: {b},\nz(x): {valorFuncao(z, xRelativo, b)}')
    else:
        print("problema nao tem solucao otima finita ou gera uma matriz sem inversa")


main()
