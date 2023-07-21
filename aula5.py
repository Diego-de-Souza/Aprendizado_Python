################  metodos uteis da classe string  ################
nome = "Diego"
# metodo maisuculo,   minusculo e titulo
print(nome.upper())
print(nome.lower())
print(nome.title())

# metodo eliminar espaços em branco
texto = " Olá mundo!    "

print(texto+".")
print(texto.strip()+".")
print(texto.lstrip()+".")
print(texto.rstrip()+".")

# metodo de junção e centralização
menu = "Python"

print("####"+menu+"####")
print(menu.center(14))
print(menu.center(14,"#"))
print("P-Y-T-H-O-N")
print("-".join(menu))

################  INTERPOLAÇÃO DE VARIAVEIS  ################
#1° FORMA "%", em python 3 ela não é mais recomendada
nome1 = "Diego"
idade = 35
profissao = "Programador"
linguagem = "Python"



print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s."%(nome, idade, profissao,linguagem))

#2° FORMA "{}" format 
dados1={"nome":"Diego","idade": 28,"profissao":"Programador","linguagem":"Python"}

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}.".format(nome, idade, profissao,linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho com {1} e estou matriculado no curso de {1}.".format(linguagem, profissao,idade,nome))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.".format(**dados1))

#3°FORMA
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.")

PI=3.14159
print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")

#############  fatiamento de string  #############
vida = "Thais de Assis Corrêa"

print(vida[0])
print(vida[:9])
print(vida[10:])
print(vida[10:16])
print(vida[10:16:2])
print(vida[:])
print(vida[::-1])

################  strings de mutiplas linhas  ################

mensagem = f'''
      Olá meu nome é {nome},
    Eu estou aprendendo Python.
         Essa mensagem tem diferentes recuos
'''
print(mensagem)

print("""
      *************menu****************
      
      1 - Depositar
      2 - Sacar
      3 - Sair
      
      *********************************
      
        Obrigado por usar nosso sistema!!!!
      """
      )