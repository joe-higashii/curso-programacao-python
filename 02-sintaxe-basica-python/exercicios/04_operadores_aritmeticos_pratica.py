# 02-sintaxe-basica-python/exercicios/04_operadores_aritmeticos_pratica.py

"""
Exercício 4: Prática com Operadores Aritméticos

Objetivo:
Aplicar os operadores aritméticos do Python para realizar cálculos e entender
seu funcionamento, incluindo os operadores de atribuição aumentada.
Este exercício é baseado nas Figuras 12, 13 e 14 do material do curso [1].
"""

print("--- Prática com Operadores Aritméticos ---")

# Parte 1: Operadores Aritméticos Básicos (Conceito da Figura 12 [1])
# A Figura 12 [1] apresenta os operadores, mas não os executa com `print`.
# Vamos definir algumas variáveis e aplicar os operadores.
num_x = 20
num_y = 7

print(f"\n--- Parte 1: Operadores Aritméticos Básicos (num_x = {num_x}, num_y = {num_y}) ---")

# Adição (+)
resultado_soma = num_x + num_y
print(f"{num_x} + {num_y} = {resultado_soma}")

# Subtração (-)
resultado_subtracao = num_x - num_y
print(f"{num_x} - {num_y} = {resultado_subtracao}")

# Multiplicação (*)
resultado_multiplicacao = num_x * num_y
print(f"{num_x} * {num_y} = {resultado_multiplicacao}")

# Divisão (/) - sempre retorna float
resultado_divisao = num_x / num_y
print(f"{num_x} / {num_y} = {resultado_divisao}")

# Divisão Inteira (//) - retorna a parte inteira
resultado_divisao_inteira = num_x // num_y
print(f"{num_x} // {num_y} = {resultado_divisao_inteira}")

# Módulo (%) - retorna o resto da divisão
resultado_modulo = num_x % num_y
print(f"{num_x} % {num_y} = {resultado_modulo}")

# Exponenciação (**)
base = 2
expoente = 5
resultado_exponenciacao = base ** expoente # 2 elevado a 5
print(f"{base} ** {expoente} = {resultado_exponenciacao}")


# Parte 2: Operadores de Atribuição Aumentada (Baseado nas Figuras 13 e 14 [1])
# A Figura 13 [1] usa `variavel_a` inicializada com 5 e aplica operadores de atribuição aumentada.
# A Figura 14 [1] mostra a saída dessas operações.

print("\n--- Parte 2: Operadores de Atribuição Aumentada ---")
variavel_a = 5
print(f"Valor inicial de variavel_a = {variavel_a}")

# += (Adição e atribuição)
# variavel_a += 2  é o mesmo que variavel_a = variavel_a + 2
variavel_a_original = variavel_a # Guardar para resetar
variavel_a += 2
print(f"Após variavel_a += 2: variavel_a = {variavel_a}") # Esperado: 7
variavel_a = variavel_a_original # Resetar

# -= (Subtração e atribuição)
# variavel_a -= 2 é o mesmo que variavel_a = variavel_a - 2
variavel_a -= 2
print(f"Após variavel_a -= 2: variavel_a = {variavel_a}") # Esperado: 3
variavel_a = variavel_a_original # Resetar

# *= (Multiplicação e atribuição)
# variavel_a *= 2 é o mesmo que variavel_a = variavel_a * 2
variavel_a *= 2
print(f"Após variavel_a *= 2: variavel_a = {variavel_a}") # Esperado: 10
variavel_a = variavel_a_original # Resetar

# /= (Divisão e atribuição)
# variavel_a /= 2 é o mesmo que variavel_a = variavel_a / 2
variavel_a /= 2
print(f"Após variavel_a /= 2: variavel_a = {variavel_a}") # Esperado: 2.5
variavel_a = variavel_a_original # Resetar

# %= (Módulo e atribuição)
# variavel_a %= 2 é o mesmo que variavel_a = variavel_a % 2
variavel_a %= 2
print(f"Após variavel_a %= 2: variavel_a = {variavel_a}") # Esperado: 1 (5 % 2)
variavel_a = variavel_a_original # Resetar

# //= (Divisão inteira e atribuição)
# variavel_a //= 2 é o mesmo que variavel_a = variavel_a // 2
variavel_a //= 2
print(f"Após variavel_a //= 2: variavel_a = {variavel_a}") # Esperado: 2 (5 // 2)
variavel_a = variavel_a_original # Resetar

# **= (Exponenciação e atribuição)
# variavel_a **= 2 é o mesmo que variavel_a = variavel_a ** 2
variavel_a **= 2
print(f"Após variavel_a **= 2: variavel_a = {variavel_a}") # Esperado: 25 (5 ** 2)
variavel_a = variavel_a_original # Resetar

# As saídas devem corresponder à Figura 14 do material do curso [1].

print("\n--- Fim do Exercício 4 ---")
