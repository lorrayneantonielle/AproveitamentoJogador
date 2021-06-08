time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador["nome"] = str(input('Qual o nome do jogador? '))
    total = int(input(f"Quantas partidas foram jogadas por {jogador['nome']}? "))
    partidas.clear()
    for c in range(1, total+1):
        partidas.append(int(input(f'Quantos gols foram feitos na {c}° partida? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
            print('ERRO! Responda apneas S ou N.')
    if resposta == 'N':
        break
print('=-' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('=-' * 30)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):>15}', end='')
    print()
print('-=' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código da {busca}!')
    else:
        print(f' LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f' No jogo {i+1} fez {g} gols.')
    print('-=' * 30)
print('VOLTE SEMPRE')