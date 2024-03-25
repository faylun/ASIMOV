# Dado duas listas, printe todos os valores que aparecerem
# duplicados nas duas listas.

list1 = [10, 5, 20, 55, 44, 1]
list2 = [1, 10, 6, 9, 2]

for values1 in list1:
    if values1 in list2:
        print(f'The same value in both lists are: {values1}')
print('\n\n')

# Dado duas listas, printe uma mensagem dizendo se existe
# algum elemento em comum entre elas ou não.

flag = False
for values1 in list1:
    if values1 in list2:
        flag = True
        break
if flag:
    print('There are elements in common in both lists.')
else:
    print('There are no elements in common in both lists.')