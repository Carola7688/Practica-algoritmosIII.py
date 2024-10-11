#Verificar si la edad del cliente le permite ingresar a la discoteca

#Paso 1: Solicitar al usuario que ingrese la edad de su cliente

Edad = float(input("Por favor, ingrese la edad del cliente: "))

#Paso 2: Verificar si la edad del cliente cumple con la edad para poder entrar
Permitido = True if Edad >= 18 else False


#Paso 3: Mostrar al usuario si su cliente puede ingresar o no
if Permitido:
    print("El cliente puede ingresar a la discoteca")
else:
    print("Lo sentimos, el cliente no puede ingresar a la discoteca")