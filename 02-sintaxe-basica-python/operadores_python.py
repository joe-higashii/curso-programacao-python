# 02-sintaxe-basica-python/operadores_python.py

"""
Módulo de Demonstração: Operadores em Python

Este arquivo explora os diferentes tipos de operadores disponíveis em Python:
Aritméticos, de Comparação, Lógicos e de Identidade.
O conteúdo é baseado na Seção 2.2 ("Operadores") e nas Figuras 12 a 20
do material do curso [1].
"""

print("--- Demonstração de Operadores em Python ---")

# 1. Operadores Aritméticos (Baseado nas Figuras 12, 13 e 14 de [1])
# Realizam operações matemáticas.

print("\n--- 1. Operadores Aritméticos ---")
a = 15
b = 4
c = 5 # Usado para o exemplo da Figura 13

print(f"Valores iniciais: a = {a}, b = {b}, c = {c}")

# Operador de Atribuição (=)
# Atribui um valor a uma variável. Já usado extensivamente.
# Exemplo: variavel = valor

# Operador de Adição (+)
soma = a + b
print(f"{a} + {b} = {soma}")

# Operador de Subtração (-)
subtracao = a - b
print(f"{a} - {b} = {subtracao}")

# Operador de Multiplicação (*)
multiplicacao = a * b
print(f"{a} * {b} = {multiplicacao}")

# Operador de Divisão (/)
# Retorna um resultado float (número real).
divisao = a / b
print(f"{a} / {b} = {divisao}")

# Operador de Divisão Inteira (//)
# Retorna a parte inteira da divisão (resultado inteiro, arredondado para baixo).
divisao_inteira = a // b
print(f"{a} // {b} = {divisao_inteira}")

# Operador de Módulo (%)
# Retorna o resto da divisão.
modulo = a % b
print(f"{a} % {b} = {modulo}")

# Operador de Exponenciação (**)
# Eleva o primeiro operando à potência do segundo.
exponenciacao = a ** b # a elevado a b
print(f"{a} ** {b} = {exponenciacao}")
print(f"2 ** 3 = {2**3}")

# Operadores de Atribuição Aumentada (Exemplos da Figura 13 [1])
# São atalhos para realizar uma operação e atribuir o resultado à mesma variável.
# variavel_a += 2 é equivalente a variavel_a = variavel_a + 2
print("\n--- Operadores de Atribuição Aumentada (com c = 5) ---")
print(f"Valor inicial de c: {c}")
c_original = c # Salvar valor original para resetar entre operações

c += 2  # c = c + 2
print(f"c += 2: {c} (Equivalente a c = c + 2)")
c = c_original # Resetar c

c -= 2  # c = c - 2
print(f"c -= 2: {c} (Equivalente a c = c - 2)")
c = c_original

c *= 2  # c = c * 2
print(f"c *= 2: {c} (Equivalente a c = c * 2)")
c = c_original

c /= 2  # c = c / 2
print(f"c /= 2: {c} (Equivalente a c = c / 2)")
c = c_original

c %= 2  # c = c % 2
print(f"c %= 2: {c} (Equivalente a c = c % 2)")
c = c_original

c //= 2 # c = c // 2
print(f"c //= 2: {c} (Equivalente a c = c // 2)")
c = c_original

c **= 2 # c = c ** 2
print(f"c **= 2: {c} (Equivalente a c = c ** 2)")
# A Figura 14 [1] mostra a saída dessas operações.


# 2. Operadores de Comparação (Baseado nas Figuras 15 e 16 de [1])
# Comparam dois valores e retornam um resultado Booleano (True ou False).

print("\n--- 2. Operadores de Comparação ---")
val_a = 10
val_b = 20
val_c = 10
print(f"Valores para comparação: val_a = {val_a}, val_b = {val_b}, val_c = {val_c}")

# Igual a (==)
# Verifica se dois valores são iguais.
# Cuidado: `=` é atribuição, `==` é comparação.
print(f"{val_a} == {val_b} (val_a é igual a val_b?): {val_a == val_b}")  # False
print(f"{val_a} == {val_c} (val_a é igual a val_c?): {val_a == val_c}")  # True

# Diferente de (!=)
# Verifica se dois valores são diferentes.
print(f"{val_a} != {val_b} (val_a é diferente de val_b?): {val_a != val_b}")  # True
print(f"{val_a} != {val_c} (val_a é diferente de val_c?): {val_a != val_c}")  # False

# Maior que (>)
print(f"{val_a} > {val_b} (val_a é maior que val_b?): {val_a > val_b}")    # False
print(f"{val_b} > {val_a} (val_b é maior que val_a?): {val_b > val_a}")    # True

# Menor que (<)
print(f"{val_a} < {val_b} (val_a é menor que val_b?): {val_a < val_b}")    # True
print(f"{val_b} < {val_a} (val_b é menor que val_a?): {val_b < val_a}")    # False

# Maior ou igual a (>=)
print(f"{val_a} >= {val_c} (val_a é maior ou igual a val_c?): {val_a >= val_c}") # True
print(f"{val_a} >= {val_b} (val_a é maior ou igual a val_b?): {val_a >= val_b}") # False

# Menor ou igual a (<=)
print(f"{val_a} <= {val_c} (val_a é menor ou igual a val_c?): {val_a <= val_c}") # True
print(f"{val_b} <= {val_a} (val_b é menor ou igual a val_a?): {val_b <= val_a}") # False
# A Figura 16 [1] mostra a saída dessas comparações.


# 3. Operadores Lógicos (Baseado nas Figuras 17 e 18 de [1])
# Usados para combinar expressões Booleanas. Retornam True ou False.
# Operadores principais: `and`, `or`, `not`.

print("\n--- 3. Operadores Lógicos ---")
# Exemplo conceitual da Figura 17 [1]:
idade_cliente = 25
renda_cliente = 3000
idade_base = 18
renda_base = 2500

print(f"Dados do cliente: Idade = {idade_cliente}, Renda = {renda_cliente}")
print(f"Critérios base: Idade Base = {idade_base}, Renda Base = {renda_base}")

# Operador `and` (E lógico)
# Retorna True se AMBAS as condições forem verdadeiras.
aprovado_credito_and = (idade_cliente > idade_base) and (renda_cliente > renda_base)
print(f"({idade_cliente} > {idade_base}) AND ({renda_cliente} > {renda_base})? Resultado: {aprovado_credito_and}") # True

# Operador `or` (OU lógico)
# Retorna True se PELO MENOS UMA das condições for verdadeira.
tem_algum_beneficio_or = (idade_cliente > 60) or (renda_cliente < 1500)
print(f"({idade_cliente} > 60) OR ({renda_cliente} < 1500)? Resultado: {tem_algum_beneficio_or}") # False

# Operador `not` (NÃO lógico)
# Inverte o valor Booleano de uma expressão.
nao_e_jovem = not (idade_cliente < 30)
print(f"NOT ({idade_cliente} < 30)? Resultado: {nao_e_jovem}") # False (pois idade_cliente < 30 é True)

# O material do curso [1] (Figuras 17-18) tem exemplos mais complexos:
print("\n--- Exemplos da Figura 17 [1] ---")
# Cenário 1: idade > idade_base E renda > renda_base
# idade_cliente = 25, idade_base = 18 -> True
# renda_cliente = 3000, renda_base = 2500 -> True
# Resultado: True AND True -> True
print(f"Teste 1 (AND): {(idade_cliente > idade_base) and (renda_cliente > renda_base)}")

# Cenário 2: Atualiza renda_cliente para 2000. Teste OR.
renda_cliente_cenario2 = 2000
# idade_cliente = 25, idade_base = 18 -> True
# renda_cliente_cenario2 = 2000, renda_base = 2500 -> False
# Resultado: True OR False -> True
print(f"Teste 2 (OR, renda={renda_cliente_cenario2}): {(idade_cliente > idade_base) or (renda_cliente_cenario2 > renda_base)}")

# Cenário 3: "and not". O material diz: "o que está à sua direita que a princípio seria falso e geraria uma saída também falsa é invertida"
# Expressão: (idade_cliente > idade_base) and not (renda_cliente > renda_base)
# Mantendo renda_cliente = 3000
# (idade_cliente > idade_base) -> True
# (renda_cliente > renda_base) -> True
# not (renda_cliente > renda_base) -> not True -> False
# Resultado: True AND False -> False
# O texto do anexo [1] para o terceiro teste parece ter uma interpretação confusa do `and not`.
# Vamos seguir a lógica padrão:
# "(idade_cliente > idade_base)" é True.
# "(renda_base > renda_cliente)" é False. (No exemplo da Figura 17, parece ser "renda_base > RENDA_CLIENTE")
# Se for `(idade_cliente > idade_base) and not (renda_base > renda_cliente)`:
# `not (renda_base > renda_cliente)` (i.e., `not (2500 > 3000)`) -> `not False` -> `True`.
# Então seria `True and True` -> `True`.
# Se for `(idade_cliente > idade_base) and not (renda_cliente > renda_base)`:
# `not (renda_cliente > renda_base)` (i.e., `not (3000 > 2500)`) -> `not True` -> `False`.
# Então seria `True and False` -> `False`.
# O texto da figura 17/18 diz: "o cliente possui idade maior que 18 anos, porém, quando usamos o 'and not', invertemos a lógica,
# então o que está à sua direita que a princípio seria falso e geraria uma saída também falsa é invertida,
# o que satisfaz a condição da porta lógica “AND”em termos de duas entradas verdadeiras para termos uma saída verdadeira."
# Isso sugere que a condição à direita do `not` era originalmente Falsa, e o `not` a torna Verdadeira.
# Exemplo que se encaixa nessa descrição: (idade_cliente > idade_base) and not (renda_cliente < renda_base)
# (True) and not (3000 < 2500 -> False) -> True and not False -> True and True -> True
condicao_direita_originalmente_falsa = (renda_cliente < renda_base) # False
teste3_fig17 = (idade_cliente > idade_base) and not condicao_direita_originalmente_falsa
print(f"Teste 3 (AND NOT, com direita sendo False): {teste3_fig17}")

# Cenário 4: "antes colocamos a renda do cliente superior à renda_base e desta forma, como utilizamos o 'and not',
# o que geraria duas entradas verdadeiras e uma saída verdadeira, passamos a possuir então uma entrada verdadeira e outra falsa"
# Isso sugere que a condição à direita do `not` era originalmente Verdadeira.
# Exemplo: (idade_cliente > idade_base) and not (renda_cliente > renda_base)
condicao_direita_originalmente_verdadeira = (renda_cliente > renda_base) # True
teste4_fig17 = (idade_cliente > idade_base) and not condicao_direita_originalmente_verdadeira
print(f"Teste 4 (AND NOT, com direita sendo True): {teste4_fig17}")
# A Figura 18 [1] mostra as saídas True, True, True, False para estes cenários, o que
# indica que minha interpretação do Teste 3 e 4 corresponde aos resultados.


# 4. Operadores de Identidade (Baseado nas Figuras 19 e 20 de [1])
# Comparam se dois operandos se referem ao MESMO objeto na memória (não apenas se têm o mesmo valor).
# Operadores: `is`, `is not`.

print("\n--- 4. Operadores de Identidade ---")
# Exemplo com listas (objetos mutáveis) da Figura 19 [1]:
lista_1 = [10, 20, 30]
lista_2 = [10, 20, 30] # Mesmo conteúdo, mas objeto diferente
lista_3 = [40, 50, 60]
lista_4 = lista_1      # lista_4 agora referencia o MESMO objeto que lista_1

print(f"lista_1: {lista_1}, id: {id(lista_1)}")
print(f"lista_2: {lista_2}, id: {id(lista_2)}") # id diferente de lista_1
print(f"lista_3: {lista_3}, id: {id(lista_3)}")
print(f"lista_4: {lista_4}, id: {id(lista_4)}") # id IGUAL ao de lista_1

# Operador `is`
# Retorna True se ambos os operandos são o mesmo objeto.
print(f"lista_1 is lista_2? {lista_1 is lista_2}")  # False (conteúdo igual, mas objetos diferentes)
print(f"lista_1 is lista_4? {lista_1 is lista_4}")  # True (referenciam o mesmo objeto)

# Operador `is not`
# Retorna True se os operandos não são o mesmo objeto.
print(f"lista_1 is not lista_2? {lista_1 is not lista_2}") # True
print(f"lista_1 is not lista_3? {lista_1 is not lista_3}") # True
print(f"lista_1 is not lista_4? {lista_1 is not lista_4}") # False

# O material [1] na Figura 19 usa os termos "mesmo_objeto" e "objeto_diferente"
# para os resultados dos testes "lista_1 is lista_2" e "lista_1 is not lista_3".
# O resultado esperado na Figura 20 é True e True.
# "lista_1 is lista_2" -> A Figura 20 diz que é True. Isso é inesperado para listas,
# a menos que Python esteja otimizando pequenas listas ou se `lista_2 = lista_1`.
# No entanto, a descrição do material diz: "verificamos se na 'lista_1' possuímos itens presentes na 'lista_2'".
# Isso soa mais como uma verificação de conteúdo, não de identidade.
# O operador `is` verifica IDENTIDADE, não igualdade de conteúdo. `==` verifica igualdade de conteúdo.
# Vamos seguir a definição correta de `is`. Se o anexo implica outra coisa, é uma imprecisão.
# Para que `lista_1 is lista_2` seja `True`, `lista_2` teria que ser `lista_1` ou uma cópia que Python otimiza
# para o mesmo objeto (raro para listas mutáveis, mais comum para inteiros pequenos e strings).
# A Figura 20 mostrando True para `mesmo_objeto = lista_1 is lista_2` é peculiar se `lista_1` e `lista_2`
# foram criadas independentemente como `[10,20,30]`. É mais provável se `lista_2 = lista_1`.

# Se o exemplo do anexo fosse:
# lista_x = [1, 2]
# lista_y = [1, 2]
# lista_z = lista_x
# print(f"lista_x is lista_y: {lista_x is lista_y}") # Geralmente False
# print(f"lista_x is lista_z: {lista_x is lista_z}") # True

# Para inteiros pequenos, Python frequentemente reutiliza objetos:
num1 = 256
num2 = 256
print(f"num1 ({num1}) is num2 ({num2})? {num1 is num2}") # Provavelmente True para inteiros pequenos

num_grande1 = 1000
num_grande2 = 1000
print(f"num_grande1 ({num_grande1}) is num_grande2 ({num_grande2})? {num_grande1 is num_grande2}") # Pode ser False

str1 = "python"
str2 = "python"
print(f"str1 ('{str1}') is str2 ('{str2}')? {str1 is str2}") # Provavelmente True (interning de strings)

print("\n--- Fim da Demonstração de Operadores ---")
