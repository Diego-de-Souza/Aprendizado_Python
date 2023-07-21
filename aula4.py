##############  IDENTAÇÃO DE BLOCO  ##############
### a linguagem sabe como e onde começa e termina um bloco pela identação
### ou seja, você é obrigado a usar a identação.

#sempre usar a identação no bloco, caso contrario não vai funcionar
def sacar(valor:float): #aqui inicia o bloco com a inserção dos ":"
    saldo = 500
    if saldo >= valor: #aqui inicia o bloco com a inserção do ":"
        #essas mensagens só serão impressas caso a condição seja verdadeira
        print("Valor sacado!")
        print("retire seu dinheiro na boca do caixa.")
    #neste caso vai executar independente do valor a ser sacado
    print("Obrigado por ser nosso cliente, tenha um bom dia!")

sacar(100)
sacar(1000)

################  ESTRUTUAS CONDICIONAIS  ################

MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")

if idade < MAIOR_IDADE :
    print("Ainda não pode tirar a CNH")


if idade >= 21:
    print("Já pode viajar com o carro")
else:
    print("Ainda cheira leite, tem que treinar muito antes de viajar")

if idade >= MAIOR_IDADE:
    print("Já pode retirar a CNH")
elif idade >= IDADE_ESPECIAL:
    print("Pode fazer as aulas teoricas, mas não pode tirar a CNH")
else:
    print("Ainda não pode tirar a CNH")

## if aninhado
conta_normal = True
conta_universitaria = False

saldo1 = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo1 >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo1 + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("não foi possivel realizar o saque, saldo insuficiente")
elif conta_universitaria:
    if saldo1 >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente")


## if ternario
status = "Sucesso" if saldo1 >= saque else "Falha"
print(f"{status} ao realizar o saque!")


#############  ESTRUTURA DE REPETIÇÃO  #############
## FOR e WHILE

texto = input("Informe seu texo: ")
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else: 
    print()

##RANGE
list(range(4))
print(list)

for numero in range (0,11):
    print(numero,end=" ")

#exemplo utilizando a função built-in range
for numero in range(0,51,5):
    print(numero, end=" ")

##While
opcao = 1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por utilizar nosso sistema bancário, até logo!")

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)