# Crie um código que implementa a "Cifra de César", isto é, que
# transforma um string movendo cada letra um certo número de
# passos no alfabeto. O número de passos é dado por uma chave.
# Letra com acentos, espaços e pontuação permanecem iguais.

# Exemplos:
# "abc" com chave 1 = "bcd"
# "ABCDE" com chave 2 = "CDEFG"
# "Cachorro" com chave -1 = "Bzbgnqqn"
# "Olá Mundo!" com chave 3 = "Roá Pxqgr!"

# DICA: construa 2 strings com as letras do alfabeto em ordem,
# um para letra minúsculas e outra para as maiúsculas, e use este
# string para guiar as substituições.

def cipher_character(character, seq, key):
    new_index = seq.index(character) + key

    # Checking if the key is bigger than text
    while new_index >= len(seq):
        new_index -= len(seq)

    # Checking if the key is smallest than text
    while new_index < 0:
        new_index += len(seq)

    return seq[new_index]

text = 'meu nome é kauan!!'

lowerCase = 'abcdefghijklmnopqrstuvwxyz'
upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 27
cipher = ''

for charac in text:
    if charac in lowerCase:
        character_cipher = cipher_character(charac, lowerCase, key)
    elif charac in upperCase:
        character_cipher = cipher_character(charac, upperCase, key)
    else:
        character_cipher = charac
    cipher += character_cipher
    
print(cipher)