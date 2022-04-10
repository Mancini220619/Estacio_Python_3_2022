contador = 0

timespaulista = ["corinthians", "sao paulo", "palmeiras", "santos", "redbull", "ajax", "sao bernardo", "santo andre", "sao caetano", "guarani"]

while contador <= 1:
    print ('o contador esta em', contador)

    time1 = input ("digite o time 1: \n")
    if time1 in timespaulista:
        print(time1, "participa do torneio")

    time2 = input ("digite o time 2: \n")
    if time2 in timespaulista:
        print(time2, "participa do torneio")

    print ("******************* \n")
    print ("PLACAR DO JOGO")

    golprotime1 = int (input ('placar do time1: \n'))
    golprotime2 = int (input ("placar do time2: \n"))

    golcontratime1 = golprotime2
    golcontratime2 = golprotime1

    saldotime1 = (golprotime1 - golprotime2)
    print('saldo de gols', saldotime1, time1)

    saldotime2 = (golprotime2 - golprotime1)
    print('saldo de gols', saldotime2, time2)

    if golprotime1 > golprotime2:
        pontostime1 = 3
        print (time1 , 'venceu a partida')
    elif golprotime2 > golprotime1:
        pontostime2 = 3
        print (time2 , 'venceu a partida')
    elif golprotime1 == golprotime2:
        pontostime1 = 1
        pontostime2 = 1
        print ('houve empate')

    print ('pontos ganhos', golprotime1, 'para o time: ', time1)
    print ('pontos ganhos', golprotime2, 'para o time: ', time2)



    if contador == 2:
        break;
    contador += 1