""" def cargar_orden():
    orden=[]
    for x in range(5):
        nom=input("Ingresar el nombre del pais:")
        cant=int(input("Ingrese la cantidad de habitantes:"))
        paises.append((nom,cant))
    return paises """

from itertools import count
import operator

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

estados = {1:"Reponer Copia", 2:"Quitar Pelicula",3:"Dejar como esta"}
genero = {1:"Accion",2:"Terror",3:"Comedia"}
peliculas= {}

cantidad=int(input("¿Cuantas peliculas quiere cargar?: "))

def cargar_Pelicula():
    codigoPelicula=int(input("Ingresar codigo de pelicula:"))
    genero=int(input("Ingresar genero (Colocar 'verGeneros()' para ver los tipos que hay):"))
    descripcion=input("Ingresar descripción de pelicula:")
    cantCopias=int(input("Ingrese la cantidad de copias:"))
    cantCopiasAlqu=int(input("Ingrese la cantidad de copias alquiladas:"))
    estado=int(input("Ingrese el estado en el que se encuentra:"))
    peliculas[codigoPelicula] = {"Genero":genero,"Descripcion":descripcion,"Cantidad":cantCopias,"Alquiladas":cantCopiasAlqu,"Estado":estado}
    print(bcolors.OK + "================ La pelicula fue agregada con éxito ================" + bcolors.RESET)

""" i = 1
while i <= cantidad:
    cargar_Pelicula()
    i += 1 """

peliculas[12] = {"Genero":1,"Descripcion":"Scream 4","Cantidad":4,"Alquiladas":4,"Estado":2}
peliculas[13] = {"Genero":2,"Descripcion":"Padre de familia","Cantidad":42,"Alquiladas":2,"Estado":1}
peliculas[144] = {"Genero":1,"Descripcion":"Dragon ball Z","Cantidad":7,"Alquiladas":6,"Estado":3}
peliculas[233] = {"Genero":3,"Descripcion":"Black mirror","Cantidad":4,"Alquiladas":6,"Estado":1}

def peliculasGenero():
    print("================================")
    for clave1 in genero:
        valor = genero[clave1]
        generosCount = [] 
        for clave in peliculas:
            generosCount.append(peliculas[clave]["Genero"])
        print("En el genero " + str(valor) + " hay: " + str(generosCount.count(clave1)) + " peliculas")
    
def copiasAlquiladas():
    print("================================")
    total = 0
    for clave in peliculas:
        valor = peliculas[clave]
        total = total + valor["Alquiladas"]
    print("Total de copias alquiladas: ", total)

def peliculasXdesc():
    print("================================")
    array = []
    for key in peliculas:
        array.append(peliculas[key]["Descripcion"])
    ordenados = sorted(array)
    print("Lista de peliculas ordenadas por descripción:")
    print(ordenados)

def peliculasEliminar():
    print("================================")
    print(bcolors.FAIL +"Peliculas a eliminar:" + bcolors.RESET)
    for clave2 in peliculas:
        valor = peliculas[clave2]
        if int(valor["Cantidad"]) <= int(valor["Alquiladas"]):
            print(peliculas[clave2]["Descripcion"])

def peliculaCodigo():
    codigo=int(input(bcolors.WARNING +"Ingrese el codigo para buscar una pelicula:" + bcolors.RESET))
    if codigo in peliculas:
     print(peliculas[codigo])
    else:
     print(bcolors.FAIL +'Esta clave no existe' + bcolors.RESET)

def peliculasGeneroMayor():
    print("================================")
    for clave1 in genero:
        valor = genero[clave1]
        generosCount = [] 
        for clave in peliculas:
            generosCount.append(peliculas[clave]["Genero"])
    print ("GENERO:" + genero[max(generosCount)])

def listarPelis():
    print("Peliculas del genero 1 y 2:")
    for clave2 in peliculas:
        valor = peliculas[clave2]
        if int(valor["Genero"]) == 1 or int(valor["Genero"]) == 2:
            print(peliculas[clave2])
    print("================================")

listarPelis()
peliculasGeneroMayor()
peliculasEliminar()
peliculasXdesc()
peliculasGenero()
copiasAlquiladas()
peliculaCodigo()

input(bcolors.FAIL +"Precionar enter para cerrar programa" + bcolors.RESET)