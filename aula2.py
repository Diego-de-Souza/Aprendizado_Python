#variaveis e constantes
age= 35
nome= 'Diego'
print(f'Meu nome é {nome} e eu tenho {age} anos de idade.')

nome ='Thomas'

print(nome, age)

#em pythom usar o nome das váriaveis em snake case
#exe.:
limite_saque_diario = 1000

#definição de constante
BRAZILIAN_STATES= ['SP','RJ','RS','SC']

print(BRAZILIAN_STATES)

#posso atribuir tudo na mesma linha
nome, idade, mentira = 'Diego', 38, True

print(nome, idade, mentira)

############## convertendo tipos #################
preco=10.5
valor=29
valor_total="20.50"
# de float para str
print(str(preco))
#de str para float
print(float(valor_total))
#transformando float em int
print(int(1.9))
# de string para float
print(float("10.10"))

print(type(preco))
preco_str=str(preco)
print(type(preco_str))

############ entrada e saida ############
nome = input("Informe seu nome: ")
idade = input("Digite sua idade: ")
#imprimindo de forma normal
print(nome, idade)
#imprimindo utilizando end
print( nome, idade, end="... \n")
#imprimir alterando o separador
print(nome, idade, sep="s")
