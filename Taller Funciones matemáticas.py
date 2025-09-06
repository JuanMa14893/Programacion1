from itertools import product
K, M = map(int, input("Ingresa K y M separados por espacio: ").split())


listas = []
for _ in range(K):
    datos = list(map(int, input("-----------Ingresar la lista con su tamaño: ---------").split()))
    lista = datos[1:]  
    listas.append(lista)

def f(x):
    return x ** 2

combinaciones = product(*listas)

max_s = 0
for combinacion in combinaciones:
    suma = sum(f(x) for x in combinacion)
    s = suma % M
    if s > max_s:
        max_s = s

print("El valor máximo de S es:", max_s)
