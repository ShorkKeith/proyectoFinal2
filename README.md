# ejemplo2

Aquí se consolidarán el resto de branches.
print("identificar cuantos numeros son 0 y 1")
print("Lista:")
lista = [ ]
for i in range(5) :
    num=int(input("ingrese numero"))
    lista.insert(i,num)
n=1
for x in lista:
    n=int(x)*n
if n==1:
        print(" todos son 1")
else:
        print(" almenos existe un 0 en la lista")

