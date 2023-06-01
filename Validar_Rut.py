#Import math Library
import math
lista = []
for i in range (8):
  print("Ingrese el " + str(i+1) + "°" + " dígito de su rut: (va antes del guión y sin puntos)")
  rut = int(input("RUT: "))
  lista.append(rut)
  print(str(lista))

lista.reverse()
print(lista)
print("Multiplicación por serie:")
a = lista[0]*2
print(a)
b = lista[1]*3
print(b)
c = lista[2]*4
print(c)
d = lista[3]*5
print(d)
e = lista[4]*6
print(e)
f = lista[5]*7
print(f)
g = lista[6]*2
print(g)
h = lista[7]*3
print(h)

print("")
print("Suma de los resultados:")
suma_lista = a + b + c + d + e + f + g + h
print(suma_lista)
print("")
print("División por 11:")
resto = math.trunc(suma_lista/11)
print(resto)
print("")
print("Multiplicación por 11:")
multi = resto*11
print(multi)
print("")
print("Resta entre la suma anterior y el producto:")
resta = abs(suma_lista - multi)
print(resta)
print("")
print("Resta de 11 al resultado anterior:")
resta_final = 11 - resta
print(resta_final)

if resta_final == 11:
  print("El dígito verificador es 0.")
elif resta_final == 10:
  print("El dígito verificador es K.")
else:
  print("El dígito verificador es " + str(resta_final) + ".")
