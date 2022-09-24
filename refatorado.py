from xmlrpc.client import MAXINT
import numpy as np

from Simples import valorFuncao

# funcoes extras necessarias


def Multiplicacao_matrizes(matrizA: list, matrizB: list):
    matrizC = np.matmul(matrizB, matrizA)
    return matrizC


def Multiplicacao_vetores(vetorA: list, vetorB: list):
    resultado = np.dot(vetorA, vetorB)
    return resultado


def Transposta(matriz: list):
    return np.transpose(matriz)


def Inversa(matriz: list):
    return np.linalg.inv(matriz)


def Cria_submatriz(matrizA: list, vetorX: list):
    submatriz = []
    for j in range(len(matrizA)):
        linha = []
        for i in range(len(vetorX)):
            linha.append(matrizA[j][vetorX[i]])
        submatriz.append(linha)
    return submatriz


# SIMPLEX, SIMPLAO, COMPLEX

# Fase I:

#   1. Determine inicialmente uma parti¸c˜ao b´asica fact´ıvel A=[B,N]. A rigor, precisa-se de
#   dois vetores de ´ındices b´asicos e n˜ao-b´asicos:
#   (B1, B2, ..., Bm) e (N1, N2, ..., Nn−m)
#   Os vetores das vari´aveis b´asicas e n˜ao-b´asicas, respectivamente:
#   x transpost basico = (xB1, xB2, ..., xBm ) e
#   x transposto nao basico = (xN1, xN2, ..., xNn−m ).


def Separacao_da_matriz(funcaoZ: list, funcoes: list):
    # definicao da existencia de variaveis de folga
    inequacoes = []
    for i in range(len(funcoes)):
        condicao = funcoes[i][-2]
        if condicao != '=':
            funcaoZ.append(0)
            if(condicao == '<='):
                inequacoes.append(1)
            else:
                inequacoes.append(-1)
        else:
            inequacoes.append(0)
    # fim da definicao das variaveis de folga

    # inicio do aumento da matriz A
    matrizA = []
    for i in range(len(funcoes)):
        linha = funcoes[i][:-2]
        for j in range(len(inequacoes)):
            if(i == j):
                linha.append(inequacoes[j])
            else:
                linha.append(0)
        matrizA.append(linha)
    # fim do aumento da matriz A

    # inicio da definicao basicas e nao basicas
    basicas = []
    naoBasicas = []
    maxBasicas = len(funcoes)
    for i in range(len(funcaoZ)):
        if(i < maxBasicas):
            basicas.append(i)
        else:
            naoBasicas.append(i)
    # fim da definicao basicas e nao basicas

    # inicio da criacao da matriz de termos independentes
    independentes = []
    for i in range(len(funcoes)):
        independentes.append(funcoes[i][-1])
    # fim da criacao da matriz de termos independentes

    # area de testes
    # print(matrizA)
    # print(basicas)
    # print(naoBasicas)

    return matrizA, basicas, naoBasicas, independentes


#Separacao_da_matriz([5, 8], [[1, 2, '<=', 6], [5, 9, '<=', 45]])

#   2. Fa¸ca itera¸c˜ao ← 1.


# Fase II: {in´ıcio da itera¸c˜ao simplex}

#   Passo 1: {c´alculo da solu¸c˜ao b´asica}
#       x relativo basico ← B−1*b (equivalentemente, resolva o sistema B * x relativo basico = b)
#       x relativo nao basico ← 0
# !!!(devido a analises, o x relativo nao basico nao foi feito, afinal ele nao aparece mais)!!!

def Calculo_x_relativo(BInversa: list, b: list):
    xRelativoBasico = Multiplicacao_matrizes(BInversa, np.matrix(b))
    # print(xRelativoBasico)
    return xRelativoBasico


#Calculo_x_relativo([[1, 0], [0, 1]], [2, 3])

#   Passo 2: {c´alculo dos custos relativos}

#       2.1) {vetor multiplicador simplex}
#           λ transposto ← c transposto basico B^−1
#           (equivalentemente, resolva o sistema B transposto * λ = cB)


def Custo(funcaoZ: list, variaveis: list):
    custoBasico = [0]*len(variaveis)
    for i in range(len(custoBasico)):
        custoBasico[i] = funcaoZ[variaveis[i]]
    return custoBasico


def Calcula_lambda(custoBasico: list, basicaInversa: list):
    lambdaSimplex = Multiplicacao_matrizes(basicaInversa, custoBasico)
    return lambdaSimplex


#       2.2) {custos relativos}
#           c relativo nao basico j ← c nao basico j − (λ transposto * a nao bascio j)
#           j = 1, 2, ..., n − m

def Custos_Relativos(lambdaSimplex: list, custoNaoBasico: list, matrizNaoBasica: list):
    naoBasicaTransposta = Transposta(matrizNaoBasica)
    print(matrizNaoBasica)
    print(naoBasicaTransposta)
    print(lambdaSimplex)
    custoRelativoNaoBasico = [0]*len(custoNaoBasico)
    for i in range(len(custoRelativoNaoBasico)):
        custoRelativoNaoBasico[i] = custoNaoBasico[i] - \
            (Multiplicacao_vetores(lambdaSimplex, naoBasicaTransposta[i]))
    return custoRelativoNaoBasico


#       2.3) {determina¸c˜ao da vari´avel a entrar na base}
#           c relativo nao basico k ← min{c relativo nao basico j, j = 1, 2, ..., n − m}
#           (a variavel x nao basico k entra na base)

def Calcula_k(custoRelativoNaoBasico: list):
    print(custoRelativoNaoBasico)
    menor = min(custoRelativoNaoBasico)
    return custoRelativoNaoBasico.index(menor)


#print(Calcula_k(Custos_Relativos([1, 0], [-2, -1], [[1, 0], [1, 1]])))

#   Passo 3: {teste de otimalidade}
#       Se c relativo nao basico k ≥ 0, ent˜ao: pare {solu¸c˜ao na itera¸c˜ao atual ´e ´otima}


def Otimalidade(custoRelativoNaoBasico: list, k: int):
    if(custoRelativoNaoBasico[k] >= 0):
        return True
    else:
        return False


#   Passo 4: {c´alculo da dire¸c˜ao simplex}
#       y ← B^−1 * a nao basico k
#       (equivalentemente, resolva o sistema: B*y = a nao basico k)


def Direcao_simplex(BasicaInversa: list, matrizA: list, k: int, naoBasicas: list):
    colunaK = [0]*len(matrizA)
    for i in range(len(matrizA)):
        colunaK[i] = matrizA[i][naoBasicas[k]]
    colunaK = Transposta(colunaK)
    y = Multiplicacao_matrizes(BasicaInversa, colunaK)
    return y

# print(Direcao_simplex([[1,0],[0,1]],[1,1]))

#   Passo 5: {determina¸c˜ao do passo e vari´avel a sair da base}
#       Se y ≤ 0, ent˜ao: pare {problema n˜ao tem solu¸c˜ao ´otima finita f(x) → −∞ }
#       Caso contr´ario, determine a vari´avel a sair da base pela raz˜ao m´ınima:
#       ε ← x relativo basico l/yl= min{x relativo basico i/yi, tal que yi> 0, i = 1, 2, ..., m}
#       (a variavel xBl sai da base)


def Calcula_l(y: list, xRelativoBasico: list):

    # se y <= 0
    seguro = False
    for i in range(len(y)):
        if y[i] > 0:
            seguro = True
            break
    if(not(seguro)):
        return [False]

    razoes = []
    for i in range(len(xRelativoBasico)):
        if(y[i] <= 0):
            razoes.append(MAXINT)
        else:
            razoes.append(xRelativoBasico[i]/y[i])

    passo = min(razoes)
    l = razoes.index(passo)

    return l


#   Passo 6: {atualiza¸c˜ao: nova parti¸c˜ao b´asica, troque a l-´esima coluna de B pela k-´esima
#   coluna de N}
#       matriz b´asica nova: B ← [a basico 1...a basico (l−1) a nao basico k a basico (l+1) ...a basico m ]
#       matriz n˜ao-b´asica nova: N ← [a nao basico 1...a nao basico (k−1) a basico l a naos basico (k+1) ...a nao basico (n−m) ]
#       itera¸c˜ao ← itera¸c˜ao + 1
#       Retorne ao Passo 1
#       {fim da itera¸c˜ao simplex}

def Troca_k_l(basicas: list, naoBasicas: list, k: int, l: int):
    aux = basicas[k]
    basicas[k] = naoBasicas[l]
    naoBasicas[l] = aux
    return basicas, naoBasicas


# 3. Calcule o valor da fun¸c˜ao objetivo f(x) =⇒ FIM.

def Valor_funcao(funcaoZ: list, xRelativoBasico: list):
    return Multiplicacao_vetores(funcaoZ, xRelativoBasico)


# main

def Leitura():
    funcaoZ = input("digite a funcao z separada por espacos (2 -4 3): ")
    funcaoZ = funcaoZ.split(' ')
    for i in range(len(funcaoZ)):
        funcaoZ[i] = int(funcaoZ[i])
    numeroFuncoes = int(input("qual o numero de funcoes? "))
    print("insira as funcoes separadas por enter")
    funcoes = []
    # gera mat (matriz das funcoes) e B (matriz dos termos independentes)
    for i in range(numeroFuncoes):
        novaFuncao = input(
            f"digite a funcao {i+1} separada por espacos (2 -4 3 <= 5): ").split()
        for j in range(len(novaFuncao)):
            if (novaFuncao[j] != novaFuncao[-2]):
                novaFuncao[j] = float(novaFuncao[j])
        funcoes.append(novaFuncao)
    return funcaoZ, funcoes


def main():
    funcaoZ, funcoes = Leitura()
    matrizA, basicas, naoBasicas, independentes = Separacao_da_matriz(
        funcaoZ, funcoes)
    it = 1
    maxit = 10
    solucaoOtima = []
    while(it < maxit):
        matrizBasica = Cria_submatriz(matrizA, basicas)
        matrizNaoBasica = Cria_submatriz(matrizA, naoBasicas)
        matrizBasicaInversa = Inversa(matrizBasica)

        xRelativo = Calculo_x_relativo(matrizBasicaInversa, independentes)

        custoBasico = Custo(funcaoZ, basicas)
        lambdaTransposto = Calcula_lambda(
            Transposta(custoBasico), matrizBasicaInversa)

        custoNaoBasico = Custo(funcaoZ, naoBasicas)
        custoRelativoNaoBasico = Custos_Relativos(
            lambdaTransposto, custoNaoBasico, matrizNaoBasica)

        k = Calcula_k(custoRelativoNaoBasico)

        if(Otimalidade(custoRelativoNaoBasico, k)):
            print("Otimo!")
            solucaoOtima = xRelativo
            break
        print("Nao otimo!")

        y = Direcao_simplex(matrizBasicaInversa, matrizA, k, naoBasicas)

        l = Calcula_l(y, xRelativo)

        basicas, naoBasicas = Troca_k_l(basicas, naoBasicas, k, l)
    # fim do laco de repeticao simplex

    print("A solucao factivel otima eh:")
    for i in range(len(solucaoOtima)):
        print(f'x{basicas[i]+1} = {solucaoOtima[i]}, ', end=' ')
    print(f'z = {Valor_funcao(funcaoZ, solucaoOtima)}')


print()
main()
