""" def cargar_orden():
    orden=[]
    for x in range(5):
        nom=input("Ingresar el nombre del pais:")
        cant=int(input("Ingrese la cantidad de habitantes:"))
        paises.append((nom,cant))
    return paises """

from itertools import count
import operator


estados = {1:"Reponer Copia", 2:"Quitar Pelicula",3:"Dejar como esta"}
genero = {1:"Accion",2:"Terror",3:"Comedia"}
peliculas= {}

codigoPelicula = 0

def cargar_Pelicula():
    global codigoPelicula
    codigoPelicula += 1
    print("\x1b[0;37m"+"Agregando pelicula con codigo:", codigoPelicula)
    genero=int(input("Ingresar genero (Colocar 'verGeneros()' para ver los tipos que hay):"))
    descripcion=input("Ingresar descripción de pelicula:")
    cantCopias=int(input("Ingrese la cantidad de copias:"))
    cantCopiasAlqu=int(input("Ingrese la cantidad de copias alquiladas:"))
    estado=int(input("Ingrese el estado en el que se encuentra:"))
    peliculas[codigoPelicula] = {"Genero":genero,"Descripcion":descripcion,"Cantidad":cantCopias,"Alquiladas":cantCopiasAlqu,"Estado":estado}
    print("================ La pelicula fue agregada con éxito ================")
    si=int(input("\x1b[1;33m"+"Colocar '1' para cargar otra pelicula o otro caracter para cancelar: "))
    if si == 1:
       cargar_Pelicula()

cargar_Pelicula()

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
    print("Peliculas a eliminar:")
    for clave2 in peliculas:
        valor = peliculas[clave2]
        if int(valor["Cantidad"]) <= int(valor["Alquiladas"]):
            print(peliculas[clave2]["Descripcion"])
    print("================================")

def peliculaCodigo():
    codigo=int(input("Ingrese el codigo para buscar una pelicula:"))
    if codigo in peliculas:
     print(peliculas[codigo])
    else:
     print('Esta clave no existe')

def peliculasGeneroMayor():
    print("================================")
    for clave1 in genero:
        valor = genero[clave1]
        generosCount = [] 
        for clave in peliculas:
            generosCount.append(peliculas[clave]["Genero"])
    print ("GENERO:" + genero[max(generosCount)])

def listarPelis():
    print(list(e for e in peliculas if e['Genero']  == 2)[0])

listarPelis()
peliculasGeneroMayor()
peliculasEliminar()
peliculasXdesc()
peliculasGenero()
copiasAlquiladas()
peliculaCodigo()

input("\x1b[0;37m"+"Precionar enter para cerrar programa")