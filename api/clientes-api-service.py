import requests

#URL da API do json-server
url = 'http://localhost:3000/clientes'

class ClientesApiService:

    #Fazendo a requisição GET
    def buscarClientes(self):
        response = requests.get(url)

        if response.status_code == 200:
            users = response.json()
            print(users)
            return
        else:
            print("Erro ao acessar a API:", response.status_code)

    #GET com parametro
    def buscarCliente(self, id=None, nome=None):
        if id is not None and nome is not None:
            response = requests.get(f"{url}?id={id}&nome={nome}")
        elif id is not None:
            response = requests.get(f"{url}/{id}")
        elif nome is not None:
            response = requests.get(f"{url}?nome={nome}")
        else:
            self.buscarClientes
            return
    
    #Post sendo enviado o body JSON
    def adicionatCliente(self, nome):
        novo_cliente = {"nome": nome}
        response = requests.post(url, json=novo_cliente)

        if response.status_code == 201:
            print(f"{nome} foi adicionado a lista de clientes")
        else:
            print("Erro ao adicionar o cliente: ", response.status_code)

    #Put sendo enviado o body JSON
    def alterarCliente(self, id, nome):
        cliente_atualizado = {"nome": nome}
        
        response = requests.put(f"{url}/{id}", json=cliente_atualizado)
        if response.status_code == 200:
            print(f"{nome} foi atualizado a lista de clientes")
        else:
            print("Erro ao atualizar o cliente: ", response.status_code)

    # Delete via parametro ID
    def removerCliente(self, id):
        response = requests.delete(f"{url}/{id}")
        if response.status_code == 200:
            print(f"Cliente de codigo {id} foi removido da lista com sucesso")
        else:
            print("Erro ao remover o cliente: ", response.status_code)

servico = ClientesApiService()
clientes = servico.buscarClientes()
servico.buscarCliente(1)
servico.buscarCliente(None, "Hit")
servico.buscarCliente(3, "Goku")
servico.alterarCliente("6ce4", "Guilherme Porto")
servico.removerCliente("1")