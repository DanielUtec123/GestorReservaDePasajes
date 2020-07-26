
pasajesFile ="pasajes.txt"
pasajesComprados = "pasajesComprados.txt"

#Inicializar las tablas si aún no están creados
def inicializar_entidades():
    try:
        f = open(pasajesFile)
        f.close()
        m = open(pasajesComprados)
        m.close()
    except:
        f = open(pasajesFile,"w")
        f.write("id, destino, costo\n")
        f.close()
        f = open(pasajesComprados,"w")
        f.write("id, dni_cliente, fecha, id_pasaje, nombre, apellido, correo\n")
        f.close()

#guarda un pasaje en la base de datos
def guardar_pasaje(destino, costo):
    #TO DO
    pasajes = all_pasajes()

    # crear un id diferente
    max_id = 0
    for pasaje in pasajes:
        if (int(pasaje[0]) > max_id):
            max_id = int(pasaje[0])


    nuevo_id = max_id + 1

    #guardamos el nuevo pasaje

    f = open(pasajesFile,'a')
    f.write(str(nuevo_id)+", "+destino + ", "+ str(costo)+ "\n")
    f.close()

    return True


#Retorna si un id pertenece al archivo pasajes.tct
def is_in_pasaje(id):

    pasajes = all_pasajes()

    for pasaje in pasajes:
        if(int(pasaje[0]) == id):
            return True
    return False


#retorna todos lo pasajes guardados
def all_pasajes():
    f = open(pasajesFile,"r")

    # setear el cursor en el primer elemento de la tabla
    f.readline()

    registros = []
    while (True):
        linea = f.readline()
        if not linea:
            break

        linea = linea.strip().split(",")

        registro = [i.strip() for i in linea]
        registros.append(registro)

    return registros


def search_pasajes_by_id(id):
    pasajes = all_pasajes()

    for pasaje in pasajes:
        if pasaje[0] == id:
            return pasaje

    return None



#Guarda el pasaje en comprado en el archivo
def guardar_pasaje_comprado(dni_cliente, fecha, id_pasaje, nombre, apellido, email):
    pasajes = all_pasaje_comprado()

    # crear un id diferente
    max_id = 0
    for pasaje in pasajes:
        if (int(pasaje[0]) > max_id):
            max_id = int(pasaje[0])

    nuevo_id = max_id + 1
    # guardamos el nuevo pasaje

    f = open(pasajesComprados, 'a')
    f.write(str(nuevo_id) + ", " + dni_cliente + ", " + fecha +", "+ id_pasaje+ ", "+ nombre
            +", "+apellido +", " +email + "\n")
    f.close()
    return True


#retorna una lista con todos los pasajes comprados
def all_pasaje_comprado():
    f = open(pasajesComprados, "r")

    # setear el cursor en el primer elemento de la tabla
    f.readline()

    registros = []
    while (True):
        linea = f.readline()
        if not linea:
            break

        #Parseo de la linea
        linea = linea.strip().split(",")

        registro = [i.strip() for i in linea]
        registros.append(registro)

    # filtrar con los datos de pasajes.txt

    for registro in registros:
        pasaje = search_pasajes_by_id(registro[3])
        registro.append(pasaje[1])
        registro.append(pasaje[2])
    return registros



#Retorna la lista de pasajes que coinciden con el dni
def search_pasajes_by_dni(dni):

    pasajes =  all_pasaje_comprado()

    resultado =[]

    for pasaje in pasajes:
        if pasaje[1] == dni:
            resultado.append(pasaje)

    for registro in resultado:
        pasaje = search_pasajes_by_id(registro[3])
        registro.append(pasaje[1])
        registro.append(pasaje[2])

    return resultado


inicializar_entidades()
