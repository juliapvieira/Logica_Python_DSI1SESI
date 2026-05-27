#AULA COMPLETA - STRINGS EM PYTHON 

# Criação de Strings
# Strings multilinhas
# Indice e slides
# Operações em string
# Imutabilidade
# Métodos úteis
# Formação de texto
# Unicode e bytes

# ---------------------------
# 1) CRIAÇÃO DE STRINGS
# ---------------------------
# strings são textos em python
# Podem ser criadas usando aspas simples ou duplas: quando? depende do que a empresa quer que você use 

texto1 = "Python"
texto2 = "Curso de python"
texto3 = "Copa 'padrão fifa'"
print (texto1, texto2, texto3)

# Python permite misturar aspas simples e duplas, dentro das strings sem precisar escapar caracteres

# -----------------------------
# 2) STRINGS MULTILINHA
# -----------------------------
# Usando 3 aspas (""" ou ''') para criar textos que ocupam várias linhas 

menu = """\
Uso: programa [OPÇÕES]
-h Exibe ajuda
-U Url do dataset
"""
print (menu)

# Esse formato é muito usado para:
# - Menus
# - documentação
# - textos longos
# -------------------------------
# 3) CONCATENAÇÃO AUTOMÁTICA
# -------------------------------
# Quando duas strings aparecem lado a lado, o Python junta automaticamente

texto = ("Copa" " 2026," " Neymar é show mesmo?")
print (texto)

# --------------------------------
# 4) STRINGS COMO SEQUENCIA
# --------------------------------

st = "maracana"
print ("Primeira letra:", st [0])
# Só exibir a letra: m

print ("Ultima letra:", st [-1])

print ("Trecho 1:4", st [1:4])

print ("Do início ate 3:", st [:3])

print ("Tamanho", len (st))

# ------------------------------------
# 5) OPERAÇÕES COM STRINGS
# ------------------------------------
# Python permite várias variações com strings
# detectar se tem ou nao o "n" na palavra maracana, e vai detectar em booleano (verdadeiro ou falso)

print ("n" in st)
# Signfica que a letra "n" existe dentro da string

print ("X" not in st)
# Siginifica que "X" não existe na string

print ("m" * 20)
#Multiplicação repete a string

print ("m" + "aracana " + texto1)
# Operador + concatena strings

# ---------------------------------------
# 6) STRINGS SÃO IMUTÁVEIS
# ---------------------------------------
# Strings não podem ser alteradas diretamente!!!
# Isso significa que o conteudo orginial não muda
# O que acontece é a criação de uma nova string 

# texto ="python 3"
# python 3 = string

# Método replace cria uma nova string
# replace é substituir. 
texto ="python 3"
texto = texto.replace ("3", "2")

print (texto)

# -----------------------------------------
# 7) MÉTODOS IMPORTANTES
# -----------------------------------------
# Strings possuem vários  métodos úteis.

# isso serve para deixar a letra maiúscula
cidade = "maracana" 
print(cidade.capitalize())
# Serve para colcoar a primeira letra em maiúscula

# Conta quantas vezes "a" aparece
print(cidade.count("a"))

# Verifica se começa com "m"
print(cidade.startswith("m"))

# Verifica se termina com "z"
print(cidade.endswith("z"))

# divide a string em uma lista
frase = "Copa de 2002"
print(frase.split(" "))
