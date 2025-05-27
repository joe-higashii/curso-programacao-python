# 02-sintaxe-basica-python/exercicios/01_declaracao_variaveis.py

"""
Exercício 1: Declaração de Variáveis e Atribuição de Valor

Objetivo:
Praticar a declaração de variáveis em Python e a atribuição de valores a elas,
conforme ilustrado na Figura 5 do material do curso [1].

Instruções:
1. Crie uma variável chamada `nome_aluno` e atribua a ela uma string com um nome.
2. Crie uma variável chamada `idade_aluno` e atribua a ela um valor inteiro.
3. Crie uma variável chamada `nota_final_aluno` e atribua a ela um valor float (ex: 7.5).
4. Crie uma variável chamada `aluno_aprovado` e atribua a ela um valor booleano (True ou False),
   baseado em uma lógica simples (ex: se nota_final_aluno >= 7.0).
5. Imprima o valor e o tipo de cada uma dessas variáveis.
"""

# 1. Declaração e atribuição da variável nome_aluno (tipo string)
nome_aluno = "João Victor da Silva"  # Atribuindo um valor string

# 2. Declaração e atribuição da variável idade_aluno (tipo inteiro)
idade_aluno = 22  # Atribuindo um valor inteiro

# 3. Declaração e atribuição da variável nota_final_aluno (tipo float)
nota_final_aluno = 8.7  # Atribuindo um valor float (ponto flutuante)

# 4. Declaração e atribuição da variável aluno_aprovado (tipo booleano)
# A aprovação pode ser determinada por uma expressão lógica.
# Se a nota final for maior ou igual a 7.0, o aluno está aprovado (True).
aluno_aprovado = (nota_final_aluno >= 7.0) # Expressão que resulta em True ou False

# 5. Imprimindo os valores e os tipos das variáveis
# A função print() exibe informações no console.
# A função type() retorna o tipo de um dado ou variável.

print("--- Informações do Aluno ---")
print(f"Nome do Aluno: {nome_aluno}")
print(f"Tipo da variável 'nome_aluno': {type(nome_aluno)}")

print(f"\nIdade do Aluno: {idade_aluno} anos")
print(f"Tipo da variável 'idade_aluno': {type(idade_aluno)}")

print(f"\nNota Final do Aluno: {nota_final_aluno}")
print(f"Tipo da variável 'nota_final_aluno': {type(nota_final_aluno)}")

print(f"\nAluno Aprovado: {aluno_aprovado}")
print(f"Tipo da variável 'aluno_aprovado': {type(aluno_aprovado)}")

# Este exercício espelha o conceito da Figura 5 do material do curso [1],
# que demonstra a atribuição de um valor (25) a uma variável (idade_usuario).
# Aqui, expandimos para diferentes tipos de dados, que é o próximo tópico do material.

print("\n--- Fim do Exercício 1 ---")
