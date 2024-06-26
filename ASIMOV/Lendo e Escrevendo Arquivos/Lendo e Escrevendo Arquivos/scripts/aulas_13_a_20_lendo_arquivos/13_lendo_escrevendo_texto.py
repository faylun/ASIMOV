from pathlib import Path

# Lendo um arquivo forma nao recomendada
pasta_atual = Path(__file__).parent

lista_compras = open(pasta_atual / 'lista_de_compras.txt')

print(lista_compras.read())

lista_compras.close()


# Lendo arquivo forma recomendada
pasta_atual = Path(__file__).parent

with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    print(lista_compras.read())


# Lendo linha a linha
pasta_atual = Path(__file__).parent

with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    linha = lista_compras.readline()
    while linha != '':
        print(linha, end='')
        linha = lista_compras.readline()


# Lendo todas as linhas
pasta_atual = Path(__file__).parent

with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    print(lista_compras.readlines())


# Escrevendo arquivo
pasta_atual = Path(__file__).parent
itens_ja_comprados = ['farinha', 'fermento', 'agua']

with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    itens_lista = lista_compras.readlines()

with open(pasta_atual / 'lista_de_compras_atualizada.txt', mode='w') as lista_atualizada:
    for item in itens_lista:
        if not item.replace('\n', '') in itens_ja_comprados:
            lista_atualizada.write(item)


# Escrevendo linha a linha
pasta_atual = Path(__file__).parent
itens_ja_comprados = ['farinha', 'fermento', 'agua']

with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    itens_lista = lista_compras.readlines()

itens_lista_atualizada = []
for item in itens_lista:
    if not item.replace('\n', '') in itens_ja_comprados:
        itens_lista_atualizada.append(item)

with open('lista_de_compras_atualizada.txt', mode='w') as lista_atualizada:
    itens_lista_atualizada[-1] = itens_lista_atualizada[-1].replace('\n', '')
    lista_atualizada.writelines(itens_lista_atualizada)

print(itens_lista_atualizada)


# Acrescentando valores a um arquivo

pasta_atual = Path(__file__).parent

novos_items = ['abacate']
novos_items_c_quebra = [f'\n{item}' for item in novos_items]

with open('lista_de_compras.txt', mode='a') as lista_adicionada:
    lista_adicionada.writelines(novos_items_c_quebra)