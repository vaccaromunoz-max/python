#pedir datos 
num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))
operacion = input("ingrese la operacion(+, -, *, /): ")
#2) resolver segun la operacion
resultado = None
if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 == 0: print("error, no se puede dividir por 0")
    else:resultado = num1 / num2 
else: 
    print("error, operacion no valida")
if resultado is not None:
    print(f"resultado: {resultado}")