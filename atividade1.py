numeros = [0,1,2,5,-7,4,3,8,-12,24,88]

maior_numero = numeros[0]
menor_numero = numeros[0]

for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero

print("O maior numero da lista é:", maior_numero)
print("O menor numero da lista é:", menor_numero)