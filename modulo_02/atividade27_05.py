# ======================================================
# MÓDULO 1 — CRIAÇÃO DE STRINGS
# ======================================================

# EX1
# Crie uma variável chamada texto1 com o valor "Logica"
# usando aspas duplas e exiba o conteúdo.

texto1 = "Logica"
print (texto1)
# -----------------------------------------------------------

# EX2
# Crie uma variável chamada texto2 com o valor
# 'Eu sou top em python' usando aspas simples e exiba.

texto2 = 'Eu sou top em python'
print (texto2)

# ---------------------------------------------------------

# EX3
# Crie uma string usando aspas simples que contenha
# aspas duplas dentro do texto: copa "padrão fifa".

texto = 'Copa "padrão fifa"'
print (texto)
# ---------------------------------------------------------

# EX4
# Crie uma string usando aspas duplas que contenha
# aspas simples dentro do texto: copa 'padrão fifa'.
texto = ("Copa 'padrão fifa'")
print (texto)
# ---------------------------------------------------------

# ======================================================
# MÓDULO 2 — STRINGS MULTILINHA
# ======================================================

# EX5
# Crie uma string multilinha representando um menu
# com as opções:
# -A  Exibe ajuda
# -E  Execute agora, quero jogar!

menu = """\
-A  "Exibe ajuda"
-E  "Execute agora, quero jogar!"
"""
print (menu)

#  =====================================
# EX6
# Crie uma string multilinha contendo um poema
# com três versos.
menu = """\
O amor machuca 
tanto quanto cura
Ele acaba tanto quanto dura
Mesmo sendo eterno ele sempre escapula

O mundo parece vazio
O amor resolve isso sozinho
Acreditar no que ele sempre faz
Torna-o bem mais veraz

Quando a vida parece um pesadelo
O amor elimina com um simples apelo
Todos querem o amor
Mas para isso precisam descobrir seu sabor
# peguei do google
"""
print (menu)
# -----------------------------------------

# ======================================================
# MÓDULO 3 — CONCATENAÇÃO AUTOMÁTICA
# ======================================================

# EX7
# Use concatenação automática de literais para unir
# as palavras "Volei" e "top!".
texto = ("Volei " "é" " top")
print (texto)
# ----------------------------------------------------

# EX8
# Concatene automaticamente as strings
# "Python", " é ", "demais" em uma única string.
texto = ("Python" " é" " demais")
print (texto)

# ======================================================
# MÓDULO 4 — STRINGS COMO SEQUÊNCIAS
# ======================================================

# EX9
# Atribua "software" a uma variável chamada st
# e mostre a primeira letra da string.
st = "software"
print ("Primeira letra:", st [0])
# ----------------------------------------------------

# EX10
# Usando a mesma string "software",
# mostre a última letra.
st = "software"
print ("Última letra:", st [-1])
# ------------------------------------------------------

# EX11
# Mostre os caracteres do índice 1 até o índice 4
# (sem incluir o 4) da string "software ".
st = "software"
print ("Primeira letra:", st [0])

st = "software"
print ("Segunta letra:", st [1])

st = "software"
print ("Terceira letra:", st [2])

st = "software"
print ("Quarta letra:", st [3])
# -----------------------------------------------------

# EX12
# Mostre os caracteres do início até o índice 3
# da string "software".
st = "software"
print ("Primeira letra:", st [0])

st = "software"
print ("Segunda letra:", st [1])

st = "software"
print ("Terceira letra:", st [2])
# -----------------------------------------------------


# EX13
# Mostre os caracteres do índice 2 até o final
# da string "software".
st = "software"
print ("Segunda letra:", st [1])
st = "software"

print ("Terceira letra:", st [2])
st = "software"

print ("Quarta letra:", st [3])
st = "software"

print ("Quinta letra:", st [4])
st = "software"

print ("Sexta letra:", st [5])
st = "software"

print ("Sétima letra:", st [6])
st = "software"

print ("Oitava letra:", st [7])
st = "software"

# ------------------------------------------

# EX14
# Mostre o tamanho da string "software"
# usando a função len().
st = "software"
print("Tamanho", len (st))
# -------------------------------------------

# EX15
# Acesse o último caractere de "software"
# usando índice positivo (sem usar -1).
st = "software"
print("Sétima letra:", st [7])
# --------------------------------------------


# EX16
# Mostre os caracteres que estão nos índices pares
# da string "software".
texto = "software"
print(texto[::2])


# EX17
# Inverta a string "software".
texto = "software"
print(texto[::-1])