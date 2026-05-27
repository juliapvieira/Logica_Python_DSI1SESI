# AULA COMPLETA: NUMEROS EM PYTHON
"""
Vamos aprender:
1- Tipos numéricos
2- Conversões de tipos
3- Hierarquia numérica
4- Operações matemáticas 
5- Coerção de tipos
6- Verificação de tipos
7- Entrada de dados
"""
# ==============================
# PASSO 01 - TIPOS NUMÉRICOS
# ==============================
# int = NÚMEROS INTEIROS
# float + números com casas decimais 
# complex = números complexos (usado em matemática/engenharia)

print ("===== TIPOS NUMÉRICOS =====")

# EXEMPLO 01 - NÚMERO INTEIRO 

# Criamos uma variável chamada número_inteiro
numero_inteiro = 10

# Mostramos o valor
print ("Valor:", numero_inteiro)
# Type () mostra qual é o tipo da variável 
print ("Tipo", type (numero_inteiro))

print ("-------------------------------------")

# EXEMPLO 02 - NÚMERO DECIMAL
# Float é um número com ponto decimal
numero_decimal = 3.14

print ("Valor:", numero_decimal)
print ("Tipo:", type (numero_decimal))
print ('-------------------------------------')

# EXEMPLO 03 - NÚMEROS COMPLEXOS 
# Um número complexo possui duas partes 
# Parte real (número normal)
# Parte imaginária (multiplicada por j)

# Estrutura geral:
# Número = a + bj

# a = parte real
# b = parte imaginária
# j = unidade imaginária

numero_complexo = 2 + 3j
print ("Valor:" , numero_complexo)
print ("Tipo:" ,type (numero_complexo))
print ("------------------------------------")
# EXEMPLO 03 - ACESSANDO CADA PARTE DO NÚMERO
#.real retorna a parte real
print ("parte real:", numero_complexo.real)


#.imag retorna a parte imaginária
print ("parte imaginária:", numero_complexo.imag)

#apenas para separar visualmente a saída 
print ("\n\n")


#===============================
#PASSO 02 - CONVERSÃO DE TIPOS 
#===============================

## Exemplo Clássico:
## Dados vindo do usuário são texto (string), muitas vezes é necessário converter eles. 
#exemplo de conversão:

print("======conversões=======")
#float - > int

valor = int (3.9)
 
print("int(3.9:",valor)
print("tipo:", type (valor))
 
#convertendo string(texto) para inteiro
valor1 = int= "10"
print(type(valor1))

valor2 =int ("10") 
print('int("10"):', valor2)
print ("tipo:", type (valor2))

#int --> float
valor3 = float(10)
print("float(10):", valor3)
print ("Tipo:", type (valor3))
                    




                    # EX4
# Tente converter a string "cento e vinte"
# para inteiro e observe o que acontece.
# string = cento_e_vinte
# numero = str (numero)
# inteiro= int (numero)
# print ("conversão para inteiro:",numero)
# Traceback (most recent call last):
# #File "c:\Users\Aluno\Logica_Python_DSI1SESI\aula.py\exerciciosaula.py", line 44, in <module>
# tring = cento_e_vinte 
print ("================================================")