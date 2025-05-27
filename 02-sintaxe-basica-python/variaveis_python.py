# 02-sintaxe-basica-python/variaveis_python.py

"""
Módulo de Demonstração: Variáveis em Python

Este arquivo explora a declaração de variáveis, atribuição de valores,
convenções de nomenclatura e o conceito de escopo (local e global) em Python,
conforme descrito na Seção 2.1 e nas Figuras 5, 10 e 11 do material do curso [1].
"""

print("--- Demonstração de Variáveis em Python ---")

# 1. Declaração e Atribuição de Variáveis (Baseado na Figura 5 de [1])
# Em Python, não é necessário declarar o tipo de uma variável explicitamente.
# A variável é criada no momento em que você atribui um valor a ela.
# O tipo da variável é inferido a partir do valor atribuído (tipagem dinâmica).

print("\n--- 1. Declaração e Atribuição ---")
# Exemplo da Figura 5 [1]
idade_usuario = 25
nome_usuario = "Carlos Silva"
saldo_conta = 1500.75
usuario_ativo = True

# Exibindo os valores e os tipos das variáveis
# A função type() retorna o tipo de um objeto/variável.
print(f"Variável 'idade_usuario': Valor = {idade_usuario}, Tipo = {type(idade_usuario)}")
print(f"Variável 'nome_usuario': Valor = '{nome_usuario}', Tipo = {type(nome_usuario)}")
print(f"Variável 'saldo_conta': Valor = {saldo_conta}, Tipo = {type(saldo_conta)}")
print(f"Variável 'usuario_ativo': Valor = {usuario_ativo}, Tipo = {type(usuario_ativo)}")


# 2. Convenções de Nomenclatura de Variáveis (Baseado na Seção 2.1 "Importante" de [1])
# O material do curso [1] sugere:
#   - Palavras no infinitivo impessoal (mais aplicável a funções/métodos).
#   - Uso de letras maiúsculas e minúsculas para diferenciar palavras.
#   - Exemplos do material: NumerosFixos, JurosSimples, _JurosCompostos, MediaAnual, Saldo_CC.

# A convenção mais comum e recomendada pela PEP 8 (Guia de Estilo para Código Python)
# para nomes de variáveis e funções é o `snake_case` (palavras minúsculas separadas por underscores).
# Para constantes, a convenção é `UPPER_SNAKE_CASE`.

print("\n--- 2. Convenções de Nomenclatura ---")
# Exemplos seguindo PEP 8 (snake_case):
taxa_de_juros = 0.05
nome_completo_cliente = "Ana Pereira"
quantidade_em_estoque = 100

# Exemplo de constante (UPPER_SNAKE_CASE):
PI = 3.14159
VELOCIDADE_MAXIMA_PERMITIDA = 110

print(f"Taxa de Juros (snake_case): {taxa_de_juros}")
print(f"Constante PI (UPPER_SNAKE_CASE): {PI}")

# Regras importantes para nomes de variáveis em Python:
# - Devem começar com uma letra (a-z, A-Z) ou um underscore (_).
# - O restante do nome pode conter letras, números (0-9) e underscores.
# - Nomes de variáveis são case-sensitive (idade, Idade e IDADE são três variáveis diferentes).
# - Não podem ser palavras reservadas do Python (ex: if, else, for, while, class, def, etc.).


# 3. Escopo de Variáveis: Local e Global (Baseado nas Figuras 10 e 11 de [1])
# O escopo de uma variável define onde ela pode ser acessada ou modificada no código.

print("\n--- 3. Escopo de Variáveis ---")

# Variável Global: Definida fora de qualquer função.
# Pode ser acessada de qualquer lugar no escopo do módulo (arquivo).
variavel_global_exemplo = "Eu sou global!"
print(f"Fora da função, 'variavel_global_exemplo' é: {variavel_global_exemplo}")

def minha_funcao_escopo():
    # Variável Local: Definida dentro de uma função.
    # Só pode ser acessada de dentro desta função.
    variavel_local_exemplo = "Eu sou local!"
    print(f"Dentro da função, 'variavel_local_exemplo' é: {variavel_local_exemplo}")

    # Acessando a variável global de dentro da função (apenas leitura por padrão)
    print(f"Dentro da função, 'variavel_global_exemplo' (lida) é: {variavel_global_exemplo}")

    # Para modificar uma variável global dentro de uma função,
    # é preciso usar a palavra-chave 'global'.
    global variavel_global_exemplo_modificada
    variavel_global_exemplo_modificada = "Global modificada pela função!"
    print(f"Dentro da função, 'variavel_global_exemplo_modificada' é: {variavel_global_exemplo_modificada}")

# Chamando a função para executar o código dentro dela
minha_funcao_escopo()

variavel_local_exemplo = None  # Initialize to prevent NameError.
# Tentando acessar a variável local fora da função.
# Com a inicialização acima, 'variavel_local_exemplo' refere-se à global None (ou ao valor atribuído),
# e não mais causa um NameError aqui. O bloco except NameError não será acionado para este caso.
try:
    print(f"Fora da função, tentando acessar 'variavel_local_exemplo': {variavel_local_exemplo}")
except NameError as e:
    print(f"Erro ao tentar acessar 'variavel_local_exemplo' fora da função: {e}")
    print("Isso demonstra que variáveis locais não são acessíveis globalmente.")

# Acessando a variável global que foi modificada pela função
# (Como foi declarada globalmente antes de ser modificada, não precisa de 'global' aqui)
# No entanto, a Figura 10 e 11 do anexo [1] parecem tratar de uma `variavel_global`
# que é modificada dentro da função sem a keyword `global`, o que em Python criaria
# uma nova variável local com o mesmo nome, sombreando a global.
# O exemplo acima com `variavel_global_exemplo_modificada` demonstra a forma correta
# de modificar uma global de dentro de uma função.

# Replicando o cenário da Figura 10/11 [1] para discussão:
# A Figura 10 define `variavel_local` dentro de `funcao_local` e `variavel_global` fora.
# A Figura 11 chama `funcao_local()` (que imprime a local e a global) e depois imprime a global.

print("\n--- Replicando o cenário das Figuras 10 e 11 [1] ---")
variavel_global_fig10 = "Sou a Global da Figura 10"

def funcao_local_fig10():
    variavel_local_fig10 = "Sou a Local da Figura 10"
    print(f"[Função Fig10] Variável Local: {variavel_local_fig10}")
    print(f"[Função Fig10] Variável Global (lida): {variavel_global_fig10}")
    # Se tentássemos atribuir a variavel_global_fig10 aqui sem 'global variavel_global_fig10',
    # criaríamos uma nova variável local com esse nome.
    # Ex: variavel_global_fig10 = "Tentativa de modificar" (criaria uma local)

funcao_local_fig10()
print(f"[Fora Função Fig10] Variável Global: {variavel_global_fig10}")

# Demonstração da palavra-chave `global` para modificar
def funcao_modifica_global():
    global variavel_global_fig10 # Indica que estamos nos referindo à global
    print(f"[Função Modifica] Global antes: {variavel_global_fig10}")
    variavel_global_fig10 = "Global da Figura 10 MODIFICADA!"
    print(f"[Função Modifica] Global depois: {variavel_global_fig10}")

funcao_modifica_global()
print(f"[Fora Função Modifica] Variável Global após modificação: {variavel_global_fig10}")


print("\n--- Fim da Demonstração de Variáveis ---")
