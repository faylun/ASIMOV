# Dado uma sequência de números, calcule a soma e média dos números.
# ATENÇÃO: não vale usar a função sum() !

numbers = [5, 20, 30, 40, 10]

sum_num = 0
for n in numbers:
    sum_num += n

print(f'Sum: {sum_num}')
print(f'Average: {sum_num / len(numbers)}\n\n')

# Dado uma sequência de números, calcule o maior valor da sequência.
# ATENÇÃO: não vale usar a função max() !

bigger = numbers[0]
for n in numbers:
    if n > bigger:
        bigger = n

print(f'The biggest element: {bigger}\n\n')

# Dado uma lista de palavras, printe todas as palavras
# com pelo menos 5 caracteres.

words = ['kauan', 'python', 'escrever', 'xxx']

for word in words:
    if len(word) >= 5:
        print(f'The word that have 5 characters: {word}')