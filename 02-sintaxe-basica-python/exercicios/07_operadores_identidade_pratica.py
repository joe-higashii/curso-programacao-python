# 02-sintaxe-basica-python/exercicios/07_operadores_identidade_pratica.py

"""
Exercício 7: Prática com Operadores de Identidade

Objetivo:
Entender e aplicar os operadores de identidade `is` e `is not` para
verificar se duas variáveis se referem ao mesmo objeto na memória.
Este exercício é baseado nas Figuras 19 e 20 do material do curso [1].

Importante:
Os operadores de identidade (`is`, `is not`) comparam a IDENTIDADE dos objetos
(se são o mesmo objeto na memória, verificado pelo `id()` da variável).
Eles são DIFERENTES dos operadores de igualdade (`==`, `!=`) que comparam
o VALOR dos objetos.
"""

print("--- Prática com Operadores de Identidade ---")

# Cenário com Listas (Objetos Mutáveis)
# Como no material [1], Figura 19.
lista_a = [1, 2, 3]
lista_b = [1, 2, 3]  # Mesmo conteúdo, mas é um objeto diferente na memória.
lista_c = [4, 5, 6]
lista_d = lista_a    # lista_d agora aponta para o MESMO objeto que lista_a.

print("\n--- Cenário com Listas ---")
print(f"Conteúdo: lista_a = {lista_a}, lista_b = {lista_b}, lista_c = {lista_c}, lista_d = {lista_d}")
print(f"IDs: ")
print(f"  id(lista_a): {id(lista_a)}")
print(f"  id(lista_b): {id(lista_b)}") # Geralmente diferente de id(lista_a)
print(f"  id(lista_c): {id(lista_c)}")
print(f"  id(lista_d): {id(lista_d)}") # Deve ser IGUAL a id(lista_a)

# Operador `is`
print("\nUsando operador 'is':")
# Verifica se lista_a e lista_b são o mesmo objeto.
# Embora tenham o mesmo conteúdo, são objetos distintos em memória.
mesmo_objeto_ab = (lista_a is lista_b)
print(f"lista_a is lista_b (são o mesmo objeto?): {mesmo_objeto_ab}") # Esperado: False

# Verifica se lista_a e lista_d são o mesmo objeto.
# Como lista_d = lista_a, elas apontam para o mesmo local na memória.
mesmo_objeto_ad = (lista_a is lista_d)
print(f"lista_a is lista_d (são o mesmo objeto?): {mesmo_objeto_ad}") # Esperado: True

# Operador `is not`
print("\nUsando operador 'is not':")
# Verifica se lista_a e lista_b NÃO são o mesmo objeto.
objeto_diferente_ab = (lista_a is not lista_b)
print(f"lista_a is not lista_b (NÃO são o mesmo objeto?): {objeto_diferente_ab}") # Esperado: True

# Verifica se lista_a e lista_c NÃO são o mesmo objeto.
objeto_diferente_ac = (lista_a is not lista_c)
print(f"lista_a is not lista_c (NÃO são o mesmo objeto?): {objeto_diferente_ac}") # Esperado: True

# Verifica se lista_a e lista_d NÃO são o mesmo objeto.
objeto_diferente_ad = (lista_a is not lista_d)
print(f"lista_a is not lista_d (NÃO são o mesmo objeto?): {objeto_diferente_ad}") # Esperado: False


# Observação sobre a Figura 20 do material do curso [1]:
# A Figura 20 mostra a saída `True` para `mesmo_objeto = lista_1 is lista_2`
# e `True` para `objeto_diferente = lista_1 is not lista_3`.
# A saída `True` para `lista_1 is lista_2` seria correta APENAS se `lista_2` fosse
# uma referência direta a `lista_1` (ex: `lista_2 = lista_1`) ou em casos raros de
# otimização interna do Python com certos tipos imutáveis e pequenos.
# Para listas criadas independentemente como `[10,20,30]`, `is` normalmente retorna `False`.
# O texto do material [1] na descrição da Figura 19/20 diz:
# "através do 'is', verificamos se na 'lista_1' possuímos itens presentes na 'lista_2'".
# Esta descrição está INCORRETA para o operador `is`. `is` não verifica se itens
# estão presentes; ele verifica se as duas variáveis apontam para o EXATO mesmo objeto.
# Para verificar se itens estão presentes, usaríamos o operador `in` ou comparações de conteúdo.
# Para verificar se o CONTEÚDO é igual, usaríamos `lista_1 == lista_2`.

print("\n--- Comparando Identidade (is) vs Igualdade de Conteúdo (==) ---")
print(f"lista_a ({lista_a}) == lista_b ({lista_b}) (Conteúdo igual?): {lista_a == lista_b}") # True
print(f"lista_a ({lista_a}) is lista_b ({lista_b}) (Mesmo objeto?): {lista_a is lista_b}")   # False (geralmente)

print(f"lista_a ({lista_a}) == lista_d ({lista_d}) (Conteúdo igual?): {lista_a == lista_d}") # True
print(f"lista_a ({lista_a}) is lista_d ({lista_d}) (Mesmo objeto?): {lista_a is lista_d}")   # True


# Cenário com Tipos Imutáveis Pequenos (onde Python pode otimizar)
print("\n--- Cenário com Inteiros Pequenos e Strings ---")
int_a = 5
int_b = 5
# Python frequentemente reutiliza objetos para inteiros pequenos (-5 a 256)
print(f"int_a = {int_a} (id: {id(int_a)}), int_b = {int_b} (id: {id(int_b)})")
print(f"int_a is int_b? {int_a is int_b}") # Provavelmente True

int_c = 1000
int_d = 1000
# Para inteiros maiores, a reutilização de objetos é menos garantida
print(f"int_c = {int_c} (id: {id(int_c)}), int_d = {int_d} (id: {id(int_d)})")
print(f"int_c is int_d? {int_c is int_d}") # Pode ser True ou False dependendo da implementação do Python

str_a = "exemplo"
str_b = "exemplo"
# Python também faz "interning" de strings, reutilizando objetos para strings idênticas.
print(f"str_a = '{str_a}' (id: {id(str_a)}), str_b = '{str_b}' (id: {id(str_b)})")
print(f"str_a is str_b? {str_a is str_b}") # Provavelmente True

# O `is` é particularmente útil quando se trabalha com o valor singleton `None`:
var_none_1 = None
var_none_2 = None
print(f"\nvar_none_1 is None? {var_none_1 is None}") # True
print(f"var_none_1 is var_none_2? {var_none_1 is var_none_2}") # True

print("\n--- Fim do Exercício 7 ---")
