"""
### Regras da aplicação

- A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
- Deve ser possível adicionar um contato
    - O contato pode ter os dados:
    - Nome
    - Telefone
    - Email
    - Favorito (está opção é para poder marcar um contato como favorito)
- Deve ser possível visualizar a lista de contatos cadastrados
- Deve ser possível editar um contato
- Deve ser possível marcar/desmarcar um contato como favorito
- Deve ser possível ver uma lista de contatos favoritos
- Deve ser possível apagar um contato

"""

def adicionar_contato(contatos, nome_contato, telefone, email):
  contato = {"nome": nome_contato, "telefone": telefone, "email": email, "favorito": False}
  contatos.append(contato)
  print(f"Contato {nome_contato} foi adicionada com sucesso!")
  return

def ver_contatos(contatos):
  print("\nLista de Contatos:")
  for indice, contato in enumerate(contatos, start=1):
    status = "✓" if contato["favorito"] else " "
    nome_contato = contato["nome"]
    telefone = contato["telefone"]
    email = contato["email"]
    print(f"{indice}. [{status}] {nome_contato} {telefone} {email}")
  return

def atualizar_contato(contatos, indice_contato, novo_nome_contato, novo_telefone, novo_email ):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]["nome"] = novo_nome_contato
    contatos[indice_contato_ajustado]["telefone"] = novo_telefone
    contatos[indice_contato_ajustado]["email"] = novo_email
    print(f"Contato {indice_contato} atualizada para {novo_nome_contato}")
  else:
    print("Índice de contato inválido.")
  return

def favoritar_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if contatos[indice_contato_ajustado]["favorito"] == False:
    contatos[indice_contato_ajustado]["favorito"] = True
  elif contatos[indice_contato_ajustado]["favorito"] == True:
    contatos[indice_contato_ajustado]["favorito"] = False
  print(f"Tarefa {indice_contato} marcada como favorito")
  return

def ver_contatos_favoritos(contatos):
  print("\nLista de Contatos Favoritos:")
  for indice, contato in enumerate(contatos, start=1):
    status = "✓" if contato["favorito"] else " "
    nome_contato = contato["nome"]
    telefone = contato["telefone"]
    email = contato["email"]
    if contato["favorito"] == True:
      print(f"{indice}. [{status}] {nome_contato} {telefone} {email}")
  return

def deletar_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  #contatos.remove(indice_contato_ajustado)
  del contatos[indice_contato_ajustado]
  print("Contato deletado.")
  return

contatos = []

while True:
  print("\nMenu Genrenciador de contatos:")
  print("1 - Adcionar Contato")
  print("2 - Visualizar Contatos")
  print("3 - Atualizar Contato")
  print("4 - Marcar/Desmarcar Contato como Favorito")
  print("5 - Lista de Contatos Favoritos")
  print("6 - Excluir Contato")
  print("7 - Finalizar Programa")

  opcao = input("Digite sua opção: ")

  if opcao == "1":
    nome_contato = input("Digite o nome do contato que deseja adicionar: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    adicionar_contato(contatos,nome_contato, telefone, email)
  
  elif opcao == "2":
    ver_contatos(contatos)

  elif opcao == "3":
    ver_contatos(contatos)
    indice_contato = input("Digite o número do contato que deseja atualizar: ")
    novo_nome = input("Digite o novo nome do contato: ")
    novo_telefone = input("Digite o novo numero de telefone do contato: ")
    novo_email = input("Digite o novo email do contato: ")
    atualizar_contato(contatos, indice_contato, novo_nome,novo_telefone,novo_email)

  elif opcao =="4":
    ver_contatos(contatos)
    indice_contato = input("Digite o número do contato que deseja favoritar: ")
    favoritar_contato(contatos, indice_contato)
  
  elif opcao == "5":
    ver_contatos_favoritos(contatos)

  elif opcao == "6":    
    ver_contatos(contatos)
    indice_contato = input("Digite o número do contato que deseja atualizar: ")
    deletar_contato(contatos, indice_contato)

  elif opcao == "7":
    break

print("Programa Finalizado")