# 02-sintaxe-basica-python/exercicios/05_operadores_comparacao_pratica.py

"""
Exercício 5: Prática com Operadores de Comparação

Objetivo:
Utilizar os operadores de comparação do Python para comparar valores e
observar os resultados booleanos (True ou False).
Este exercício é baseado nas Figuras 15 e 16 do material do curso [1].
"""

print("--- Prática com Operadores de Comparação ---")

# Inicialização das variáveis, como na Figura 15 [1]
# No material, as variáveis são nomeadas variavel_a e variavel_b.
# Vamos usar nomes diferentes para clareza neste script.
num1 = 10
num2 = 20
num3 = 10 # Para testar igualdade e desigualdade com num1

print(f"Valores para comparação: num1 = {num1}, num2 = {num2}, num3 = {num3}")

# 1. Operador de Igualdade (==)
# Verifica se num1 é igual a num2.
resultado_igual_1_2 = (num1 == num2)
print(f"\n{num1} == {num2} (num1 é igual a num2?): {resultado_igual_1_2}") # Esperado: False

# Verifica se num1 é igual a num3.
resultado_igual_1_3 = (num1 == num3)
print(f"{num1} == {num3} (num1 é igual a num3?): {resultado_igual_1_3}") # Esperado: True

# 2. Operador de Diferença (!=)
# Verifica se num1 é diferente de num2.
resultado_diferente_1_2 = (num1 != num2)
print(f"\n{num1} != {num2} (num1 é diferente de num2?): {resultado_diferente_1_2}") # Esperado: True

# Verifica se num1 é diferente de num3.
resultado_diferente_1_3 = (num1 != num3)
print(f"{num1} != {num3} (num1 é diferente de num3?): {resultado_diferente_1_3}") # Esperado: False

# 3. Operador Menor que (<)
# Verifica se num1 é menor que num2.
resultado_menor_1_2 = (num1 < num2)
print(f"\n{num1} < {num2} (num1 é menor que num2?): {resultado_menor_1_2}") # Esperado: True

# Verifica se num2 é menor que num1.
resultado_menor_2_1 = (num2 < num1)
print(f"{num2} < {num1} (num2 é menor que num1?): {resultado_menor_2_1}") # Esperado: False

# 4. Operador Maior que (>)
# Verifica se num1 é maior que num2.
resultado_maior_1_2 = (num1 > num2)
print(f"\n{num1} > {num2} (num1 é maior que num2?): {resultado_maior_1_2}") # Esperado: False

# Verifica se num2 é maior que num1.
resultado_maior_2_1 = (num2 > num1)
print(f"{num2} > {num1} (num2 é maior que num1?): {resultado_maior_2_1}") # Esperado: True

# 5. Operador Menor ou Igual a (<=)
# Verifica se num1 é menor ou igual a num2.
resultado_menor_igual_1_2 = (num1 <= num2)
print(f"\n{num1} <= {num2} (num1 é menor ou igual a num2?): {resultado_menor_igual_1_2}") # Esperado: True

# Verifica se num1 é menor ou igual a num3 (que é igual a num1).
resultado_menor_igual_1_3 = (num1 <= num3)
print(f"{num1} <= {num3} (num1 é menor ou igual a num3?): {resultado_menor_igual_1_3}") # Esperado: True

# Verifica se num2 é menor ou igual a num1.
resultado_menor_igual_2_1 = (num2 <= num1)
print(f"{num2} <= {num1} (num2 é menor ou igual a num1?): {resultado_menor_igual_2_1}") # Esperado: False

# 6. Operador Maior ou Igual a (>=)
# Verifica se num1 é maior ou igual a num2.
resultado_maior_igual_1_2 = (num1 >= num2)
print(f"\n{num1} >= {num2} (num1 é maior ou igual a num2?): {resultado_maior_igual_1_2}") # Esperado: False

# Verifica se num2 é maior ou igual a num1.
resultado_maior_igual_2_1 = (num2 >= num1)
print(f"{num2} >= {num1} (num2 é maior ou igual a num1?): {resultado_maior_igual_2_1}") # Esperado: True

# Verifica se num1 é maior ou igual a num3 (que é igual a num1).
resultado_maior_igual_1_3 = (num1 >= num3)
print(f"{num1} >= {num3} (num1 é maior ou igual a num3?): {resultado_maior_igual_1_3}") # Esperado: True

# A Figura 16 do material do curso [1] apresenta a saída esperada para
# comparações com variavel_a = 10 e variavel_b = 20.
# Os resultados acima devem estar alinhados com essa saída conceitual.
# Por exemplo, para `variavel_a == variavel_b`, a Figura 16 mostra `False`.
# Para `variavel_a != variavel_b`, mostra `True`.
# Para `variavel_a < variavel_b`, mostra `True`.
# E assim por diante.

print("\n--- Fim do Exercício 5 ---")
