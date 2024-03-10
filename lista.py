lista = []

print("Bem Vindo a Sua lista de Comprar o Que vc vai anotar")

while True:
    item = input("Digite sua lista de Compras ou se quiser sair e so escrever 'sair' ")
    if item.lower() == "sair":
        break
    lista.append(item)

def acrencentar(lista,nome):
    lista.append(nome)
    print(f"você Acrescentou  -----> {nome} <-------- na Lista .")

def remover_nome(lista,nome):
    if nome in lista:
        lista.remove(nome)
        print(f"O item --------> {nome} <-------- foi removido.")
    else:
        print(f"Nao tem item selecionado ---------> {nome} <--------.")

def mostrar_lista():
    if lista:
        print("Lista de Compras")
        for i, item in enumerate (lista, start=1):
            print(f"{i}= {item}")
    else:
        print("LISTA DE COMPRAS VAZIAS")

mostrar_lista()