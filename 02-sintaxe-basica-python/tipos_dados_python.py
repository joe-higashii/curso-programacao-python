# 02-sintaxe-basica-python/tipos_dados_python.py

"""
Módulo de Demonstração: Tipos de Dados em Python

Este arquivo explora os tipos de dados fundamentais em Python (Numéricos, Literais, Lógicos),
a tipagem implícita e a reatribuição de valores e tipos a variáveis,
conforme a Seção 2.2 e as Figuras 6 a 9 do material do curso [1].
"""

print("--- Demonstração de Tipos de Dados em Python ---")

# 1. Tipagem Implícita em Python (Baseado na Seção 2.2 e Figuras 6-7 de [1])
# Em Python, não é necessário declarar explicitamente o tipo de uma variável.
# O tipo é inferido (implicitamente definido) pelo interpretador no momento
# da atribuição do valor. Isso é conhecido como tipagem dinâmica.

print("\n--- 1. Tipos de Dados e Tipagem Implícita ---")

# Tipo Numérico: Inteiro (int)
# Armazena números inteiros (sem parte decimal).
# Exemplos do material [1]: Idade = 18, AtributoForca = 15, _FatorCorrecao = 13
idade = 18
quantidade_itens = 150
ano_atual = 2024
print(f"Variável 'idade': Valor = {idade}, Tipo = {type(idade)}")
print(f"Variável 'quantidade_itens': Valor = {quantidade_itens}, Tipo = {type(quantidade_itens)}")

# Tipo Numérico: Real/Ponto Flutuante (float)
# Armazena números com parte decimal.
# Exemplos do material [1]: Altura = 1.70, _JurosSimples = 17.50, JurosCompostos = 19.00
altura = 1.75
preco_produto = 49.99
taxa_conversao = 5.23
print(f"Variável 'altura': Valor = {altura}, Tipo = {type(altura)}")
print(f"Variável 'preco_produto': Valor = {preco_produto}, Tipo = {type(preco_produto)}")

# Tipo Literal: String (str)
# Armazena sequências de caracteres (texto).
# Deve ser delimitado por aspas simples ('...') ou duplas ("...").
# Exemplos do material [1]: Nome = "Eduardo", TituloAplicacao = "Exemplos de Software"
nome_completo = "Alice Wonderland"
mensagem_boas_vindas = 'Bem-vindo ao curso de Python!'
endereco_email = "contato@exemplo.com"
print(f"Variável 'nome_completo': Valor = '{nome_completo}', Tipo = {type(nome_completo)}")
print(f"Variável 'mensagem_boas_vindas': Valor = '{mensagem_boas_vindas}', Tipo = {type(mensagem_boas_vindas)}")

# Tipo Lógico: Booleano (bool)
# Armazena valores de verdade: True (Verdadeiro) ou False (Falso).
# Note que True e False começam com letra maiúscula em Python.
# Exemplos do material [1]: TelaAtiva = True, _ValidarDados = False
login_sucesso = True
tem_permissao = False
maior_de_idade = (idade >= 18) # Expressões de comparação resultam em booleanos
print(f"Variável 'login_sucesso': Valor = {login_sucesso}, Tipo = {type(login_sucesso)}")
print(f"Variável 'tem_permissao': Valor = {tem_permissao}, Tipo = {type(tem_permissao)}")
print(f"Variável 'maior_de_idade' (para idade={idade}): Valor = {maior_de_idade}, Tipo = {type(maior_de_idade)}")

# Exemplo combinando as declarações, similar à Figura 6 [1]
print("\n--- Exemplo da Figura 6 [1] (conceitual) ---")
Nome = "Eduardo"       # str
Idade = 18             # int
_JurosSimples = 17.50  # float
TelaAtiva = True       # bool

print(f"Nome: {Nome} (Tipo: {type(Nome)})")
print(f"Idade: {Idade} (Tipo: {type(Idade)})")
print(f"_JurosSimples: {_JurosSimples} (Tipo: {type(_JurosSimples)})")
print(f"TelaAtiva: {TelaAtiva} (Tipo: {type(TelaAtiva)})")
# A Figura 7 [1] mostra a execução e a saída desses prints.

# 2. Reatribuição de Valores e Tipos (Baseado nas Figuras 8 e 9 de [1])
# Em Python, uma variável pode ter seu valor e, consequentemente, seu tipo
# alterados durante a execução do programa. Isso é uma característica da tipagem dinâmica.

print("\n--- 2. Reatribuição de Valores e Tipos ---")
minha_variavel_dinamica = 100
print(f"Valor inicial de 'minha_variavel_dinamica': {minha_variavel_dinamica} (Tipo: {type(minha_variavel_dinamica)})")

minha_variavel_dinamica = "Agora sou uma string"
print(f"Após reatribuição para string: '{minha_variavel_dinamica}' (Tipo: {type(minha_variavel_dinamica)})")

minha_variavel_dinamica = 3.14159
print(f"Após reatribuição para float: {minha_variavel_dinamica} (Tipo: {type(minha_variavel_dinamica)})")

minha_variavel_dinamica = False
print(f"Após reatribuição para bool: {minha_variavel_dinamica} (Tipo: {type(minha_variavel_dinamica)})")

# O material do curso [1] (Figura 8) ilustra a reatribuição assim:
# primeiro_nome = "Eduardo"
# primeiro_nome = 123456
# print(primeiro_nome)
# A Figura 9 [1] mostra a saída "123456", pois o programa é executado linha a linha
# e o print() exibe o último valor atribuído.

print("\n--- Exemplo das Figuras 8 e 9 [1] ---")
exemplo_fig8 = "Valor textual inicial"
print(f"Valor de 'exemplo_fig8' antes da reatribuição: '{exemplo_fig8}' (Tipo: {type(exemplo_fig8)})")
exemplo_fig8 = 777
print(f"Valor de 'exemplo_fig8' após reatribuição para inteiro: {exemplo_fig8} (Tipo: {type(exemplo_fig8)})")
# Se um print(exemplo_fig8) fosse executado após a segunda atribuição, sairia 777.


# 3. Conversão de Tipos (Casting)
# Embora o Python seja dinamicamente tipado, às vezes precisamos converter
# explicitamente um valor de um tipo para outro.

print("\n--- 3. Conversão Explícita de Tipos (Casting) ---")
numero_string = "123"
numero_inteiro = int(numero_string) # Converte string para int
print(f"String '{numero_string}' convertida para inteiro: {numero_inteiro} (Tipo: {type(numero_inteiro)})")

valor_inteiro = 42
valor_float = float(valor_inteiro) # Converte int para float
print(f"Inteiro {valor_inteiro} convertido para float: {valor_float} (Tipo: {type(valor_float)})")

valor_numerico = 98.6
string_convertida = str(valor_numerico) # Converte float para string
print(f"Float {valor_numerico} convertido para string: '{string_convertida}' (Tipo: {type(string_convertida)})")

# Tentativa de conversão inválida (pode gerar erro)
texto_nao_numerico = "Python"
try:
    numero_invalido = int(texto_nao_numerico)
except ValueError as e:
    print(f"Erro ao tentar converter '{texto_nao_numerico}' para int: {e}")

# O material do curso [1] (Seção 8, Figura 73) mostra a conversão de `input()` para `int()`:
# primeiro_nome = int(input("Digite o nome: ")) (o exemplo parece misturar nome com número)
# O ponto principal é que input() retorna string, e `int()` converte para inteiro.

print("\n--- Fim da Demonstração de Tipos de Dados ---")
