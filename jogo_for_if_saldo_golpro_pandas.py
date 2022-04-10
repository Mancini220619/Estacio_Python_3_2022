import pandas as pd
listaJogos = []
for i in range(3):
  jogo = input ('Qual o jogo? ')
  gp = int (input ('Quantos gols pró? '))
  gc = int (input ('Quantos gols contra? '))
  saldo = gp -gc 
  ponto = 0
  if saldo > 0:
    ponto = 3
  elif saldo == 0:
    ponto = 1
  listaJogos.append((jogo, gp,gc,saldo,ponto))
  
df = pd.DataFrame(listaJogos, columns= ['Lista de Jogos', 'GP', 'GC', 'Saldo','Pontos'])
print (df)