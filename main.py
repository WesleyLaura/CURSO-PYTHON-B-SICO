nombre=input("\nIngres su nombre:\n")
print(f"Hola,{nombre}")

print("\n\tHola bienvenido a nuestro programa basico de python\n")
while True:
    try:

        edad=int(input("Ingrese su edad(EDAD POSITIVA): "))
    
        if edad>0:
            break
        else:
            print("Edad inválida, inténtelo de nuevo.")
    except ValueError:
        print("Ingrese un número entero, por favor")
    
if edad >=18:
    print("Es un adulto")
elif edad > 12:
    print("Es un adolescente")
else:
    print("Es un niño")       
    
    #ahora haremos uso de bucle for
    for i in range(edad):
        print(i)
    #usaremos el buble while
    print("\n--------------------------------------\n")
while edad < 5:
    print(edad)
    edad+=1
    
