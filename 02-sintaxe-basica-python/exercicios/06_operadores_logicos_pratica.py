# 02-sintaxe-basica-python/exercicios/06_operadores_logicos_pratica.py

"""
Exercício 6: Prática com Operadores Lógicos

Objetivo:
Aplicar os operadores lógicos `and`, `or` e `not` para combinar ou inverter
expressões booleanas, compreendendo suas tabelas verdade.
Este exercício é baseado nas Figuras 17 e 18 do material do curso [1].
"""

print("--- Prática com Operadores Lógicos ---")

# Variáveis base para os cenários, inspiradas na Figura 17 [1]
idade_cliente = 25
renda_cliente_inicial = 3000.00
idade_minima_aprovacao = 18
renda_minima_aprovacao = 2500.00

print(f"Dados Iniciais: Idade Cliente = {idade_cliente}, Renda Cliente = R${renda_cliente_inicial:.2f}")
print(f"Critérios: Idade Mínima = {idade_minima_aprovacao}, Renda Mínima = R${renda_minima_aprovacao:.2f}")

# Cenário 1: Operador `and`
# Saída verdadeira se AMBAS as condições forem verdadeiras.
# Teste: idade_cliente > idade_minima_aprovacao E renda_cliente_inicial > renda_minima_aprovacao
condicao_idade_ok = (idade_cliente > idade_minima_aprovacao)       # True (25 > 18)
condicao_renda_ok = (renda_cliente_inicial > renda_minima_aprovacao) # True (3000 > 2500)
resultado_and = condicao_idade_ok and condicao_renda_ok
print(f"\nCenário 1 (AND): Idade OK ({condicao_idade_ok}) AND Renda OK ({condicao_renda_ok})? Resultado: {resultado_and}") # Esperado: True (conforme Figura 18 [1])

# Cenário 2: Operador `or`
# Saída verdadeira se AO MENOS UMA das condições for verdadeira.
# No material [1], a renda do cliente é atualizada para um valor inferior para este teste.
renda_cliente_cenario2 = 2000.00
print(f"\nAtualizando Renda Cliente para Cenário 2: R${renda_cliente_cenario2:.2f}")
condicao_renda_cenario2_ok = (renda_cliente_cenario2 > renda_minima_aprovacao) # False (2000 > 2500)
# Teste: idade_cliente > idade_minima_aprovacao OU renda_cliente_cenario2 > renda_minima_aprovacao
resultado_or = condicao_idade_ok or condicao_renda_cenario2_ok
print(f"Cenário 2 (OR): Idade OK ({condicao_idade_ok}) OR Renda Cenário 2 OK ({condicao_renda_cenario2_ok})? Resultado: {resultado_or}") # Esperado: True (conforme Figura 18 [1])

# Cenário 3: Operador `not` e `and`
# O `not` inverte o valor booleano de uma expressão.
# O material [1] para o terceiro teste diz: "...utilizamos o 'and not', invertemos a lógica,
# então o que está à sua direita que a princípio seria falso e geraria uma saída também falsa é invertida,
# o que satisfaz a condição da porta lógica 'AND'..."
# Isso implica uma expressão como: (CondicaoVerdadeira) AND NOT (CondicaoFalsa)
# Vamos usar a renda inicial (R$3000) para este exemplo.
condicao_renda_menor_que_minima = (renda_cliente_inicial < renda_minima_aprovacao) # False (3000 < 2500 é False)
# Teste: idade_cliente > idade_minima_aprovacao AND NOT (renda_cliente_inicial < renda_minima_aprovacao)
resultado_and_not_falso = condicao_idade_ok and not condicao_renda_menor_que_minima
#                       True        and not False
#                       True        and True
#                       True
print(f"\nCenário 3 (AND NOT com condição direita sendo False):")
print(f"  Idade OK ({condicao_idade_ok}) AND NOT (Renda Inicial < Renda Mínima ({condicao_renda_menor_que_minima}))?")
print(f"  Resultado: {resultado_and_not_falso}") # Esperado: True (conforme Figura 18 [1])


# Cenário 4: Operador `not` e `and` (com a condição direita sendo verdadeira)
# O material [1] diz: "...antes colocamos a renda do cliente superior à renda_base e desta forma,
# como utilizamos o 'and not', o que geraria duas entradas verdadeiras e uma saída verdadeira,
# passamos a possuir então uma entrada verdadeira e outra falsa..."
# Isso implica uma expressão como: (CondicaoVerdadeira) AND NOT (CondicaoVerdadeira)
# Usando a renda inicial (R$3000) novamente.
# condicao_renda_ok já é True (renda_cliente_inicial > renda_minima_aprovacao)
# Teste: idade_cliente > idade_minima_aprovacao AND NOT (renda_cliente_inicial > renda_minima_aprovacao)
resultado_and_not_verdadeiro = condicao_idade_ok and not condicao_renda_ok
#                             True        and not True
#                             True        and False
#                             False
print(f"\nCenário 4 (AND NOT com condição direita sendo True):")
print(f"  Idade OK ({condicao_idade_ok}) AND NOT (Renda Inicial > Renda Mínima ({condicao_renda_ok}))?")
print(f"  Resultado: {resultado_and_not_verdadeiro}") # Esperado: False (conforme Figura 18 [1])

# Mais exemplos simples com `not`:
verdade = True
falso = False

print(f"\nOutros exemplos com NOT:")
print(f"not {verdade} = {not verdade}") # False
print(f"not {falso} = {not falso}")   # True


# Operadores lógicos com valores não booleanos (curto-circuito e "truthy/falsy" values)
# Em Python, valores como 0, None, strings vazias, listas vazias são considerados "falsy".
# Outros valores (números não-zero, strings/listas não vazias) são "truthy".

print("\n--- Operadores Lógicos com Valores Não-Booleanos ---")
# `and` retorna o primeiro valor "falsy" ou o último valor "truthy" se todos forem "truthy".
print(f"10 and 20: {10 and 20}")   # 20 (ambos truthy, retorna o último)
print(f"0 and 20: {0 and 20}")     # 0 (0 é falsy, retorna o primeiro falsy)
print(f"'' and 'Olá': {'' and 'Olá'}") # '' (string vazia é falsy)
print(f"'Olá' and '': {'Olá' and ''}") # '' (retorna o falsy)

# `or` retorna o primeiro valor "truthy" ou o último valor "falsy" se todos forem "falsy".
print(f"10 or 20: {10 or 20}")     # 10 (10 é truthy, retorna o primeiro truthy)
print(f"0 or 20: {0 or 20}")       # 20 (0 é falsy, 20 é truthy)
print(f"'' or 'Olá': {'' or 'Olá'}") # 'Olá'
print(f"0 or '': {0 or ''}")       # '' (ambos falsy, retorna o último)


print("\n--- Fim do Exercício 6 ---")
