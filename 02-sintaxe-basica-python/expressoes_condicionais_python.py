# 02-sintaxe-basica-python/expressoes_condicionais_python.py

"""
Módulo de Demonstração: Expressões e Estruturas Condicionais em Python

Este arquivo explora a construção de expressões matemáticas, a ordem de
precedência dos operadores (PEMDAS), e as estruturas condicionais básicas
`if` e `else` em Python.
O conteúdo é baseado na Seção 2.3 e nas Figuras 21 a 24 do material do curso [1].
"""

print("--- Demonstração de Expressões e Condicionais ---")

# 1. Expressões e Ordem de Precedência (PEMDAS)
# (Baseado nas Figuras 21 e 22 de [1])
# Expressões são combinações de valores, variáveis e operadores que Python
# pode avaliar para produzir um resultado.
# A ordem de precedência determina quais operações são realizadas primeiro
# em uma expressão complexa. A sigla PEMDAS ajuda a lembrar a ordem:
# P - Parênteses ()
# E - Exponenciação (**)
# M - Multiplicação (*)
# D - Divisão (/) (e também //, %)
# A - Adição (+)
# S - Subtração (-)
# Multiplicação e Divisão têm a mesma precedência e são avaliadas da esquerda para a direita.
# Adição e Subtração têm a mesma precedência e são avaliadas da esquerda para a direita.

print("\n--- 1. Expressões e Ordem de Precedência (PEMDAS) ---")

# Exemplo 1 (da Figura 21 [1], adaptado para ter variáveis)
a = 10
b = 5
c = 2
d = 3

# Expressão sem parênteses (para ilustrar a ordem padrão)
resultado_sem_parenteses = a + b * c # Multiplicação (b*c) primeiro, depois adição
# 10 + (5 * 2) = 10 + 10 = 20
print(f"Expressão: {a} + {b} * {c}")
print(f"Resultado (sem parênteses, b*c primeiro): {resultado_sem_parenteses}")

# Expressão com parênteses (para alterar a ordem)
resultado_com_parenteses = (a + b) * c # Adição (a+b) primeiro, depois multiplicação
# (10 + 5) * 2 = 15 * 2 = 30
print(f"Expressão: ({a} + {b}) * {c}")
print(f"Resultado (com parênteses, a+b primeiro): {resultado_com_parenteses}")

# Exemplo mais complexo da Figura 21 [1]:
# Nota: As variáveis da Figura 21 são valor_a, valor_b, valor_c.
# Vamos usar a, b, c, d que já temos.
# Expressao_1 = valor_a + valor_b / valor_c
# Expressao_2 = (valor_a + valor_b) / valor_c
# Expressao_3 = valor_a ** valor_b - valor_c + valor_d * valor_a
# Expressao_4 = (valor_a ** valor_b) - (valor_c + valor_d) * valor_a

# Usando nossas variáveis a=10, b=5, c=2, d=3:
expressao_1_fig21 = a + b / c  # 10 + 5 / 2  = 10 + 2.5 = 12.5 (Divisão primeiro)
expressao_2_fig21 = (a + b) / c # (10 + 5) / 2 = 15 / 2 = 7.5 (Parênteses primeiro)

# Para Expressao_3 e Expressao_4, vamos usar valores menores para exponenciação
# Digamos a=2, b=3, c=4, d=1
val_x = 2
val_y = 3
val_z = 4
val_w = 1

expressao_3_fig21 = val_x ** val_y - val_z + val_w * val_x
# 2**3 - 4 + 1 * 2
# 8 - 4 + 1 * 2 (Exponenciação primeiro)
# 8 - 4 + 2     (Multiplicação depois)
# 4 + 2         (Subtração da esquerda para direita)
# 6             (Adição final)

expressao_4_fig21 = (val_x ** val_y) - (val_z + val_w) * val_x
# (2**3) - (4 + 1) * 2
# 8 - (4 + 1) * 2 (Parênteses e exponenciação)
# 8 - 5 * 2       (Parênteses interno)
# 8 - 10          (Multiplicação)
# -2              (Subtração)

print(f"\nExemplos da Figura 21 [1] adaptados:")
print(f"Expressao_1 ({a} + {b} / {c}): {expressao_1_fig21}")
print(f"Expressao_2 (({a} + {b}) / {c}): {expressao_2_fig21}")
print(f"Expressao_3 ({val_x}**{val_y} - {val_z} + {val_w}*{val_x}): {expressao_3_fig21}")
print(f"Expressao_4 (({val_x}**{val_y}) - ({val_z}+{val_w})*{val_x}): {expressao_4_fig21}")
# A Figura 22 [1] mostra as saídas, que devem corresponder a estes cálculos.

# O material do curso [1] enfatiza: "sem o respeito da ordem de execução dos cálculos
# dentro de uma expressão matemática, o resultado apresentado pode não ser o que esperamos."


# 2. Estruturas Condicionais: `if` e `else`
# (Baseado nas Figuras 23 e 24 de [1])
# Permitem que o programa execute diferentes blocos de código com base
# em uma condição ser verdadeira (True) ou falsa (False).

print("\n--- 2. Estruturas Condicionais: `if` e `else` ---")

# Exemplo da Figura 23 [1]: Aprovação por nota
nota_aluno = float(input("Digite a nota do aluno (0 a 10): ")) # Lê a nota como float

# A estrutura `if` testa uma condição.
# Se a condição for True, o bloco de código indentado abaixo do `if` é executado.
if nota_aluno >= 7.0:
    situacao = "Aprovado"
    print(f"Parabéns! Com nota {nota_aluno:.1f}, você está {situacao}.")
    # Pode haver múltiplas linhas de código aqui
# A estrutura `else` é opcional.
# Se a condição do `if` for False, o bloco de código indentado abaixo do `else` é executado.
else:
    situacao = "Reprovado"
    print(f"Que pena! Com nota {nota_aluno:.1f}, você está {situacao}.")
    print("Estude mais para a próxima!")

# A Figura 24 [1] mostra exemplos de saída para diferentes notas.

# Outro exemplo simples:
idade_para_votar = 16
idade_pessoa = int(input("\nDigite sua idade: "))

if idade_pessoa >= idade_para_votar:
    print("Você já pode (ou deve) votar!")
else:
    diferenca_idade = idade_para_votar - idade_pessoa
    print(f"Você ainda não pode votar. Faltam {diferenca_idade} ano(s).")


# Condicionais podem ser aninhadas (um if dentro de outro if ou else),
# e podemos usar `elif` (else if) para testar múltiplas condições em sequência.
# Embora o material [1] nesta seção foque em `if` e `else`, `elif` é uma extensão natural.
print("\n--- Exemplo com `if-elif-else` (conceito adicional) ---")
temperatura_celsius = 25

if temperatura_celsius < 0:
    print("Congelando!")
elif temperatura_celsius < 15: # Se não for < 0, testa se é < 15
    print("Está frio.")
elif temperatura_celsius < 28: # Se não for < 15, testa se é < 28
    print("Temperatura agradável.")
else: # Se nenhuma das condições anteriores for verdadeira (>= 28)
    print("Está calor!")


print("\n--- Fim da Demonstração de Expressões e Condicionais ---")

