#vetor

s = "olá mundo"
print ("Silling")

print(s[0]) #primeiro
print(s[1])
print(s[2])
print(s[6])

print(s[-1])
print(s[-2])
print(s[-4])

print(s[1:3])
print(s[:3])
print(s[::2]) #imprime os caracteres nos indices pares
print(s[1::2]) #imprime os caracteres nos indices impares

print (1+2+3+4) #o python soma
print(123, "python \n") #com virgula ele compoe string 



frase = "se a canoa nao virar {1} o pau vai quebrar {0}".format("oleoleolá","denovo") #usando o format ordem '0' ou '1'
print (frase)

frase2 = "se a canoa nao virar {0} o pau vai quebrar {1}".format("oleoleolá","denovo") #usando o format ordem '0' ou '1'
print (frase2)




#usando split transforma em lista 
txt = "welcome to the jungle"
x = txt.split()
print(x)



#usando for
frutas = ["apple", "banana", "cherry", "lemon"]
for x in frutas:
  print(x)


# comparando listas
l1 = [1,2,3,6]
l2 = [3,2,5,6 ]
for i in l1:
    for j in l2:
        if(i==j):
            print(i)
            break


#pesquisar palavra chave dentro de uma frase
import re
txt = "The rain in Spai, sabia eu sabiail"
x = re.findall("ai", txt)
print(x)