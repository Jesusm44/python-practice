# numeros_positivos = 0

# while True:
#     numero = int(input("Ingresa un numero(Si ingresa un numero negativo se acaba el programa): "))
#     if numero < 0:
#         print("Ha terminado el programa.")
#         break
#     if numero  == 0:
#         continue 
#     numeros_positivos += 1

# print(f'La cantidad de numeros positivos son: {numeros_positivos} ')



# suma_numeros_pares = 0


# while True:
#     numero = int(input("Ingrese un numero: "))
    
#     if numero % 2 == 0:
#         suma_numeros_pares += numero
#         if suma_numeros_pares > 100:
#             break
#     else:
#         continue

# print("Ha terminado la suma de numeros.")


# numeros_validos = 0

# multiplos_siete = None
# anterior = None
# anterior_dos = None


# while True:
#     numero = int(input("Ingresa un numero (Si ingresa tres multiplos de siete se detiene el programa): "))
#     if  anterior is not None and anterior_dos is not None:
#         if numero % 7 == 0 and anterior % 7 == 0 and anterior_dos % 7 == 0:
#             print("Ingresaste tres numeros multiplos de siete")
#             break
#         if numero % 7 == 0:
#             continue     
#         else: 
#             numeros_validos += 1
#     anterior_dos = anterior
#     anterior = numero

    
# print(f'Numeros validos procesados: {numeros_validos}')


# cantidad_ingresados = 0
# cantidad_pares = 0

# numero_anterior = None
# ingresado_mayor = None

# while True:
#     numero = int(input("Ingrese un numero(Si ingresa un numero menor al anterior se acaba): "))
#     if numero_anterior is not None:
#         if numero_anterior > numero:
#             print("El programa se acabo porque ingreso un numero menor")
#             break
#         if numero % 2 == 0:
#             cantidad_pares += 1
#         if ingresado_mayor is None or ingresado_mayor < numero:
#             ingresado_mayor = numero
#     cantidad_ingresados += 1
#     numero_anterior = numero

# print(f'El numero mayor ingresado fue {ingresado_mayor}')
# print(f'Cantidad de pares ingresados {cantidad_pares}')



# cantidad_multiplos_tres = 0
# cantidad_positivos = 0

# numero_mayor = None
# numero_anterior = None


# while True:
#     numero = int(input("ingresa un numero(Si es igual al anterior se detiene el programa): "))
#     if numero_anterior is not None:
#         if numero == numero_anterior:
#             print("Los numeros son iguales")
#             break
#         if  numero > 0:
#             cantidad_positivos += 1
#         else: 
#             continue
#         if numero % 3 == 0:
#             cantidad_multiplos_tres += 1
#         if numero_mayor is None or numero_mayor < numero:
#             numero_mayor = numero
#     numero_anterior = numero


# print(f'La cantidad multiplos de tres ingresados son: {cantidad_multiplos_tres}')
# print(f'La cantidad de numero positivos son: {cantidad_positivos}')
# print(f'El numero mayor es: {numero_mayor}')


# numeros_ingresados = 0
# cantidad_de_ceros = 0

# anterior = None
# numero_anterior_dos = None
# numero_mayor = None

# while True:
#     numero = (int(input("Ingresa un numero el programa acaba (si ingresas un numero impar un numero par y un numero impar): ")))
#     if numero_anterior_dos is not None and anterior is not None:
#         if numero % 2 == 1 and anterior % 2 == 0 and numero_anterior_dos % 2 == 1:
#             print("Ha ingresado la secuencia indicada.")
#             break
#     if numero == 0:
#         cantidad_de_ceros += 1
#     if numero_mayor is None or numero_mayor < numero:
#         numero_mayor = numero
#     numero_anterior_dos = anterior
#     anterior = numero
#     numeros_ingresados += 1


# print(f'La cantidad de numeros ingresados fueron: {numeros_ingresados}')
# print(f'La cantidad de ceros ingresados: {cantidad_de_ceros}')
# print(f'El numero Mayor es: {numero_mayor}')


# cantidad_ingresos = 0
# multiplos_cuatro = 0
# cantidad_impares = 0

# numero_anterior = None
# numero_menor = None

# while True:
    # numero = int(input("Ingresa un numero (Si ingresas dos numeros pares y mayores a 50 se acaba se acaba el programa): "))
    # if numero_anterior is not None:
    #     if numero > 50 and numero % 2 == 0 and numero_anterior > 50 and numero_anterior % 2 == 0:
    #         print("Has cumplido la secuencia de dos numeros pares y mayores a 50")
    #         break
    #     else:
    #         if numero % 2 == 1:
    #             cantidad_impares += 1
    #         if numero % 4 == 0:
    #             multiplos_cuatro += 1
    #     if numero_menor is None or numero_menor > numero:
    #         numero_menor = numero
    #     cantidad_ingresos += 1
#     numero_anterior = numero

# print(f'La cantidad de numeros impares ingresados fueron: {cantidad_impares}')
# print(f'La cantidad de numeros ingresados fueron: {cantidad_ingresos}')
# print(f'Los multiplos de cuatro son: {multiplos_cuatro}')

# multiplos_cinco = 0
# cantidad_positivos = 0

# numero_mayor = None
# numero_anterior = None

# while True:
#     numero = int(input("Ingresa un numero (si ingresa un numero negativo y despues un numero impara acab el programa): "))
#     if numero_anterior is not None:
#         if numero < 0 and numero_anterior % 2 == 1:
#             print("Has cumplido la condicion")
#             break
#         if numero == 0:
#             continue
#         if numero % 5 == 0:
#             multiplos_cinco += 1
#         if numero_mayor is None or numero_mayor < numero:
#             numero_mayor = numero
#     cantidad_positivos += 1
#     numero_anterior = numero

# print(f'Los numeros multiplso de 5 son: {multiplos_cinco}')
# print(f'Los numeros positivos son: {cantidad_positivos}')
# print(f'El numero mayor es: {numero_mayor}')


# cantidad_numeros_ingresados = 0
# negativos_ingresados = 0
# numeros_mayores_cien = 0

# numero_anterior_uno = None
# numero_anterior_dos = None
# nuemero_menor = None

# while True:
#     numero = int(input("Ingresa un numero (Si ingresa un numero +,-,+ se acaba el programa): "))

#     if numero_anterior_uno is not None and numero_anterior_dos is not None:

#         if numero > 0 and numero_anterior_uno < 0 and numero_anterior_dos > 0:
#             print("Has cumplido la condicion")
#             break
#         if numero <= 0:
#             negativos_ingresados += 1
#         if numero > 100:
#             numeros_mayores_cien += 1
#         if nuemero_menor is None or nuemero_menor > numero:
#             nuemero_menor = numero

#     cantidad_numeros_ingresados += 1
#     numero_anterior_dos = numero_anterior_uno
#     numero_anterior_uno = numero

# print(f'La cantidad de numeros ingresados es: {cantidad_numeros_ingresados}')
# print(f'La cantidad de numeros negativos ingresados es: {negativos_ingresados}')
# print(f'La cantidad numeros mayores a cien son: {numeros_mayores_cien}')
# print(f'El numero menor es: {nuemero_menor}')


# numeros_validos = 0 
# pares_ingresados = 0 

# numero_anterior = None
# numero_mayor = None

# while True:
#     numero = int(input("Ingrese un numero(Si ingresa dos numeros menores a o iguales a cero acaba el progrma): "))

#     if numero_anterior is not None:

#         if numero <= 0:
#             print("Se ha cumplido la condicion")
#             break
#         if numero % 2 == 0:
#             pares_ingresados += 1
#         if numero_mayor is None or numero_mayor < numero:
#             numero_mayor = numero
    
#     numeros_validos += 1
#     numero_anterior = numero
    

# print(f'Los numeros validos ingresados son:{numeros_validos}')
# print(f'Los numeros pares son: {pares_ingresados}')
# print(f'El numero mayor es: {numero_mayor}')


# numeros_validos = 0
# multiplos_seis = 0 

# numero_menor = None
# numero_anterior = None

# while True:
#     numero = int(input("Ingresa un numero (Si ingresa dos - seguidos acaba el programa): "))

#     if numero_anterior is not None:
#         if numero < 0 and numero_anterior < 0:
#             print("Has cumplido la condicion")
#             break
#         if numero > 100:
#             continue
#         if numero % 6 == 0:
#             multiplos_seis += 1
#         if numero_menor is None or numero_menor > numero:
#             numero_menor = numero
#     if 0 <= numero < 100:
#         numeros_validos += 1
#     numero_anterior = numero

# print(f'Los numeros validos ingresados son: {numeros_validos}')
# print(f'Los numeros multiplos de 6 son: {multiplos_seis}')
# print(f'El numero menor es: {numero_menor}')
        

# contador_ingresados = 0
# contador_ceros = 0

# numero_anterior_uno = None
# numero_anterior_dos = None
# numero_mayor = None

# while True:

#     numero = int(input("Ingresa un numero (Si el numero ingresado es par par e impar" \
#                        "se detiene el programa): "))
    
#     if numero_anterior_uno is not None and  numero_anterior_dos is not None:
#         if numero_anterior_dos % 2 == 0 and numero_anterior_uno % 2 == 0 and numero % 2 == 1:
#             print("Ha cumplido la condicion.")
#             break
#         if numero_mayor is None or numero_mayor < numero:
#             numero_mayor = numero
#     if numero == 0:
#             contador_ceros += 1
            
#     contador_ingresados += 1
#     numero_anterior_dos = numero_anterior_uno
#     numero_anterior_uno = numero


# print(f'Los numeros ingresados fueron: {contador_ingresados}')
# print(f'Los nuemros 0 ingresados fueron: {contador_ceros}')
# print(f'El numero mayor es: {numero_mayor}')


# cont_numeros = 0
# mult_cuatro = 0

# num_anterior = None
# num_mayor = None

# while True: 
    
#     num = int(input("Ingresa un numero (Si ingresas un par y despues un impar" \
#                     "se detiene el programa): "))
    
#     if num_anterior is not None:
#         if num_anterior % 2 == 1 and num % 2 == 0:
#             print("Has cumplido la condicion") 
#             break
#         if num > 0:
#             if num_mayor is None or num_mayor < num:
#                 num_mayor = num
#             cont_numeros += 1
#         else:
#             continue
#         if num % 4 == 0:
#             mult_cuatro += 1
    

#     num_anterior = num

# print(f'Los numeros multiplos de 4 son: {mult_cuatro}')
# print(f'Los numeros positivos contados son: {cont_numeros}')
# print(f'El numero mayor es: {num_mayor}')


# num_validos_ingresados = 0

# sum_num_validos = None
# num_menor = None
# valido = None

# while True:

#     num = int(input("Ingrese un numero (Si el contador llega a 200 acaba):"))

#     if num < 0:
#         continue

#     if num > 50:
#         continue

#     if sum_num_validos is None:
#         if sum_num_validos + num > 200:
#             print("Has cumplido la condicion")
#             break

#     if sum_num_validos is None:
#         sum_num_validos = num
#     else:
#         sum_num_validos += num
    
#     if num_menor is None or num_menor > num:
#         num_menor = num
    
#     num_validos_ingresados += 1
    


# print(f'Los numeros ingresados validos son: {num_validos_ingresados}')
# print(f'La suma de los numeros fue: {sum_num_validos}')
# print(f'El numero menor es: {num_menor}')


# cant_numeros_ingresados = 0
# cant_ceros = 0

# num_anterior_uno = None
# num_anterior_dos = None
# num_menor = None

# while True:

#     num = int(input("Ingresa un numero: (si la secuencia es +, 0, + acaba el programa): "))
#     if num_anterior_dos is not None and num_anterior_uno is not None:
#         if num_anterior_dos > 0 and num_anterior_uno == 0 and num > 0:
#             print("Has cumplido la condicion")
#             break

#     if num == 0:
#         cant_ceros += 1

#     if num_menor is None or num_menor > num:
#         num_menor = num

#     num_anterior_dos = num_anterior_uno
#     num_anterior_uno = num
#     cant_numeros_ingresados += 1

# print(f'Las cantidades de ceros ingresados son: {cant_ceros}')
# print(f'las cantudades de numeros ingresados son: {cant_numeros_ingresados} ')
# print(f'El numero menor es: {num_menor}')
    