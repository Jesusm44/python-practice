# numero_mayor = None
# num_positivos_ingresados = 0

# while True:
     
#      num = int(input("Ingrese un numero (" \
#      "si ingresa un numero negativo acaba el programa): "))

#      if num < 0:
#           print("Has cumplido la condicion")
#           break
     
#      if num == 0:
#           continue
     
#      if num > 0:
#           num_positivos_ingresados += 1
     
#      if numero_mayor is None or numero_mayor < num:
#           numero_mayor += num

# print(F'El numero mayor es: {numero_mayor}')
# print(f'La cantidad de numeros positivos es: {num_positivos_ingresados}')


# num_anterior = None

# cant_positivos = 0
# cant_pares = 0

# while True:

#     num = int(input("Ingrese un numero(Si ingresa dos numeros iguales" \
#     "el programa acaba): "))

#     if num_anterior is not None:
#         if num_anterior == num:
#             print("Ha cumplido la condicion")
#             break
#     if num < 0:
#         continue

#     if num > 0:
#         cant_positivos += 1

#     if num % 2 == 0 and num :
#         cant_pares += 1
    
    

#     num_anterior = num

# print(f'La cantidad de numeros positivos son: {cant_positivos}')
# print(f'La cantidad de numeros pares son: {cant_pares}')

# cont_impares = 0 

# comp_cero = False

# while True:
#     num = int(input("Ingrese un numero(Si ingresa un numero negativo" \
#     "despues de un cero se acaba el programa): "))

#     if  num == 0:
#         comp_cero = True
#         continue

#     if  num < 0:
#         if comp_cero:
#             print("Has cumplido la condicion")
#             break

#     if comp_cero:
#         if num % 2 == 0:
#             continue
#         else: 
#             cont_impares += 1
        

# print(f'La cantidad de numeros impares es: {cont_impares}')


# num_impares = 0

# num_anterior = None
# flag = False

# while True:
    
#     num = int(input("Ingrese un numero (Si ingresa un numero negativo" \
#     "el programa acaba):"))

#     if num < 0:
#         if flag:
#             print("Ha cumplido la condicion")
#             break
#         else:
#             flag = True
#             continue

#     if flag:
#         if num % 2 == 0:
#             continue
#         else:
#             if num > 0 and num % 2 == 1:
#                 num_impares += 1

#     num_anterior = num
    
# print(f'Los contadores de impares son {num_impares}')
    


# demas_num = 0

# bandera_off = False

# while True:
    
#     num = int(input("Ingrese un numero (Si ingresa un numero negativo despues del cero" \
#     "se acaba el programa): "))

#     if num < 0:
#         if bandera_off:
#             print("Has cumplido la condicion")
#             break
#         else:
#             bandera_off = True
#             continue

#     if num == 0:
#         bandera_off = True
#         continue

#     if bandera_off:
#         if num % 3 == 0:
#             continue
#         else:
#             demas_num += 1


# print(f'Los numeros contados son')


# cont_impares = 0

# num_anterior = None
# bandera = False

# while True:

#     num = int(input("Ingrese un numero: (Si el numero viene seguido de un" \
#     "par y un impar y se coloca un numero negativo se acaba el programa): "))

#     if num_anterior is not None:

#         if num < 0:
#             if bandera:
#                 print("Has cumplido la condicion")
#                 break
#             else:
#                 bandera = True
#                 continue

#         if num_anterior % 2 == 0 and num % 2 == 1:
#             bandera = True
#             continue

#         if bandera:
#             if num % 2 == 0:
#                 continue
#             else:
#                 cont_impares += 1
 
#     num_anterior = num

# print(f'Los numeros impares son: {cont_impares}')


# max_num = None
# bandera = False

# num_valido = 0

# while True:

#     num = int(input("Ingrese un numero (Si el numero mayor es 100 y coloca un numero negativo" \
#     "se acaba el programa): "))

#     if num < 0:
#         if bandera:
#             print("has cumplido la condicion.")
#             break
#         else:
#             bandera = True
#             continue

#     if max_num is None:
#         max_num = num
       
#     if max_num > 100:
#         bandera = True
#         continue
    
#     if bandera:
#         max_num = 100

#     num_valido += 1


# print(f'Los numeros validos son: {num_valido}')    


# count_even = 0

# flag = False

# while True:

#     number = int(input("Ingrese un numero (Si el numero es menor que el anterior se activa" \
#     "la bandera): "))

#     if number < 0:
#         if flag:
#             print("Has cumplido la condicion se ha cumplido.")
#             break
#         else:
#             flag = True
#             continue

#     if flag:
#         if number % 2 == 0:
#             continue
#         else:
#             count_even

# print(f'los numeros pares ingresados son: {count_even}')





    

    
    






        
