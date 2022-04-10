timescamp = {} #sets são uma coleção de itens desordenada e dentro de colchetes {}
aprovados = [] #lista é representada como uma sequência de objetos separados por vírgula e dentro de colchetes []
reprovados = []

i = 0
qtd = 2

while i < qtd:
    timesjogando = str(input('Quais times jogando: '))
    golpro = int (input('Digite gol pro: '))
    golcontra = int (input('Digite gol contra: '))

    timescamp[timesjogando]=golpro,golcontra #criando uma lista "alunos" a partir de aluno digitado + nota digitada + serie
    i += 1

    
print(timescamp)
