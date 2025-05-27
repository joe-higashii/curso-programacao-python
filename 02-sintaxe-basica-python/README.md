# 🐍 Módulo 2: Sintaxe Básica de Python

Bem-vindo(a) ao Módulo 2 do curso de Programação Python! 👋 Após a introdução inicial à linguagem e a configuração do ambiente no Módulo 1, este módulo mergulhará nos blocos de construção fundamentais de qualquer programa Python: **variáveis, tipos de dados, operadores e expressões**. Compreender esses conceitos é essencial para escrever código funcional, lógico e eficiente.

Neste módulo, exploraremos como o Python lida com diferentes formas de dados, como realizar cálculos e comparações, e como instruir o programa a tomar decisões simples com base em condições.

---

## 🎯 Objetivos de Aprendizagem

Ao final deste módulo, você será capaz de:

* ✍️ Declarar e atribuir valores a **variáveis** em Python, compreendendo as convenções de nomenclatura (como `snake_case`).
* 🔄 Entender a natureza da **tipagem dinâmica** do Python e como os tipos de dados são implicitamente definidos.
* 📊 Identificar e utilizar os principais **tipos de dados** numéricos (`int`, `float`), literais (`str`) e lógicos (`bool`).
* 🔍 Compreender o conceito de **escopo de variáveis** (local e global) e seu impacto no acesso aos dados.
* 🧮 Aplicar diversos **operadores** Python para realizar cálculos e comparações:
    * Operadores **Aritméticos** (adição `+`, subtração `-`, multiplicação `*`, divisão `/`, divisão inteira `//`, módulo `%`, exponenciação `**`).
    * Operadores **De Comparação** (igual `==`, diferente `!=`, maior que `>`, menor que `<`, etc.).
    * Operadores **Lógicos** (`and`, `or`, `not`).
    * Operadores **De Identidade** (`is`, `is not`).
* 🧠 Construir e avaliar **expressões** matemáticas e lógicas, respeitando a ordem de precedência dos operadores (PEMDAS).
* 🚦 Implementar **estruturas condicionais** simples utilizando `if` e `else` para controlar o fluxo de execução do programa.

---

## 📚 Conteúdo Abordado

Este módulo cobre em detalhes os seguintes tópicos da sintaxe básica do Python:

* **Variáveis em Python:**
    * Declaração e atribuição direta de valores (ex: `idade = 25`).
    * Convenções de nomenclatura: uso de `snake_case` para nomes de variáveis (ex: `nome_completo`), escolha de nomes significativos.
    * Escopo de variáveis:
        * **Locais:** Definidas dentro de funções, acessíveis apenas dentro dessas funções.
        * **Globais:** Definidas fora de qualquer função, acessíveis de qualquer parte do código (com ressalvas e boas práticas).
    * Demonstrações e exemplos práticos em `exemplos/variaveis_python.py`.

* **Tipos de Dados Fundamentais:**
    * Tipagem implícita e dinâmica em Python: o tipo é inferido no momento da atribuição.
    * **Numéricos:**
        * Inteiros (`int`): para números inteiros (ex: `10`, `-3`).
        * Reais/Ponto Flutuante (`float`): para números decimais (ex: `3.14`, `-0.5`).
    * **Literais (Sequências):**
        * Strings (`str`): para representar texto, delimitado por aspas simples (`'texto'`) ou duplas (`"texto"`).
    * **Lógicos:**
        * Booleanos (`bool`): representam valores de verdade, podendo ser `True` ou `False`.
    * Reatribuição de valores e, consequentemente, de tipos a variáveis.
    * Exemplos e exploração em `exemplos/tipos_dados_python.py`.

* **Operadores em Python:**
    * **Aritméticos:** `+` (soma), `-` (subtração), `*` (multiplicação), `/` (divisão), `//` (divisão inteira), `%` (módulo/resto), `**` (exponenciação).
    * **De Comparação (Relacionais):** `==` (igual a), `!=` (diferente de), `<` (menor que), `>` (maior que), `<=` (menor ou igual a), `>=` (maior ou igual a). Retornam `True` ou `False`.
    * **Lógicos (Booleanos):** `and` (E lógico), `or` (OU lógico), `not` (NÃO lógico). Usados para combinar expressões booleanas.
    * **De Identidade:** `is`, `is not`. Comparam se duas variáveis referenciam o mesmo objeto na memória (identidade), não apenas se têm o mesmo valor.
    * Explicações detalhadas e exemplos de uso em `exemplos/operadores_python.py`.

* **Expressões e Estruturas Condicionais:**
    * Construção de expressões matemáticas e lógicas combinando variáveis, literais e operadores.
    * **Ordem de Precedência dos Operadores (PEMDAS/BODMAS):** Parênteses, Exponenciação, Multiplicação/Divisão (da esquerda para a direita), Adição/Subtração (da esquerda para a direita).
    * Estruturas condicionais básicas para tomada de decisões:
        * `if` (se uma condição é verdadeira, execute um bloco de código).
        * `else` (senão, se a condição do `if` for falsa, execute outro bloco de código).
    * Detalhes e exemplos em `exemplos/expressoes_condicionais_python.py`.

---

## 📂 Arquivos de Exemplo e Exercícios Práticos

Para uma compreensão aprofundada e prática, este módulo inclui os seguintes arquivos com exemplos detalhados e exercícios:

* **Arquivos de Exemplo (na pasta `exemplos/`):**
    * `variaveis_python.py`
    * `tipos_dados_python.py`
    * `operadores_python.py`
    * `expressoes_condicionais_python.py`

* **Exercícios Práticos (na pasta `exercicios/`):**
    * `01_declaracao_variaveis.py`
    * `02_tipos_implicitos_e_reatribuicao.py`
    * `03_escopo_local_global.py`
    * `04_operadores_aritmeticos_pratica.py`
    * `05_operadores_comparacao_pratica.py`
    * `06_operadores_logicos_pratica.py`
    * `07_operadores_identidade_pratica.py`
    * `08_expressoes_matematicas_pemdas.py` (incluindo exemplos com `if/else`)

---

## 🔗 Recursos Adicionais

* 🌐 Para consulta rápida sobre sintaxe e mais exemplos práticos, o [W3Schools Python Tutorial](https://www.w3schools.com/python/default.asp) é um excelente recurso online.
* A documentação oficial do Python ([https://docs.python.org/pt-br/3/](https://docs.python.org/pt-br/3/)) é a fonte mais completa e detalhada para todos os aspectos da linguagem.

---

Este módulo é crucial para construir uma base sólida em Python. Dedique tempo para entender cada conceito e, principalmente, **pratique com os exemplos e exercícios**. A programação é uma habilidade que se desenvolve com a prática! 💪