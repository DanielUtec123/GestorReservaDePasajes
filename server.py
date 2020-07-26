from flask import Flask, render_template, request, session, Response, redirect, url_for
import json

from logic import *


app = Flask(__name__)
app.secret_key = 'Security Key'  # SECURITY KEY

cache = {}


# PAGINAA DE INICIO
# Formulario de compra de pasajes
@app.route('/')
def index():

    ofertas = all_pasajes()

    return render_template('index.html', ofertas = ofertas)




#Lista de pasajes comprados
@app.route('/pasajes')
def pasajes():
    registros = all_pasaje_comprado()

    for registro in registros:
        registro[8] = registro[8]+" PEN"

    header = ["ID", "DNI_CLIENTE", "FECHA", "ID_PRECIO", "NOMBRE", "APELLIDO", "CORREO", "DESTINO", "PRECIO"]
    print(pasajes)

    return render_template('table.html', registros = registros , header=header )


@app.route('/precios')
def precios():
    registros = all_pasajes()
    header = ["ID", "DESTINO", "COSTO"]

    for registro in registros:
        registro[2] = registro[2]+" PEN"

    return render_template('table.html', registros=registros, header=header)


@app.route('/precio')
def crear_precio():

    return render_template('precioFormulario.html')


@app.route('/do_reserva', methods=["POST"])
def do_reservation():

    name = request.form['nombre']
    apellido = request.form['apellido']
    destino = request.form['destino']
    fecha = request.form['date']
    correo = request.form['correo']
    dni = request.form['dni']

    print(name,apellido, destino, fecha, correo)
    guardar_pasaje_comprado(dni,fecha,destino,name,apellido,correo)

    return redirect(url_for('index'))


@app.route('/do_oferta', methods=["POST"])
def do_oferta():

    destino = request.form['destino']
    precio  = request.form['precio']

    guardar_pasaje(destino,precio)

    return render_template('precioFormulario.html')



#Se retornará el pasaje según el DNI del cliente
@app.route('/do_search')
def pasajes_by_dni():

    dni = request.args.get('dni')

    header = ["ID", "DNI_CLIENTE", "FECHA", "ID_OFERTA", "NOMBRE", "APELLIDO", "CORREO", "DESTINO", "PRECIO"]
    print(dni)
    registros = search_pasajes_by_dni(str(dni))

    return render_template('table.html', registros = registros , header=header)






if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=9090, threaded=True, debug=True, host=('localhost'))