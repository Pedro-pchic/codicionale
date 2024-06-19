# TRY es una estructura y flujo de controlar de error 
# EXCEPT se ejecuta no importando el error


try: 
    numero=int(input("ingrese un numero "))
    print(f"el numero {numero}")
except ValueError:
    print(" debes ingresar un numero ")
    
    