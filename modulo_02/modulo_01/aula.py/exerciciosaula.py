#Em Python, uma variável é criada usando o sinal de = para armazenar um valor.
#nome = "Julia"
#idade = 17
#altura = 1.65
#aprovado = True

#nome guarda um texto;
#idade guarda um número inteiro;
#altura guarda um número decimal;
#aprovado guarda um valor booleano (True ou False).
print ("================================================")

# EX1
# O usuário digitou "25" como sua idade em um formulário.
# Converta para inteiro e calcule a idade que ele terá
# daqui a 5 anos.
idade = "25"
idade = int(idade)
idade_futura = idade + 5
print(idade_futura)
print ("================================================")

# EX2
# Converta o número de ponto flutuante 7.999
# para inteiro e observe o resultado.
numero =  7.999
inteiro = int (numero)
print("conversão para inteiro:",numero)
print ("================================================")


# EX3
# Converta a string "-3.14" para float
# e multiplique o resultado por 2.
numero = "-3.14"
numero = float(numero)
numero = numero*2 
print(numero)
print ("================================================")

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

# EX5
# Converta o número 42 para string
# e concatene com a palavra " respostas".
numero = str (numero)
numero = 42
numero_str = str(numero)
print(numero_str + " respostas")
print ("================================================")

# EX6
# Use a função complex() para criar
# um número complexo com parte real 3
# e parte imaginária 5.
numero_complexo = "3"
numero_complexo = complex(3, 5)
print("numero_complexo:", numero_complexo)
print ("================================================")


# EX7
# Converta o número 0 para booleano
# e mostre o resultado.
numero = 0
resultado = bool(numero)
print(resultado)
print ("================================================")


# EX8
# Converta o número -100 para booleano
# e mostre o resultado.
numero = -100
resultado = bool (numero)
print (resultado)
print ("================================================")

# EX9
# Converta o número 3.1415 para inteiro
# e depois para string, tudo em uma única linha.
numero = 3.1415
inteiro = int (numero)
numero = str(int(numero))
print(numero)
print ("================================================")

# EX10
# Some um número inteiro (5) com um float (2.3)
# e verifique qual é o tipo do resultado.
numero1 = 5
numero2 = 2.3
resultado = numero1 + numero2
print(resultado)
print(type(resultado))