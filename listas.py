lista_mesclada = [1,2,3,"Olá Python",True,12.6]
print(lista_mesclada)
lista_mesclada.append(["Lista aninhada"])
print(lista_mesclada)
lista_mesclada.insert(3,5)
print(lista_mesclada)
print(len(lista_mesclada))
lista_mesclada.remove(1)
print(lista_mesclada)
nova_lista_mesclada = lista_mesclada
nova_lista_mesclada.pop(6)
nova_lista_mesclada.pop(5)
nova_lista_mesclada.pop(4)
print(nova_lista_mesclada)