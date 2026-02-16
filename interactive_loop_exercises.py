# x = 0

# while x <= 31:
#     if x % 5 == 0:
#         print(x)
#     x += 1


# y = 50

# while y >= -1:
#     y -= 4
#     print(y)

# num1 = int(input("Ingresa un Numero real: "))
# sum = 0
# z = 0

# while z >= 0:
#     x = input(f'Seguir = 1, Parar = 0')
#     if x == "1":
#         sum += num1
#         y = int(input("Ingresa un Numero real: "))
#         sum += y
#     if x == "0":S
#         print(sum)
#         break
#     else:
#         print("ERROR: Ingresa el numero 1 o 0")
#     z += 1

# suma = 0 
# num = int(input("Ingresa otro numero (0 para terminar): "))

# while num != 0:
#     suma += num
#     num = int(input("Ingresa otro numero (0 para teminar): "))

# print(f'La suma total es: {suma}')


# suma_Edades1 = 0
# suma_Edades2 = 0
# edades = int(input("Ingresa una edad (si es una edad negativa se acaba): "))

# while edades >= 0:
#     if edades >= 18:
#         suma_Edades1 += 1
#     else:
#         suma_Edades2 += 1
    
#     edades = int(input("Ingresa otra edad (negativa para terminar): "))

    
# print(f'La suma total de las edades positivas son: {suma_Edades1}')
# print(f'La suma total de las edades positivas son: {suma_Edades2}')       


# suma_de_enteros_positivos = 0
# num_enteros = int(input("Ingresa un numero entero (termina cuando el usuario ingrese el 0):"))
# x = 0

# while num_enteros > 0:
#         suma_de_enteros_positivos += 1
#         x += num_enteros
#         num_enteros = int(input("Ingresa un numero entero (termina cuando el usuario ingrese el 0):"))
        

# print(f'La suma de la cantidad de los numeros enteros positivos es: {suma_de_enteros_positivos}')
# print(f'La suma de numeros enteros positivos es: {x}')



# numeros_pedidos = int(input("Ingrese un Numero real (Cuando ingrese el 0 se acaba): "))
# cantidades_pares = 0
# suma_de_los_numeros = 0

# while numeros_pedidos > 0:
#     if numeros_pedidos % 2 == 0:
#         cantidades_pares += 1
#         suma_de_los_numeros += numeros_pedidos
#         numeros_pedidos = int(input("Ingresa otro numero entero (termina cuando el usuario ingrese el 0):"))
#     elif numeros_pedidos % 2 == 1:
#         numeros_pedidos = int(input("Ingresa otro numero entero (termina cuando el usuario ingrese el 0):"))
#         numeros_pedidos += 0

# print("La cantidad de numeros pares sumados son: ", cantidades_pares)
# print("La suma de los numeros pares son: ", suma_de_los_numeros)


# edades = int(input("Ingrese una edad (Si ingresa una edad negativa se acaba):"))
# contador_mayor_de_edad = 0
# contador_menor_de_edad = 0

# while edades > 0:
#     if edades >= 18:
#         contador_mayor_de_edad += 1
#         edades = int(input("Ingrese otra edad (Si ingresa una edad negativa se acaba):"))
#     else:
#         contador_menor_de_edad += 1
#         edades = int(input("Ingrese otra edad (Si ingresa una edad negativa se acaba):"))


# print(f'La suma de edades mayores de edad {contador_mayor_de_edad}')
# print(f'La suma de edades menores de edad {contador_menor_de_edad}')


# for i in range (7,100,7):
#     print(i)

# suma_cantidad_par = 0
# suma_cantidad_impar = 0

# for i in range(0,50):
#     if i % 2 == 0:
#         suma_cantidad_par += 1    
#     else:
#         suma_cantidad_impar += 1

# print(f'La cantidad de numeros pares son: {suma_cantidad_par}')    
# print(f'La cantidad de numeros impares son: {suma_cantidad_impar}')    


# print(f'Tienes 3 intentos para hallar el numero, incognito, en cada intento debes ingresar un numero')
 
# numero_ingresado = int(input(f'Ingresa un numero al azar tienes 3 intentos, todos los numeros son validos excepto el 0: '))
# numero_incognito = 7
# intentos = 0
# intentos_resta = 3

# while intentos < 3:
#     if numero_ingresado != numero_incognito:
#         intentos_resta -= 1
#         numero_ingresado = int(input(f'Ingresa otro numero al azar te quedan {intentos_resta} intentos: '))
#         if intentos_resta == 0:
#             print(f'Fallaste: Te quedaste sin intentos')
#     else:
#         print(f'Correcto')  
#         intentos += 3
#     intentos += 1

# print(f'Ingrese un numero de usaurio, terminara cuando el usaurio ingrese dos ceros seguidos')

# numeros_ingresados = int(input(f'Ingrese un numero (si ingresa 00 se acaba el programa): '))
# contador_ingresos = 0
# numero_anterior = 0
# contador_de_ceros = 0


# while  True:
#     if numero_anterior == 0 and numeros_ingresados == 0:
#         print("Has salido del bucle ")
#         break 
#     else:
#         contador_ingresos += 1
#         if numeros_ingresados == 0:
#             contador_de_ceros += 1
#         numero_anterior = numeros_ingresados
#         numeros_ingresados = int(input(f'Ingrese otro numero (si ingresa 00 se acaba el programa): '))

# print(f'Los numero ingresados son {contador_ingresos}')
# print(f'los ceros ingresados son {contador_de_ceros}')


# print(f'El usuario ingresara numeros, el programa se va a acabar cuando el usuario coloque un numero negativo')

# numero_usuario = int(input(f'Ingrese un numero (Si el usuario ingresa un numero negativo se acaba): '))
# numeros_validos = 0
# numeros_pares = 0
# numeros_impares = 0


# while True:
#     if numero_usuario < 0:
#         print(f'Se acabo el programa, ha ingresado un numero negativo')
#         break
#     else:
#         numeros_validos += 1
#         if numero_usuario % 2 == 0:
#             numeros_pares += 1
#         else:
#             numeros_impares += 1
#         numero_usuario = int(input(f'Ingrese un numero (Si el usuario ingresa un numero negativo se acaba): '))
        
    
# print(f'Los numeros mayores o iguales a 0 fueron: {numeros_validos}')
# print(f'Los numeros pares ingresados fueron: {numeros_pares}')
# print(f'Los numeros impares ingresados fueron: {numeros_impares}')

        



        



    
        



         


