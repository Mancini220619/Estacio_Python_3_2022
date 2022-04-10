#toda expressao logica gera um booleano
a = 1
b = 1
print(a==b)

xpto = 1==1
print(xpto)

a = 2==1
print(a)

#desvio condicional

ddd = int(input("valor: \n"))
if ddd > 10:
    print ('numero maior que 10')
elif ddd < 0:
    print ('numero negativo menor que zero')
else:
    print ('numero esta entre 1 e 10')