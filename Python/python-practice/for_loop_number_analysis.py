# for i in range(10,0,-1):
#     print(i, end = " ")
# print()

# for i in range(3,31,3):
#     print(i, end = " ")
# print()

# suma = 0
# for i in range (1,101):
#     suma += i
# print(suma)


# numeros_pares = 0 

# for i in range(2,51,2):
#         numeros_pares += 1
# print(numeros_pares)


# numeros_impares = 0

# for i in range(1,101):
#     if i % 2 == 1:
#         numeros_impares += i
# print(numeros_impares)

# for i in range(1,31):
#     if i % 2 == 0:
#         print(f'El numero {i}, es par')
#     else:
#         print(f'El numero {i}, es impar')


# contador_pares = 0
# contador_multiplos_cinco = 0


# for i in range(1,101):
#     if i % 2 == 0:
#         contador_pares += 1 
#     if i % 5 == 0:
#         contador_multiplos_cinco += 1

# print(f'Los numeros pares son: {contador_pares}')
# print(f'Los numeros multiplos de cinco son: {contador_multiplos_cinco}')
        
        
# for i in range(1,101):
#     if i % 3 != 0  and i % 5 != 0:
#         print(f'Los numeros que no son multiplos ni de 3 ni de 5 son {i}')


numeros_pares = 0 
numeros_impares = 0
multiplos_tres = 0
multiplos_cinco = 0
no_multiplos = 0


for i in range(1,201):
    if i % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1
    if i % 3 == 0:
        multiplos_tres += 1
    if i % 5 ==  0:
        multiplos_cinco += 1
    if i % 5 != 0 and i % 3 != 0:
        no_multiplos += 1

print(f'La cantidad de numeros pares son: {numeros_pares}')
print(f'La cantidad de numeros impares son {numeros_impares}')
print(f'La cantidad de numeros multiplos de tres son: {multiplos_tres}')
print(f'La cantidad de numeros multiplo de cinco son: {multiplos_cinco}')
print(f'La cantidad de numeros que no son multiplos de cinco ni de tres son: {no_multiplos}')