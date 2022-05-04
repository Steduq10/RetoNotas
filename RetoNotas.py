print("¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.")


nombre = input("Ingrese su nombre: ")
materia = input("Ingrese su materia: ")
nota = float(input("Ingrese la nota obtenida: "))
porcentaje = int(input("Ingrese el porcentaje de la nota ingresada: "))
notaAcumulada = nota * (porcentaje/100)
notas = [notaAcumulada]
lista = [porcentaje]

if porcentaje <100:
    añadir = input("¿Faltan notas por añadir? S/N: ")
    while añadir == "S" or añadir == "s":
        nota = float(input("Ingrese la nota obtenida: "))
        porcentaje = int(input("Ingrese el porcentaje de la nota ingresada: "))
        notaAcumulada = nota * (porcentaje/100)
        notas.append(notaAcumulada)
        lista.append(porcentaje)
        porcentaje = 0
        for i in lista:
            porcentaje += i
        if porcentaje <100:
            añadir = input("¿Faltan notas por añadir? S/N: ")
        elif porcentaje > 100:
            print("El porcentaje evaluado de una materia no puede ser mayor a 100")
            lista.pop()
            notas.pop()
            añadir = "S"
        else:
            añadir = "N"

elif porcentaje >100:
    print("El porcentaje evaluado de una materia no puede ser mayor a 100")
    lista.pop()
    notas.pop()
    nota = float(input("Ingrese la nota obtenida: "))
    porcentaje = int(input("Ingrese el porcentaje de la nota ingresada: "))
    notaAcumulada = nota * (porcentaje / 100)
    notas = [notaAcumulada]
    lista = [porcentaje]
    if porcentaje < 100:
        añadir = input("¿Faltan notas por añadir? S/N: ")
        while añadir == "S" or añadir == "s":
            nota = float(input("Ingrese la nota obtenida: "))
            porcentaje = int(input("Ingrese el porcentaje de la nota ingresada: "))
            notaAcumulada = nota * (porcentaje / 100)
            notas.append(notaAcumulada)
            lista.append(porcentaje)
            porcentaje = 0
            for i in lista:
                porcentaje += i
            if porcentaje < 100:
                añadir = input("¿Faltan notas por añadir? S/N: ")
            elif porcentaje > 100:
                print("El porcentaje evaluado de una materia no puede ser mayor a 100")
                lista.pop()
                notas.pop()
                añadir = "S"
            else:
                añadir = "N"

notaAcumulada = 0
for i in notas:
    notaAcumulada += i

aprobacion = " "
if notaAcumulada < 3:
    aprobacion = "Reprobado"
else:
    aprobacion = "Aprobado"


print(f"El estudiante {nombre} cursó la materia {materia} y obtuvo {notaAcumulada} resultando en {aprobacion}" )
