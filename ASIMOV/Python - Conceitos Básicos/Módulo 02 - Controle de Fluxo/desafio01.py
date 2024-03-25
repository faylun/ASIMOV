# Desafio - crie um programa que:
# - Pede por um nome de usuário e uma senha.
# - Se ambos forem corretos, exibe uma mensagem de sucesso.
# - Caso contrário, exibe uma mensagem de erro. A mensagem é diferente
# quando o usuário está incorreto, e quando a senha está incorreta
# - O usuário/senha "corretos" podem ser definidos como
# variávies dentro do próprio código.

user_true = 'Kauan'
password_true = '1234'

user = str(input('Write your user: ')) == user_true
password = str(input('Write your password: ')) == password_true

if user and password:
    print('Sucess!')
else:
    if not user:
        print('Incorrect user.')
    else:
        print('Incorrect password.')
