import requests
from pprint import pprint

#Get - Obter todos os recursos
resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos')
#pprint(resultado_get.json())

#Get com id - Obter recusro unico
resultado_getID = requests.get('https://jsonplaceholder.typicode.com/todos/2')
#pprint(resultado_getID.json())

#POST - criar um novo recurso
nova_tarefa = {'completed': False,
  'title': 'Limpar o carro',
 'userId': 1}
resultado_post = requests.post('https://jsonplaceholder.typicode.com/todos/', nova_tarefa)
#pprint(resultado_post.json())

#PUT - Alterar um recurso existente
tarefa_alterada = {'completed': False,
  'title': 'Limpar o moto',
 'userId': 1}
resultado_put = requests.put('https://jsonplaceholder.typicode.com/todos/2', tarefa_alterada)
#pprint(resultado_put.json())

#DELETE - Excluir um recurso
resultado_delete = requests.delete('https://jsonplaceholder.typicode.com/todos/2')
pprint(resultado_delete.json())