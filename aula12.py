################### metodos da classe dict ###################
#{}.clear - limpa o conjunto de chave valor do dicionario

#{}.copy - copia o dicionario

#{}.fromkeys - ele cria chave do seu dicionario
contato = dict.fromkeys(["nome","telefone"])
print(contato)
contato2 = dict.fromkeys(["nome","telefone"],"vazio")
print(contato2)

#{}.get - uma segunda forma de acessar valores dentro do dicionario
#contatos["chave"] #keyError

print(contato2.get("chave"))
print(contato2.get("chave",{}))
print(contato2.get("nome"))

#{}.keys - retorna só as chaves do dicionario
print(contato2.keys())

#{}.pop - apaga uma chave do seu dicionario
teste = {
    "diegodesouza.souza@gmail.com":{"noome":"Diego","telefone":"3333-4444"}
}
teste.pop("diegodesouza.souza@gmail.com")
print(teste.pop("diegodesouza.souza@gmail.com",{}))

#{}.setdefault - se o atributo não estiver no dicionário ele adiciona com o valor setado como padrão
contato3 = {"nome":"Diego","telefone":"333-4444"}

contato3.setdefault("nome","Emilly")
print(contato3)

contato3.setdefault("idade",35)
print(contato3)

#{}.update - ele atualiza a chave com o novo dicionario
contato4 = {
    "diegodesouza.souza@gmail.com": {"nome":"Diego","telefone":"3333-4444"}
}
contato4.update({"diegodesouza.souza@gmail.com":{"nome":"Diego de Souza"}})
print(contato4)

contato4.update({"emillylorrane@gmail.com":{"nome":"Emilly","telefone":"1111-5555"}})
print(contato4)

#{}.values - retona todos os valores
print(contato4.values())

#{}.in - uma forma elegante de verificar se exite uma chave no dicionario
print("diegodesouza.souza@gmail.com" in contato4)
print("teste2@gmail.com" in contato4)

#{}.del - remove o objeto do dicionario

del contato4["emillylorrane@gmail.com"]["telefone"]
print(contato4)

del contato4["diegodesouza.souza@gmail.com"]
print(contato4)
