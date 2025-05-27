# 02-sintaxe-basica-python/exercicios/08_expressoes_matematicas_pemdas.py

"""
Exercício 8: Expressões Matemáticas (PEMDAS) e Condicionais Simples

Objetivo:
Praticar a construção de expressões matemáticas, respeitando a ordem de
precedência dos operadores (PEMDAS), e aplicar estruturas condicionais
básicas `if` e `else`.
Este exercício é baseado nas Figuras 21, 22, 23 e 24 do material do curso [1].
"""

print("--- Prática com Expressões Matemáticas e Condicionais ---")

# Parte 1: Expressões Matemáticas e PEMDAS (Baseado nas Figuras 21 e 22 [1])
# PEMDAS: Parênteses, Exponenciação, Multiplicação/Divisão, Adição/Subtração

print("\n--- Parte 1: Expressões Matemáticas e PEMDAS ---")
# Definindo variáveis para os cálculos
valor_x = 10.0
valor_y = 4.0
valor_z = 2.0
valor_w = 3.0

print(f"Valores: x={valor_x}, y={valor_y}, z={valor_z}, w={valor_w}")

# Expressão 1: x + y / z
# Ordem: Divisão (y/z) primeiro, depois Adição (x + resultado_divisao)
# 10.0 + 4.0 / 2.0  =>  10.0 + 2.0  =>  12.0
resultado_exp1 = valor_x + valor_y / valor_z
print(f"\nExpressão 1: {valor_x} + {valor_y} / {valor_z} = {resultado_exp1}") # Esperado: 12.0

# Expressão 2: (x + y) / z
# Ordem: Parênteses (x+y) primeiro, depois Divisão (resultado_soma / z)
# (10.0 + 4.0) / 2.0  =>  14.0 / 2.0  =>  7.0
resultado_exp2 = (valor_x + valor_y) / valor_z
print(f"Expressão 2: ({valor_x} + {valor_y}) / {valor_z} = {resultado_exp2}") # Esperado: 7.0

# Expressão 3: x ** z - y + w * x  (Usando x=10, z=2, y=4, w=3)
# No material [1], Figura 21, parece que os valores são diferentes para estas expressões
# mas vamos usar os nossos para consistência.
# 10.0**2.0 - 4.0 + 3.0 * 10.0
# Ordem:
# 1. Exponenciação: 10.0 ** 2.0 = 100.0
#    Expressão se torna: 100.0 - 4.0 + 3.0 * 10.0
# 2. Multiplicação: 3.0 * 10.0 = 30.0
#    Expressão se torna: 100.0 - 4.0 + 30.0
# 3. Subtração (da esquerda para direita): 100.0 - 4.0 = 96.0
#    Expressão se torna: 96.0 + 30.0
# 4. Adição: 96.0 + 30.0 = 126.0
resultado_exp3 = valor_x ** valor_z - valor_y + valor_w * valor_x
print(f"Expressão 3: {valor_x}**{valor_z} - {valor_y} + {valor_w}*{valor_x} = {resultado_exp3}") # Esperado: 126.0

# Expressão 4: (x ** z) - (y + w) * x
# (10.0 ** 2.0) - (4.0 + 3.0) * 10.0
# Ordem:
# 1. Parênteses e Exponenciação interna: (10.0 ** 2.0) = 100.0
# 2. Parênteses interno: (4.0 + 3.0) = 7.0
#    Expressão se torna: 100.0 - 7.0 * 10.0
# 3. Multiplicação: 7.0 * 10.0 = 70.0
#    Expressão se torna: 100.0 - 70.0
# 4. Subtração: 100.0 - 70.0 = 30.0
resultado_exp4 = (valor_x ** valor_z) - (valor_y + valor_w) * valor_x
print(f"Expressão 4: ({valor_x}**{valor_z}) - ({valor_y}+{valor_w})*{valor_x} = {resultado_exp4}") # Esperado: 30.0

# A Figura 22 do material do curso [1] mostra as saídas para as expressões
# definidas na Figura 21. Os resultados aqui devem ser consistentes com a ordem PEMDAS.

# Parte 2: Estruturas Condicionais `if` e `else` (Baseado nas Figuras 23 e 24 [1])
# Permitem executar blocos de código diferentes com base em uma condição.

print("\n--- Parte 2: Estruturas Condicionais `if` e `else` ---")

# Exemplo 1: Verificação de aprovação por nota
# Vamos pedir a nota ao usuário para tornar interativo.
try:
    nota_aluno_str = input("Digite a nota do aluno (ex: 7.5): ")
    nota_aluno = float(nota_aluno_str) # Converte a entrada para float

    if nota_aluno >= 7.0:
        situacao = "Aprovado(a)"
        mensagem_feedback = f"Parabéns, {situacao} com nota {nota_aluno:.1f}!"
    else:
        situacao = "Reprovado(a)"
        mensagem_feedback = f"Infelizmente, {situacao} com nota {nota_aluno:.1f}. Estude mais!"

    print(mensagem_feedback)

except ValueError:
    print("Entrada inválida. Por favor, digite um número para a nota.")

# Exemplo 2: Verificação de maioridade
try:
    idade_str = input("\nDigite sua idade: ")
    idade = int(idade_str) # Converte a entrada para inteiro

    if idade >= 18:
        print(f"Com {idade} anos, você é maior de idade.")
    else:
        print(f"Com {idade} anos, você é menor de idade.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro para a idade.")

# A Figura 24 do material do curso [1] ilustra as saídas para diferentes entradas
# no exemplo de aprovação por nota.

print("\n--- Fim do Exercício 8 ---")
