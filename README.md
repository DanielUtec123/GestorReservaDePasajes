# Sistema de Reserva de Pasajes

## Requerimientos

* Un usuario podré seleccionar un pasaje  
* Como usuario podré comprar un pasaje.
* Como administrador podré visualizar todos los pasajes comprados por los usuarios.
* Como usuario podré buscar un pasaje por dni.
* Como administrador podré agregar destinos y costos para que los usuarios puedan comprar. 

## Constraints

* No se puede utilizar una base de datos.
* Usar archivos para el manejo de datos.

# Solución Planteada

## Tecnología

* Python 3:  Lenguaje base.
* Flask: Para el backend.
* Jinja2: Para el renderizado de templates.

## Tablas 

### Pasajes 
Lista de todos los pasajes disponibles para comprar 

Columnas:

* Id
* Destino
* Costo

### PasajesComprados

Lista de los pasajes comprados por usuarios.

Columnas:

* DNI_cliente 
* Fecha 
* Id_pasaje 
* Nombre
* Apellido
* Correo

## Run 

### Instalar Flask 

```
pip install flask
```

### Correr el servidor

```
python server.py 
```

Ir a localhost:9090 en cualquier navegador

