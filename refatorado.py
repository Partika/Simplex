import numpy as np

# funcoes extras necessarias


def Multiplicacao_matrizes(matrizA, matrizB):
    matrizC = np.matmul(matrizB, matrizA)

    return matrizC[0]


def transposta(matriz):
    return


# SIMPLEX, SIMPLAO, COMPLEX

def Inversa(matriz):
    return np.transpose(matriz)


# Fase I:

#   1. Determine inicialmente uma parti¸c˜ao b´asica fact´ıvel A=[B,N]. A rigor, precisa-se de
#   dois vetores de ´ındices b´asicos e n˜ao-b´asicos:
#   (B1, B2, ..., Bm) e (N1, N2, ..., Nn−m)
#   Os vetores das vari´aveis b´asicas e n˜ao-b´asicas, respectivamente:
#   x transpost basico = (xB1, xB2, ..., xBm ) e
#   x transposto nao basico = (xN1, xN2, ..., xNn−m ).


def Separacao_da_matriz(funcaoZ, funcoes):
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

    # area de testes
    # print(matrizA)
    # print(basicas)
    # print(naoBasicas)

    return matrizA, basicas, naoBasicas


Separacao_da_matriz([5, 8], [[1, 2, '<=', 6], [5, 9, '<=', 45]])

#   2. Fa¸ca itera¸c˜ao ← 1.


# Fase II: {in´ıcio da itera¸c˜ao simplex}

#   Passo 1: {c´alculo da solu¸c˜ao b´asica}
#       x relativo basico ← B−1*b (equivalentemente, resolva o sistema B * x relativo basico = b)
#       x relativo nao basico ← 0
# !!!(devido a analises, o x relativo nao basico nao foi feito, afinal ele nao aparece mais)!!!

def Calculo_x_relativo(BInversa, b):
    xRelativoBasico = Multiplicacao_matrizes(BInversa, np.matrix(b))
    print(xRelativoBasico)
    return xRelativoBasico


Calculo_x_relativo([[1, 0], [0, 1]], [2, 3])

#   Passo 2: {c´alculo dos custos relativos}

#       2.1) {vetor multiplicador simplex}
#           λ transposto ← c transposto basico B^−1
#           (equivalentemente, resolva o sistema B transposto * λ = cB)


#       2.2) {custos relativos}
#           c relativo nao basico j ← c nao basico j − (λ transposto * a nao bascio j)
#           j = 1, 2, ..., n − m


#       2.3) {determina¸c˜ao da vari´avel a entrar na base}
#           c relativo nao basico k ← min{c relativo nao basico j, j = 1, 2, ..., n − m}
#           (a variavel x nao basico k entra na base)


#   Passo 3: {teste de otimalidade}
#       Se c relativo nao basico k ≥ 0, ent˜ao: pare {solu¸c˜ao na itera¸c˜ao atual ´e ´otima}


#   Passo 4: {c´alculo da dire¸c˜ao simplex}
#       y ← B^−1 * a nao basico k
#       (equivalentemente, resolva o sistema: B*y = a nao basico k)


#   Passo 5: {determina¸c˜ao do passo e vari´avel a sair da base}
#       Se y ≤ 0, ent˜ao: pare {problema n˜ao tem solu¸c˜ao ´otima finita f(x) → −∞ }
#       Caso contr´ario, determine a vari´avel a sair da base pela raz˜ao m´ınima:
#       ε ← x relativo basico l/yl= min{x relativo basico i/yi, tal que yi> 0, i = 1, 2, ..., m}
#       (a variavel xBl sai da base)


#   Passo 6: {atualiza¸c˜ao: nova parti¸c˜ao b´asica, troque a l-´esima coluna de B pela k-´esima
#   coluna de N}
#       matriz b´asica nova: B ← [a basico 1...a basico (l−1) a nao basico k a basico (l+1) ...a basico m ]
#       matriz n˜ao-b´asica nova: N ← [a nao basico 1...a nao basico (k−1) a basico l a naos basico (k+1) ...a nao basico (n−m) ]
#       itera¸c˜ao ← itera¸c˜ao + 1
#       Retorne ao Passo 1
#       {fim da itera¸c˜ao simplex}


# 3. Calcule o valor da fun¸c˜ao objetivo f(x) =⇒ FIM.


# main


def main():
    return
