# miscelanea de ejercicios en phyton


# importar la función pi de math para poder hacer algunas operaciones.
from math import pi



while True:
    # realiza un ciclo donde muestra las 4 opciones principales para que el usuario elija cual necesita.
    print \
        ("MENU. \n1.Operadores. \n2.Condicionales. \n3. ciclos \n4.salir. (marque el número (99) si desea salir del programa.) ")
    menu = int(input("Digite la opción que desea usar: "))
    if menu == 1:
        # crea un submenu con las opciones de operadores para que el usuario elija.

        while True:

            # El primer submenu permite hacer operaciones que salen en el primer print (OPERADORES)
            print(
                "OPERADORES: \n Opciones \n 1. Calcular el area de un triangulo. \n 2. Ingrese dos numeros y se sumaran. \n 3. Eleva un número al cuadrado. \n 4. Convertir de Euros a Dolares. \n 5. Sacar el area y perimetro de un cuadrado.  "
                "\n 6. Sacar el área y vólumen de un cilindro. \n 7. Sacar el promedio de 3 numeros ingresados.\n 8. Sacar la longitud y el area de una circunferencia. \n 9. Salir.")
            operadores = int(input("Dgite la operación que desea usar: "))
            while operadores == 1:
                eleccion = int(
                    input("escriba '1' si desea usar esta opción o volverla a usar, si no desea salir escriba '2' "))
                if eleccion == 1:
                    # Se calcula el area de un triangulo con los datos ingresados por el usuario.
                    print("calcularemos el area de un triangulo: ")

                    base = float(input("digite la base del triangulo en cm: "))

                    height = float(input("digite la altura del triangulo en cm: "))

                    area = base * height / 2

                    print(f"el area del triangulo es igual a {area} cm²")
                elif eleccion == 2:
                    break

            while operadores == 2:
                eleccion1 = int(
                    input("escriba '1' si desea usar esta opción o volverla a usar, si no desea salir escriba '2' "))
                if eleccion1 == 1:
                    # Sumamos dos numeros ingresados por el usuario.
                    print("sumaremos dos numeros que ingrese: ")
                    sum = (input("ingrese los dos numeros que desea  sumar: "))
                    sum1 = int(sum[0])
                    sum2 = int(sum[1])

                    print((sum[0]), "+", (sum[1]), "=", sum1 + sum2)

                elif eleccion1 == 2:
                    break
            while operadores == 3:
                eleccion2 = int(
                    input("escriba '1' si desea usar esta opción o volverla a usar, si no desea salir escriba '2' "))
                if eleccion2 == 1:
                    # Se eleva al cuadrado un numero que ingrese el usuario.
                    print("elevaremos un numero al cuadrado: ")
                    num = float(input("digite el número que quiere elevar al cuadrado: "))
                    elevado = num ** 2
                    print(f"el numero digitado al cuadrado es: {elevado} ")
                elif eleccion2 == 2:
                    break
            while operadores == 4:
                eleccion3 = int(
                    input("escriba '1' si desea usar esta opción o volverla a usar, si no desea salir escriba '2' "))
                if eleccion3 == 1:
                    # Se convierte en dolares los euros que dijita el usuario.
                    dolar = 0.91
                    euros = float(input("Digite los euros que desea convertir en dolares: "))

                    dolares = euros / dolar
                    print(f"{euros} euros equivalen a ", round(dolares, 2), " dolares")
                elif eleccion3 == 2:
                    break
            while operadores == 5:
                eleccion4 = int(
                    input("escriba '1' si desea usar esta opción o volverla a usar, si no desea salir escriba '2' "))
                if eleccion4 == 1:
                    # Sacamos el perimetro y el area de un cuadrado con el lado que nos da el usuario.
                    print("Vamos a sacar primero el perimetro y luego el area del cuadrado")

                    side = int(input("Digite la medida de un lado del cuadrado en cm: "))

                    area = side * side
                    perimeter = side + side + side + side

                    print(f"El perimetro del cuadrado es {perimeter} cm y su area es {area} cm²")
                elif eleccion4 == 2:
                    break

            while operadores == 6:
                eleccion5 = int(
                    input("escriba '1' si desea usar esta opción o volverla a usar, si no desea salir escriba '2' "))

                if eleccion5 == 1:
                    # Sacamos el area y volumen de un cilindro despues de pedirle ciertos datos al usuario para hacerlo.
                    print("Vamos a sacar el area y volumen de un cilindro ")

                    radius = float(input("Digite el radio del cilindro: "))
                    height1 = float(input("Digite la altura del cilindro: "))

                    area = 2 * pi * radius ** 2 + 2 * pi * radius * height1

                    volume = pi * radius ** 2 * height1

                    print(f"el area del cilindro es: {round(area, 2)} y el volumen del cilindro es: {round(volume, 2)}")
                elif eleccion5 == 2:
                    break

            while operadores == 7:
                eleccion6 = int(
                    input("escriba '1' si desea usar esta opción o volverla a usar, si no desea salir escriba '2' "))
                if eleccion6 == 1:
                    # Sacamos el promedio con 3 numeros digitados por el usuario.
                    print("Vamos a sacar el promedio de 3 numeros que ingreses. ")
                    prom1 = float(input("ingrese el primer número: "))
                    prom2 = float(input("ingrese el segundo número: "))
                    prom3 = float(input("ingrese el tercero número: "))

                    promedio = (prom1 + prom2 + prom3) / 3

                    print(f"El promedio de los tres numeros digitados es: {round(promedio, 2)}")
                elif eleccion6 == 2:
                    break
            while operadores == 8:
                eleccion7 = int(
                    input("escriba '1' si desea usar esta opción o volverla a usar, si no desea salir escriba '2' "))
                if eleccion7 == 1:
                    # Calculamos la longitud y area de una cricunferencia despues de pedirle el radio.
                    print("vamos a calcular la longitud y area de una circunferencia.")
                    radius1 = float(input("digite el radio de la circunferencia: "))

                    lenght = 2 * radius1 * pi
                    area1 = pi * radius1 ** 2

                    print(
                        f"el area de la circunferencia es: {round(area1, 2)} y la longitud del mismo es: {round(lenght, 2)}")
                elif eleccion7 == 2:
                    break

            if operadores == 9:
                break
    elif menu == 2:
        while True:
            # El segundo submenu permite hacer los condicionales que se encuentra en el print (CONDICIONALES)
            print(
                "CONDICIONALES: \n Opciones \n 1. Saber si un número es positivo o negativo. \n 2. Saber cual número es mayor y menor. \n 3. Calcular entre tres numeros enteros positivos cual es mayor y menor. \n 4. Dados dos números A y B, sumarlos si A es menor que B o sino restarlos. "
                "\n 5. Dados dos números A y B encontrar el cociente entre A y B. \n 6. Dados dos números A y B, sumarlos si al menos uno de ellos es negativo, en caso contrario multiplicarlos. \n 7. Saber si un año es bisiesto o no.\n 8. Salir")
            condicionales = int(input("digite el condicional que desea usar: "))
            while condicionales == 1:
                eleccion_1 = int(
                    input("escriba '1' si desea usar esta opción o volverla a usar, si no desea salir escriba '2' "))
                if eleccion_1 == 1:
                    # Le decimos al usuario si el numero digitado es positivo o negativo.
                    print("sabremos si el número es positivo o negativo. ")
                    numero = int(input("Digite el número: "))
                    if numero >= 0:
                        print("El número es positivo.")
                    else:
                        print("el número es negativo.")
                elif eleccion_1 == 2:
                    break

            while condicionales == 2:
                eleccion_2 = int(
                    input("escriba '1' si desea usar esta opción o volverla a usar, si no desea salir escriba '2' "))
                if eleccion_2 == 1:
                    # Le decimos al usuario cual de los dos numeros ingresados es mayor y cual menor.
                    print("Sabremos cual número es mayor y cual menor.")
                    num1 = int(input("Digite el primer número: "))
                    num2 = int(input("digite el segundo número: "))
                    if num1 > num2:
                        print(f"El número {num1} es el mayor  y el número {num2} es el menor. ")
                    elif num1 < num2:
                        print(f"el número {num2} es el mayor y el número {num1} es el  menor.")
                    else:
                        print(f"El número {num1} y el número {num2} son iguales.")
                elif eleccion_2 == 2:
                    break

            while condicionales == 3:
                eleccion_3 = int(
                    input("escriba '1' si desea usar esta opción o volverla a usar, si no desea salir escriba '2' "))
                if eleccion_3 == 1:
                    # Le decimos al usuario cual numero es mayor y cual menor de 3 numeros ingresados.
                    print("Vamos a saber cual es el mayor y el menor de 3 numeros (enteros). ")
                    numm1 = int(input("Digite el primer número: "))
                    numm2 = int(input("Digite el segundo número: "))
                    numm3 = int(input("Digite el tercer número:"))
                    if numm2 < numm1 > numm3 and numm1 > numm2 < numm3:
                        print(f"El número mayor es {numm1} y el menor es {numm2}")
                    elif numm1 < numm2 > numm3 and numm2 > numm3 < numm1:
                        print(f"el número mayor es {numm2} y el menor es {numm3} ")
                    elif numm1 < numm3 > numm2 and numm3 > numm1 < numm2:
                        print(f"el número mayor es {numm3} y el menor es {numm1}")
                    else:
                        print(f"los números {numm1}, {numm2} y {numm3} son iguales")
                elif eleccion_3 == 2:
                    break

            while condicionales == 4:
                eleccion_4 = int(
                    input("escriba '1' si desea usar esta opción o volverla a usar, si no desea salir escriba '2' "))
                if eleccion_4 == 1:
                    # Le decimos al usuario que dijite dos numeros y le informamos que se hara dependiendo si uno es mayor o no que otro.
                    print("vamos a introducir dos números A y B, sumarlos si A es menor que B o sino restarlos.")

                    a = int(input("Digite el primer número: "))
                    b = int(input("Digite el segundo número: "))
                    if a < b:
                        c = a + b
                        print(f"la suma de {a} + {b} es igual a {c}")

                    else:
                        d = a - b
                        print(f"la resta de {a} - {b} es igual a {d}")
                elif eleccion_4 == 2:
                    break

            while condicionales == 5:
                eleccion_5 = int(
                    input("escriba '1' si desea usar esta opción o volverla a usar, si no desea salir escriba '2' "))
                if eleccion_5 == 1:
                    # Encontramos el cociente de dos numeros digitados por el usuario.
                    print("encontrar el conciente entre dos numeros.")
                    numb1 = float(input("Digite el primer número: "))
                    numb2 = float(input("Digite el segundo número: "))

                    if numb2 == 0:
                        print("La división no es posible.")
                    else:
                        cociente = numb1 / numb2
                        print(f"El cociente de {numb1} y {numb2} es {round(cociente, 2)}")
                elif eleccion_5 == 2:
                    break

            while condicionales == 6:
                eleccion_6 = int(
                    input("escriba '1' si desea usar esta opción o volverla a usar, si no desea salir escriba '2' "))
                if eleccion_6 == 1:
                    # Le pedimos al usuario digitar dos numeros y dependiendo de si es negativo o no se suma o se multiplica.
                    print("Sumaremos dos numeros si uno de ellos es negativo, de lo contrario los multiplicaremos")
                    A = int(input("Digite el primer número: "))
                    B = int(input("Digite el segundo número: "))

                    if A < 0 or B < 0:
                        C = A + B
                        print(f"El resultado de {A} + {B} es igual a {C}")
                    else:
                        D = A * B
                        print(f"El resultado de la multiplicación es {A} * {B} es igual a {D}")
                elif eleccion_6 == 2:
                    break

            while condicionales == 7:
                eleccion_7 = int(
                    input("escriba '1' si desea usar esta opción o volverla a usar, si no desea salir escriba '2' "))
                if eleccion_7 == 1:
                    # Sabremos si un año es bisiesto o no dependiendo del numero de dias que coloque el usuario.
                    print("Sabremos si un año es bisiesto o no dependiendo de los dias que tenga.")
                    bisiesto = int(input("Digite los dias que tiene el año en total: "))
                    if bisiesto <= 365:
                        print("El año no es bisiesto")
                    else:
                        print("El año es bisiesto")
                elif eleccion_7 == 2:
                    break

            if condicionales == 8:
                break

    elif menu == 3:
        while True:
            # El tercer menu permite ejecutar los ciclos que encontramos en el print (CICLOS)
            print(
                "CICLOS: \nOpciones. \n 1. Saber los multiplos de 3 que hay entre 1 y 100. \n 2. Saber los números impares que hay entre 0 y 100. \n 3. Saber los numeros pares que hay entre 1 y 100."
                "\n 4. Saber los cuadrados de los números del 1 al 30. \n 5. Sumar los cuadrados de los primeros 100 numeros naturales. \n 6. Sumar todos los números que se digitan por teclado mientras no sea cero."
                "\n 7. Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos los números comprendidos entre ellos en secuencia ascendente. \n 8. Salir.")
            ciclos = int(input("Digite la opción que desea usar: "))

            while ciclos == 1:
                eleccion__1 = int(
                    input("escriba '1' si desea usar esta opción o volverla a usar, si no desea salir escriba '2': "))
                if eleccion__1 == 1:
                    # Le mostramos al usuario cuales son los multiplos de 3 entre 1 y 100.
                    print("Sabremos cuales son los multiplos de 3 entre 1 y 100. \n Estos son:")
                    multiplos = [x for x in range(0, 101, 3)]
                    print(multiplos)
                elif eleccion__1 == 2:
                    break
            while ciclos == 2:

                eleccion__2 = int(
                    input("escriba '1' si desea usar esta opción o volverla a usar, si no desea salir escriba '2': "))
                if eleccion__2 == 1:
                    # Le mostramos al usuario cuales son los numeros pares que hay en los primeros 100 numeros naturales.
                    print("Sabremos cuales son los impares que hay entre 0 y 100")
                    impares = [y for y in range(1, 100, 2)]
                    print(impares)

                elif eleccion__2 == 2:
                    break

            while ciclos == 3:
                eleccion__3 = int(
                    input("escriba '1' si desea usar esta opción o volverla a usar, si no desea salir escriba '2': "))
                if eleccion__3 == 1:
                    # le mostramos al usuario los numeros pares que hay entre 1 y 100.
                    print("Sabremos los numeros pares que hay entre 0 y 100")
                    pares = [w for w in range(2, 101, 2)]
                    print(pares)

                elif eleccion__3 == 2:
                    break
            while ciclos == 4:
                eleccion__4 = int(
                    input("escriba '1' si desea usar esta opción o volverla a usar, si no desea salir escriba '2': "))
                if eleccion__4 == 1:
                    # le mostramos al usuario los cuadrados que hay entre 1 y 30.
                    print("Sabremos los cuadrados de los números del 1 al 30")
                    cuadrado = [q ** 2 for q in range(1, 31)]

                    print(cuadrado)
                elif eleccion__4 == 2:
                    break
            while ciclos == 5:
                eleccion__5 = int(
                    input("escriba '1' si desea usar esta opción o volverla a usar, si no desea salir escriba '2': "))
                if eleccion__5 == 1:
                    # sumamos los cudrados de los primeros 100 numeros.
                    print("sumaremos los cuadrados de los primeros 100 numeros")
                    summ = 0
                    for m in range(101):
                        cua = (m + 1) * (m + 1)
                        summ = summ + cua

                    print(f"la suma es: {summ}")


                elif eleccion__5 == 2:
                    break
            while ciclos == 6:
                eleccion__6 = int(
                    input("escriba '1' si desea usar esta opción o volverla a usar, si no desea salir escriba '2': "))
                if eleccion__6 == 1:
                    # Sumamos los digitos del numero que ingrese el usuario.
                    print("Vamos a sumar los digitos del numero que ingrese. ")


                    def sumadigitos(nuum):
                        s = 0
                        while nuum > 0:
                            s = s + nuum % 10
                            nuum = nuum // 10
                        return s


                    sumaT = 0
                    while True:
                        nuum = int(input("numeros diferentes a cero: "))
                        if nuum > 0:
                            sumaT = sumaT + sumadigitos(nuum)
                            print(sumaT)
                            break
                        else:
                            print("Por favor ingrese un número diferente a cero")

                elif eleccion__6 == 2:
                    break
            while ciclos == 7:
                eleccion__7 = int(
                    input("escriba '1' si desea usar esta opción o volverla a usar, si no desea salir escriba '2': "))
                if eleccion__7 == 1:
                    # Le decimos al usuario que coloque dos numeros y se los mostramos ne orden ascendente.
                    print("Mostraremos los numeros en orden ascende entre dos numeros que escoja el usuario")
                    while True:
                        print("Por favor digitar el primer número menor que el segundo. ")
                        r1 = int(input("Digite el primer número: "))
                        r2 = int(input("Digite el segundo número: "))
                        if r1 < r2:
                            b = 0
                            orden = [b for b in range(r1, r2 + 1)]
                            print(orden)
                            break
                        elif r1 > r2:
                            print("Pro favor introduzca el primer número menor que el segundo")

                elif eleccion__7 == 2:
                    break

            if ciclos == 8:
                break


    elif menu == 99:
        break

    # Se uso el ciclo while parapoder entrar al menu, submenu y a cada operación permitiendole al usuario
    # poder volver a elegir la misma o salir y elegir otra, con los condicionales if se pudo colocar el break
    # para terminar los ciclos whiley tambien para algunos ejercicios.






