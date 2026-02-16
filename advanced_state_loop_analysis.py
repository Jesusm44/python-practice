# numero_mayor = None

# for numero in range(5):
#     numero = int(input("Ingresa 5 numeros: "))
#     if numero_mayor is None or numero > numero_mayor:
#         numero_mayor = numero

# print(f'El numero mayor es: {numero_mayor}')


# numero_mayor = None
# numero_menor = None
# numero = int(input('Ingres un numero (Cuando ingrese un numero negativo): '))

# while numero > -1:
#     if numero_mayor is None or numero > numero_mayor:
#         numero_mayor = numero
#     if numero_menor is None or numero_menor > numero:
#         numero_menor = numero
#     numero = int(input('Ingres otro numero (Cuando ingrese un numero negativo): '))

# print(f'El numero amyor es: {numero_mayor}')
# print(f'El numero menor es: {numero_menor}')


numeros_mayores_diez = 0
numero_mayor = None
numero_anterior = None
numero_anterior_dos = None

while True:
    numero = int(input(f'Ingrese un numero(Si ingresa tres 0 seguidos se detiene el programa): '))
    if numero == 0 and numero_anterior == 0 and numero_anterior_dos == 0:
        print("Has ingresado los tres 0 has salido del bucle")
        break
    if numero > 10:
        numeros_mayores_diez += 1
    if numero_mayor is None or numero > numero_mayor:
        numero_mayor = numero
    numero_anterior_dos = numero_anterior
    numero_anterior = numero
            
print(f'Los numeros mayores a 10 son: {numeros_mayores_diez}')
print(f'El numero mayor es: {numero_mayor}')
            



