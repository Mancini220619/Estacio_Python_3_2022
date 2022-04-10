from tkinter import N


frutas = ["maça", "banana", "cereja"]
for x in frutas:
  print(x)


notas = {
'Portugues': 7, 
'Matemática': 8, 
'Geografia': 10 
}
for chave, valor in notas.items ():
    print(f"{chave}: {valor}")



#formas de desviar do laço
for num in range(5):
    if num == 3:
        print('achei o numero 3')
        continue
    print('passou do if')



i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("o limite é 5")

print("*****")

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)