# 02-sintaxe-basica-python/exercicios/02_tipos_implicitos_e_reatribuicao.py

"""
Exercício 2: Tipos de Dados Implícitos e Reatribuição de Valores

Objetivo:
Demonstrar como o Python infere (define implicitamente) os tipos de dados
das variáveis no momento da atribuição e como é possível reatribuir
valores de tipos diferentes à mesma variável.
Este exercício é baseado nas Figuras 6, 7, 8 e 9 do material do curso [1].
"""

print("--- Demonstração de Tipos Implícitos e Reatribuição ---")

# Parte 1: Tipos de Dados Implícitos (Baseado nas Figuras 6 e 7 [1])
# Em Python, você não precisa declarar o tipo da variável.
# O tipo é determinado automaticamente pelo valor que você atribui.

print("\n--- Parte 1: Tipos de Dados Implícitos ---")
# Declarando variáveis com diferentes tipos de dados, como na Figura 6 [1]
var_nome = "Maria Clara"      # Python infere que var_nome é do tipo string (str)
var_idade = 30                # Python infere que var_idade é do tipo inteiro (int)
var_salario = 4500.75         # Python infere que var_salario é do tipo float
var_tem_filhos = False        # Python infere que var_tem_filhos é do tipo booleano (bool)

# Imprimindo os valores e seus tipos (similar à saída da Figura 7 [1])
print(f"Variável 'var_nome': Valor = '{var_nome}', Tipo = {type(var_nome)}")
print(f"Variável 'var_idade': Valor = {var_idade}, Tipo = {type(var_idade)}")
print(f"Variável 'var_salario': Valor = {var_salario}, Tipo = {type(var_salario)}")
print(f"Variável 'var_tem_filhos': Valor = {var_tem_filhos}, Tipo = {type(var_tem_filhos)}")


# Parte 2: Reatribuição de Valores e Tipos (Baseado nas Figuras 8 e 9 [1])
# Uma variável em Python pode receber um novo valor, e esse novo valor pode ser
# de um tipo diferente do valor original.

print("\n--- Parte 2: Reatribuição de Valores e Tipos ---")
dado_variavel = "Texto inicial"
print(f"1. 'dado_variavel': Valor = '{dado_variavel}', Tipo = {type(dado_variavel)}")

# Reatribuindo um valor inteiro à mesma variável
dado_variavel = 12345
print(f"2. 'dado_variavel' (após reatribuição para int): Valor = {dado_variavel}, Tipo = {type(dado_variavel)}")
# Se imprimíssemos `dado_variavel` neste ponto, a saída seria 12345, como na Figura 9 [1]
# para o exemplo do "primeiro_nome".

# Reatribuindo um valor float
dado_variavel = 98.6
print(f"3. 'dado_variavel' (após reatribuição para float): Valor = {dado_variavel}, Tipo = {type(dado_variavel)}")

# Reatribuindo um valor booleano
dado_variavel = True
print(f"4. 'dado_variavel' (após reatribuição para bool): Valor = {dado_variavel}, Tipo = {type(dado_variavel)}")

# O material do curso [1] (Figura 8) mostra:
# primeiro_nome = "Eduardo"
# print(primeiro_nome) # Saída: Eduardo
# primeiro_nome = 123456
# print(primeiro_nome) # Saída: 123456 (Figura 9)
# Isso acontece porque o programa é executado linha por linha, e o `print()`
# sempre exibe o valor mais recente da variável.

print("\n--- Demonstração do Fluxo de Execução com Reatribuição (Similar Figuras 8-9) ---")
variavel_fluxo = "Primeiro Valor (String)"
print(f"Antes da primeira reatribuição: {variavel_fluxo}")

variavel_fluxo = 2024 # Reatribuição para inteiro
print(f"Após a primeira reatribuição (para int): {variavel_fluxo}")

variavel_fluxo = "Terceiro Valor (Outra String)" # Reatribuição para string novamente
print(f"Após a segunda reatribuição (para string): {variavel_fluxo}")

# Cada print reflete o estado da variável naquele ponto da execução.

print("\n--- Fim do Exercício 2 ---")
