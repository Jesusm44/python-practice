# numero_valido = 0

# while True:
#     numero = int(input("Ingresa un numero: "))
#     if numero == -1:
#         break
#     else:
#         numero_valido += 1

# print(f'La cantidad de numeros validos ingresados fueron {numero_valido}')


# anterior = None

# while True:
#     actual = int(input("Ingresa un numero: "))
#     if anterior == actual:
#         print("Se ha repetido 2 veces el mismo numero.")
#         break
#     anterior = actual

# multiplos_cuatro = 0
# multiplos_seis = 0
# multiplos_ambos = 0

# for i in range(1,300):
#     if i % 4 == 0:
#         multiplos_cuatro += 1
#     if i % 6 == 0:
#         multiplos_seis += 1
#     if i % 6 == 0 and i % 4 == 0:
#         multiplos_ambos += 1

# print(f'Los multiplos de 4 son: {multiplos_cuatro}')
# print(f'Los multiplos de 6 son: {multiplos_seis}')
# print(f'Los multiplos de ambos son: {multiplos_ambos}')


# for i in range(1,50):
#     if i % 3 == 0:
#         continue
#     if  i == 37:
#         break
#     print(i)

# numero_anterior = None
# numero_anterior_dos = None
# numeros_ingresados = 0
# numeros_pares = 0
# numeros_impares = 0


# while True:
#     numero = int(input("Ingrese un numero (Si ingresas el numero 3 veces se detiene el programa): "))
#     if numero == numero_anterior and numero == numero_anterior_dos:
#         print(f'Has salido del bucle ')
#         break
#     else:
#         if numero % 2 == 0:
#             numeros_pares += 1
#         elif numero % 2 == 1:
#             numeros_impares += 1
#         numeros_ingresados += 1
#     numero_anterior_dos = numero_anterior
#     numero_anterior = numero
        
# print(f'La cantidad de numeros ingresados fueron: {numeros_ingresados}')
# print(f'La cantidad de numeros pares fueron: {numeros_pares}')
# print(f'La cantidad de numeros impares fueron: {numeros_impares}')


cantidad_ingresados = 0
cantidad_impares = 0 
ceros_ingresados = 0
numero_anterior = None
numero_mayor = None
cantidad_ceros = 0

while True:
    numero = int(input("Ingrese un numero (Si ingresa dos numeros pares seguido acaba): "))
    
    if numero_anterior is not None:
        if numero % 2 == 0 and numero_anterior % 2 == 0:
            break
    else:
        if numero == 0:
            cantidad_ceros += 1
        elif numero % 2 == 1:
            cantidad_impares += 1
    if numero_mayor is None or numero > numero_mayor:
        numero_mayor = numero
        
    cantidad_ingresados += 1
    numero_anterior = numero
        
print (f'Numeros ingresados: {cantidad_ingresados}')
print(f'Numeros impares: {cantidad_impares}')
print(f'Cantidad de ceros: {cantidad_ceros}')
print(f'El numero mayor ingresado es {numero_mayor}')