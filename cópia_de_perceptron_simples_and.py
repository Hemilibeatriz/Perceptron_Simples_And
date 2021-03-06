# -*- coding: utf-8 -*-
"""Cópia de Perceptron - Simples-AND.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IpI89T5QrP471a9LZ_91JwITpSuJpcoH

***
# <font color=black size=6> <b>Perceptron simples - Exemplo - Operador AND</font>
***

# <font color=black>1 Importando Bibliotecas</font>
"""

import numpy as np

"""# <font color=black>2 Parâmetros de entrada, saída, pesos e taxa de Aprendizagem</font>

**Operador AND**
*   0 0 - 0
*   0 1 - 0
*   1 0 - 0
*   1 1 - 1
"""

entradas = np.array([[0,0],[0,1], [1,0], [1,1]])
#saidas = np.array([0,1,1,0]) XOR
saidas = np.array([0,0,0,1])

pesos = np.array([0.0, 0.0])
taxaAprendizagem = 0.1

"""# <font color=black>3 Step function</font>"""

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

"""# <font color=black>4 Função de somar os produtos</font>"""

def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

"""# <font color=black>5 Treinamento</font>

Detalhes importantes:
- Erro = Saída Esperada - Saída Calculada
- Erro Total = Soma dos errros
- Ajuste dos pesos (observar que ele considera a taxa de Aprendizagem, que determina o quão rápido esse ajuste ocorre - controla o risco de ótimos locais)
"""

def treinar():
    erroTotal = 1
    while (erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            
            entradas_aux=np.asarray(entradas[i])
            saida_aux=saidas[i]

            saidaCalculada = calculaSaida(entradas_aux)
            erro = saida_aux - saidaCalculada
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas_aux[j] * erro)
                print('Peso atualizado: ' + str(pesos[j]))
        print('Total de erros: ' + str(erroTotal))

"""# <font color=black>6 Executa treinamento</font>

"""

treinar()
print('Rede neural treinada')

"""# <font color=black>7 Testando a rede</font>

"""

print(calculaSaida(entradas[0]))
print(calculaSaida(entradas[3]))
print(calculaSaida(entradas[2]))
print(calculaSaida(entradas[1]))