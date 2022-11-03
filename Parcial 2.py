import time
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

estados = {1:"Reponer Copia", 2:"Quitar Pelicula",3:"Dejar como esta"}
genero = {1:"Accion",2:"Terror",3:"Comedia"}
peliculas= {}

def inicializador():
    try:
        cantidad=int(input("¿Cuantas peliculas quiere cargar?: "))
        if cantidad <= 0:
            print(bcolors.FAIL +"Coloque un numero mayor a 0" + bcolors.RESET)   
            return inicializador()
        repetir(cantidad)
    except:
        print(bcolors.FAIL +"Ocurrio un error vuelve a intentarlo" + bcolors.RESET)   
        return inicializador()

def cargar_Pelicula():
    codigoPelicula=int(input("Ingresar codigo de pelicula:"))
    genero=int(input("Ingresar genero (1 = 'Accion', 2 = 'Terror', 3 = 'Comedia'):"))
    descripcion=input("Ingresar descripción de pelicula:")
    cantCopias=int(input("Ingrese la cantidad de copias:"))
    cantCopiasAlqu=int(input("Ingrese la cantidad de copias alquiladas:"))
    estado=int(input("Ingrese el estado en el que se encuentra (1 = 'Reponer Copia', 2 = 'Quitar Pelicula', 3 = 'Dejar como esta'):"))
    peliculas[codigoPelicula] = {"Genero":genero,"Descripcion":descripcion,"Cantidad":cantCopias,"Alquiladas":cantCopiasAlqu,"Estado":estado}
    print(bcolors.OK + "================ La pelicula fue agregada con éxito ================" + bcolors.RESET)

def repetir(cantidad):
    i = 1
    while i <= cantidad:
        cargar_Pelicula()
        i += 1 

peliculas[233] = {"Genero":1,"Descripcion":"Scream 4","Cantidad":2,"Alquiladas":4,"Estado":2}
peliculas[13] = {"Genero":2,"Descripcion":"Padre de familia","Cantidad":42,"Alquiladas":2,"Estado":1}
peliculas[144] = {"Genero":2,"Descripcion":"Dragon ball Z","Cantidad":7,"Alquiladas":6,"Estado":1}
peliculas[2] = {"Genero":3,"Descripcion":"Black mirror","Cantidad":4,"Alquiladas":6,"Estado":1}

def peliculasGeneroMayor():
    time.sleep(4)
    print(bcolors.OK +"7. Mostrar qué género se alquila más (Búsqueda del mayor)." + bcolors.RESET)
    for clave1 in genero:
        valor = genero[clave1]      
        generosCount = [] 
        for clave in peliculas:
            generosCount.append(peliculas[clave]["Genero"])
    print ("El genero que mas se alquila es: " + genero[max(set(generosCount), key=generosCount.count)])
    print("================================")

def peliculasGenero():
    time.sleep(1)
    print("================================")
    print(bcolors.OK +"2. Indicar cantidad de películas por género." + bcolors.RESET)
    for clave1 in genero:
        valor = genero[clave1]
        generosCount = [] 
        texto = ""
        for clave in peliculas:
            generosCount.append(peliculas[clave]["Genero"])
            
        if generosCount.count(clave1) > 1:
            texto = "s"
        print("En el genero " + str(valor) + " hay: " + str(generosCount.count(clave1)) + " pelicula" + texto)
    print("================================")
    
def copiasAlquiladas():
    time.sleep(4)
    print(bcolors.OK +"3. Indicar la cantidad total de copias alquiladas" + bcolors.RESET)
    total = 0
    for clave in peliculas:
        valor = peliculas[clave]
        total = total + valor["Alquiladas"]
    print("Total de copias alquiladas: ", total)
    print("================================")

def peliculasXdesc():
    time.sleep(4)
    print(bcolors.OK +"4. Mostrar un Listado de películas ordenadas por descripción. " + bcolors.RESET)
    array = []
    for key in peliculas:
        array.append(peliculas[key]["Descripcion"])
    ordenados = sorted(array)
    print("Lista de peliculas ordenadas por descripción:")
    print(ordenados)
    print("================================")

def peliculasEliminar():
    time.sleep(4)
    print(bcolors.OK +"5. Listar todas las películas que hay que quitar del catálogo de películas. " + bcolors.RESET)
    print(bcolors.FAIL +"Peliculas a eliminar:" + bcolors.RESET)
    for clave2 in peliculas:
        valor = peliculas[clave2]
        if int(valor["Cantidad"]) <= int(valor["Alquiladas"]):
            print(peliculas[clave2]["Descripcion"])
    print("================================")

def peliculaCodigo():
    time.sleep(4)
    print(bcolors.OK +"6. Ingresar un Código de película y mostrar todos sus datos. " + bcolors.RESET)
    try:
        codigo=int(input(bcolors.WARNING +"Ingrese el codigo para buscar una pelicula:" + bcolors.RESET))
        if codigo <= 0:
            print(bcolors.FAIL +"Coloque un numero mayor a 0" + bcolors.RESET)   
            return peliculaCodigo()
    except:
        print(bcolors.FAIL +"Ocurrio un error vuelve a intentarlo" + bcolors.RESET)   
        return peliculaCodigo()

    if codigo in peliculas:
      print(" | "+str(genero[peliculas[codigo]["Genero"]])+" | "+peliculas[codigo]["Descripcion"]+" | "+str(peliculas[codigo]["Cantidad"])+" | "+ str(peliculas[codigo]["Alquiladas"])+" | "+str(estados[peliculas[codigo]["Estado"]] + " | ")) 
    else:
     print(bcolors.FAIL +'No hay datos que coincidan con el codigo colocado' + bcolors.RESET)
    print("================================")


def listarPelis():
    time.sleep(4)
    print(bcolors.OK +"8. Listar todas las películas de drama y acción" + bcolors.RESET)
    print("Peliculas del genero 1 y 2:")
    for clave2 in peliculas:
        valor = peliculas[clave2]
        if int(valor["Genero"]) == 1 or int(valor["Genero"]) == 2:
            print(" | "+str(genero[valor["Genero"]])+" | "+valor["Descripcion"]+" | "+str(valor["Cantidad"])+" | "+ str(valor["Alquiladas"])+" | "+str(estados[valor["Estado"]] + " | ")) 
    print("================================")

def listarPorCodigo():
    time.sleep(4)
    print(bcolors.OK +"9. Mostrar un Listado ordenados por Código de película. " + bcolors.RESET)
    keys = peliculas.keys()
    sorted_keys = sorted(keys)
    sorted_desserts = {}
    for key in sorted_keys:
        sorted_desserts[key] = peliculas[key]
    print(bcolors.WARNING +'Lista de peliculas ordenadas por código' + bcolors.RESET)
    print(sorted_desserts)
    print("================================")

def buscarPorDes():
    time.sleep(4)
    print(bcolors.OK +"10. Realizar una consulta por descripción (Es decir ingresar el nombre de la película y mostrar sus datos)" + bcolors.RESET)
    descripcion=input(bcolors.WARNING +"Ingrese la descripcion para buscar una pelicula: " + bcolors.RESET)
    error = False
    for key in peliculas:
        valor = peliculas[key]
        if valor["Descripcion"] == descripcion:
            print(bcolors.OK + "Resultado de la busqueda:" + bcolors.RESET)
            print(valor)
            error = False
            break
        else:
            error = True
    if error == True:
        print(bcolors.FAIL +'No se encontraron resultados con este criterio de busqueda (' + descripcion + ")" + bcolors.RESET)
    print("================================")

def listarCopiasInferior():
    time.sleep(4)
    print(bcolors.OK +"11. Mostrar todas las películas con cantidad de copias inferior a 3." + bcolors.RESET)
    encontro = 0
    for key in peliculas:
        valor = peliculas[key]
        if int(valor["Cantidad"]) <= 3:
            print(" | "+str(genero[valor["Genero"]])+" | "+valor["Descripcion"]+" | "+str(valor["Cantidad"])+" | "+ str(valor["Alquiladas"])+" | "+str(estados[valor["Estado"]] + " | ")) 
            encontro = 1
        else:
            if encontro != 1:
              print(bcolors.FAIL + 'No se encontraron peliculas menor a 3 copias' + bcolors.RESET)
              break
    print("================================")

def peliculas_Reponer():
    time.sleep(4)
    print(bcolors.OK +"12. Mostrar todas las películas de terror que se deben reponer" + bcolors.RESET)
    for key in peliculas:
        valor = peliculas[key]
        if int(valor["Genero"]) == 2:
            if int(valor["Estado"]) == 1:
                print(" | "+str(genero[valor["Genero"]])+" | "+valor["Descripcion"]+" | "+str(valor["Cantidad"])+" | "+ str(valor["Alquiladas"])+" | "+str(estados[valor["Estado"]] + " | "))      
            else:
                print(bcolors.FAIL + 'No se encontraron peliculas de terror a reponer' + bcolors.RESET)
                break
    print("================================")

#=====Iniciar funciones=====
inicializador()
peliculasGenero()
copiasAlquiladas()
peliculasXdesc()
peliculasEliminar()
peliculaCodigo()
peliculasGeneroMayor()
listarPelis()
listarPorCodigo()
buscarPorDes()
listarCopiasInferior()
peliculas_Reponer()
#===========================

input(bcolors.FAIL +"Precionar enter para cerrar programa" + bcolors.RESET)