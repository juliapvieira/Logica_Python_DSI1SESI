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
