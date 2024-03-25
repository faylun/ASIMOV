# Desafio - crie um programa que:
# - Escolhe um número secreto.
# - Pede por um chute do usuário.
# - Indica se o usuário acertou ou não.
# - Se não acertou, dá uma dica, dizendo
#   - se o número é mais alto ou mais baixo.
# - Repete isso até 3 vezes!

secret_number = 10
find = False

for n in range(3):
    if not find:
        kick = int(input('Write a number from 0 to 10: '))

        if kick < 10:
            print('Kick was smaller than the secret number.')
        elif kick > 10:
            print('Kick was bigger than the secret number.')
        else:
            find = True
            break
if find:
    print(f"CONGRATULATIONS!! You WIN, the number was {secret_number}")
else:
    print(f'You Lost!, the number was {secret_number}')