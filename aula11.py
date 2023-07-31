################### Dicionário ###################
#conjunto não ordenado de par, chave valor
#obs.: para ser chave tem que ser um valor imutavel

pessoa = {"nome":"Thomas", "idade": 4}
pessoa2 = dict(nome="Emilly", idade=10)
pessoa["telefone"] = "3333-4444"

print(pessoa)

# acessando os valores
print(pessoa["nome"])
print(pessoa2["nome"])

#é possivel reeescrever os valores ou subscrever
pessoa["nome"] = "Thomas Anderson"
pessoa2["nome"] = "Emilly Lorrane"
print(pessoa["nome"])
print(pessoa2["nome"])

#dicionários podem armazenar qualquer tipo de objeto dentro dele

#salvando um dicionario em estrutura aninhada
contatos = {
    "emillylorranedesouza@gmail": {"nome": "Emilly Lorrane", "telefone":"961369636"},
    "thomasanderson@gmail.com": {"nome":"Thomas Anderson", "telefone": "916452563"},
    "diegodesouza.souza@gmail.com": {"nome":"Diego de Souza", "telefone":"961969969","idade": {"ano_nasc":1988,"ano_atual":2023,"idade-real":2023-1988}}
}

telefone = contatos["emillylorranedesouza@gmail"]["telefone"]
print(telefone)

idade = contatos["diegodesouza.souza@gmail.com"]["idade"]["idade-real"]
print(idade)

#usando o for para acessar
#forma não ideal 
for chave in contatos:
    print(chave, contatos[chave])

#melhor metodo
for chave, valor in contatos.items():
    print(chave, valor)
