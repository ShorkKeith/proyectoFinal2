#JUEGO DE ORDEN
import os
import time

def TUTORIAL():                     # TUTORIAL
    for i in range (4):
        os.system("cls")
        if i % 2==0:
            print("-_-_-_-_-_-_-_JUEGO DE ORDEN_-_-_-_-_-_-_-_-_-") 
            print("En el juego de orden tienes")
            print("que conseguir que todos los",end=" ")
            print("        1 2 3")
            print("los números en la mesa sean",end=" ")
            print("      A 1 1 1")
            print("1, indicando el punto según",end=" ")
            print("      B 1 1 1")
            print("la FILA y COLUMNA, como el",end=" ")
            print("       C 1 1 1")
            print("ejemplo de la derecha",end=" ")
            print("             -B2-")
        else:
            print("-_-_-_-_-_-_-_JUEGO DE ORDEN_-_-_-_-_-_-_-_-_-")
            print("En el juego de orden tienes")
            print("que conseguir que todos los",end=" ")
            print("        1 2 3")
            print("los números en la mesa sean",end=" ")
            print("      A 1 0 1" )
            print("1, indicando el punto según",end=" ")
            print("      B 0 0 0")
            print("la FILA y COLUMNA, como el",end=" ")
            print("       C 1 0 1")
            print("ejemplo de la derecha",end=" ")
            print("             -B2-")
        time.sleep(2)
    time.sleep(2)
    print("¿listo?")
    time.sleep(3)           # FIN TUTORIAL

def validar(rpta):          #VALIDACIÓN DE RPTA
    rpta = rpta.upper()
    if (rpta[0]=="A" or rpta[0]=="B" or rpta[0]=="C" or rpta[0]=="D" or rpta[0]=="E") :
        vera = True
    else:
        vera = False

    if vera:
        if rpta[1]=="1" or rpta[1]=="2" or rpta[1]=="3" or rpta[1]=="4" or rpta[1]=="5":
            vera = True
        else:
            vera = False

    return vera             #FIN DE VALIDACION RPTA


letras = "ABCDE"
Problema = "1111111011100011101111111"

ProblemaL = []

for x in Problema:
    ProblemaL.append(x)

a = 0
print ("     1  2  3  4  5")
for x in range(5):
    print (letras[x], " - ", end ='')
    for y in range(5):
        print (ProblemaL[(x*5+y)], " ", end = '')
    print ("")
    
while True:
    print (" Ingresa tu RPTA, primero LETRA Y NUMERO ")
    rpta = str(input())
    if validar(rpta):
        break
    else:
        print ("Tu rpta es invalida")
        print ("-------------------")

print (" P R O C E S A N D O . . . ")
time.sleep(2)

cambio = []

if rpta[0]=="A" or rpta[0]=="a":
    cambio.append("1")
if rpta[0]=="B" or rpta[0]=="b":
    cambio.append("2")
if rpta[0]=="C" or rpta[0]=="c":
    cambio.append("3")
if rpta[0]=="D" or rpta[0]=="d":
    cambio.append("4")
if rpta[0]=="E" or rpta[0]=="e":
    cambio.append("5")

cambio.append(rpta[1])

k = (int(cambio[0])*5)-(5-int(cambio[1]))-1

del cambio[:]
cambio.append(int(k))
cambio.append(int(k+1))
cambio.append(int(k-1))
cambio.append(int(k+5))
cambio.append(int(k-5))

print ("Iniciando cambio")
for n in cambio:
    print (n)
    if n>=0:
        if ProblemaL[n]=="1":
            ProblemaL[n]="0"
        else:
            ProblemaL[n]="1"


print ("     1  2  3  4  5")
for x in range(5):
    print (letras[x], " - ", end ='')
    for y in range(5):
        print (ProblemaL[(x*5+y)], " ", end = '')
    print ("")