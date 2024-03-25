# Crie um "jogo dos estados". Neste jogo, o jogador precisa responder
# o nome da capital de cada Estado do Brasil. O jogo deve perguntar
# ao usuário "Qual a capital do Estado X?", e checar se o usuário
# respondeu de forma correta. Após cada pergunta, o usuário pode escolher
# parar o jogo ou continuar para a próxima pergunta. Quando o usuário
# decidir parar, ou quando todas as perguntas forem respondidas,
# o código mostra o número bruto e porcentagem de acertos.

capitais = {
    "Acre" : "Rio Branco",
    "Alagoas" : "Maceió",
    "Amapá" : "Macapá",
    "Amazonas" : "Manaus",
    "Bahia" : "Salvador",
    "Ceará" : "Fortaleza",
    "Distrito Federal" : "Brasília",
    "Espírito Santo" : "Vitória",
    "Goiás" : "Goiânia",
    "Maranhão" : "São Luís",
    "Mato Grosso" : "Cuiabá",
    "Mato Grosso do Sul" : "Campo Grande",
    "Minas Gerais" : "Belo Horizonte",
    "Pará" : "Belém",
    "Paraíba" : "João Pessoa",
    "Paraná" : "Curitiba",
    "Pernambuco" : "Recife",
    "Piauí" : "Teresina",
    "Rio de Janeiro" : "Rio de Janeiro",
    "Rio Grande do Norte" : "Natal",
    "Rio Grande do Sul" : "Porto Alegre",
    "Rondônia" : "Porto Velho",
    "Roraima" : "Boa Vista",
    "Santa Catarina" : "Florianópolis",
    "São Paulo" : "São Paulo",
    "Sergipe" : "Aracaju",
    "Tocantins" : "Palmas",
}

hitCont = 0
for state in capitais:
    user = str(input(f'What is the {state} state capital? ')) == capitais[state].lower()

    if user:
        print('Congratulations!! You are right!')
        hitCont += 1
    else:
        print('Hmmm, you wrong! Sorry...')

    leav = str(input('Do you wanna leave? ( Y/N )'))[0].lower() == 'y'

    if leav:
        break
print(f'correct answers: {hitCont}')
print(f'correct answers percents: {(hitCont / len(capitais)) * 100:.2f}%')