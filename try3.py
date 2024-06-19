try:
    numero1 =int(input("ingrese un numero "))
    numero2 =int(input("ingrese otro numero "))
    try:
        resultado = numero1 / numero2
        print(resultado)
    except ZeroDivisionError:
        print(" no se puede divir")
except ValueError:
    print("ingrese un numero ")
