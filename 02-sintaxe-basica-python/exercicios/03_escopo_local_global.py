# 02-sintaxe-basica-python/exercicios/03_escopo_local_global.py

"""
Exercício 3: Escopo de Variáveis - Local e Global

Objetivo:
Entender a diferença entre variáveis locais (definidas dentro de funções)
e variáveis globais (definidas fora de funções) e como elas são acessadas.
Este exercício é baseado nas Figuras 10 e 11 do material do curso [1].
"""

print("--- Demonstração de Escopo Local e Global ---")

# 1. Definição de Variável Global
# Esta variável é definida fora de qualquer função, no escopo principal do script.
# Ela pode ser acessada (lida) de qualquer lugar, inclusive de dentro de funções.
variavel_global_script = "Eu sou GLOBAL no script."
print(f"[ESCOPO GLOBAL] 'variavel_global_script' = '{variavel_global_script}'")


# 2. Definição de uma Função com Variável Local e Acesso à Global
def funcao_com_escopos():
    """
    Esta função demonstra o escopo local e o acesso a variáveis globais.
    """
    # Definição de Variável Local
    # Esta variável só existe dentro desta função.
    variavel_local_funcao = "Eu sou LOCAL, dentro de funcao_com_escopos."
    print(f"[FUNÇÃO funcao_com_escopos] 'variavel_local_funcao' = '{variavel_local_funcao}'")

    # Acessando (lendo) a Variável Global de dentro da função
    # Não é necessário declarar `global` para ler uma variável global.
    print(f"[FUNÇÃO funcao_com_escopos] Acessando 'variavel_global_script' (leitura) = '{variavel_global_script}'")

    # Tentativa de modificar uma variável global (sem a palavra-chave `global`)
    # Se fizermos: variavel_global_script = "Tentativa de modificar global"
    # Isso criaria uma NOVA variável LOCAL chamada 'variavel_global_script'
    # que sombrearia (ocultaria) a global dentro desta função, mas não a alteraria
    # no escopo global.

# Chamando a função para executar seu código interno
print("\n--- Chamando a funcao_com_escopos ---")
funcao_com_escopos()


# 3. Verificando o Valor da Variável Global Após a Chamada da Função
# A variável global não foi alterada pela função (pois a função apenas a leu).
print(f"\n[ESCOPO GLOBAL] Após chamada da função, 'variavel_global_script' ainda é = '{variavel_global_script}'")


# 4. Tentando Acessar a Variável Local Fora da Função
# Isso resultará em um NameError, pois variáveis locais não são visíveis fora de sua função.
print("\n--- Tentando acessar variável local de fora da função ---")
try:
    print(variavel_local_funcao)
except NameError as e:
    print(f"ERRO: Não foi possível acessar 'variavel_local_funcao' fora de seu escopo.")
    print(f"Detalhe do erro: {e}")


# 5. Modificando uma Variável Global de Dentro de uma Função (usando a palavra-chave `global`)
outra_variavel_global = 100
print(f"\n[ESCOPO GLOBAL] 'outra_variavel_global' antes da modificação = {outra_variavel_global}")

def funcao_que_modifica_global():
    """
    Esta função modifica explicitamente uma variável global.
    """
    global outra_variavel_global # Declara que estamos nos referindo à global
    print(f"[FUNÇÃO funcao_que_modifica_global] 'outra_variavel_global' (antes da modificação interna) = {outra_variavel_global}")
    outra_variavel_global = 200 # Modifica a global
    print(f"[FUNÇÃO funcao_que_modifica_global] 'outra_variavel_global' (após modificação interna) = {outra_variavel_global}")

    # Também podemos criar uma variável global de dentro de uma função, se ela não existir antes:
    global nova_global_da_funcao
    nova_global_da_funcao = "Criada dentro da função, mas é global."

print("\n--- Chamando funcao_que_modifica_global ---")
funcao_que_modifica_global()

print(f"\n[ESCOPO GLOBAL] 'outra_variavel_global' após modificação pela função = {outra_variavel_global}")
print(f"[ESCOPO GLOBAL] 'nova_global_da_funcao' (criada na função) = '{nova_global_da_funcao}'")


# Replicando o comportamento das Figuras 10 e 11 do material do curso [1]:
# Figura 10:
# variavel_global = "Mensagem Global"
# def funcao_local():
#     variavel_local = "Mensagem Local"
#     print(variavel_local)
#     print(variavel_global)
#
# Figura 11 (Saída):
# funcao_local()  # Imprime "Mensagem Local" e "Mensagem Global"
# print(variavel_global) # Imprime "Mensagem Global"
# print(variavel_local) # GERARIA ERRO, pois variavel_local é local à funcao_local

print("\n--- Simulação das Figuras 10 e 11 [1] ---")
variavel_global_fig = "Mensagem Global da Figura"

def funcao_local_fig():
    variavel_local_fig = "Mensagem Local da Figura"
    print(f"[FUNÇÃO FIGURA] Saída da variável local: {variavel_local_fig}")
    print(f"[FUNÇÃO FIGURA] Saída da variável global (lida): {variavel_global_fig}")

print("Chamando funcao_local_fig():")
funcao_local_fig()

print(f"\n[ESCOPO GLOBAL FIGURA] Saída da variável global: {variavel_global_fig}")

print("Tentando imprimir variavel_local_fig de fora (deve dar erro):")
try:
    print(variavel_local_fig)  # type: ignore
except NameError as e:
    print(f"ERRO ao tentar acessar variavel_local_fig: {e}")
    print("Conforme esperado, a variável local não é acessível globalmente.")

print("\n--- Fim do Exercício 3 ---")

