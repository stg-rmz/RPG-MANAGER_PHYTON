from flask import Flask, render_template, request, redirect
from models.personaje import Personaje
from models.repositorio import lista_personajes

app = Flask(__name__)
repo = lista_personajes

@app.route('/personajes', methods=['GET'])
def listar_personajes():
    return render_template('personajes.html', personajes=lista_personajes)

@app.route('/personajes', methods=['POST'])
def crear_personaje():
    nombre = request.form['nombre']
    clase = request.form['clase_personaje']
    nivel = int(request.form['nivel'])
    vida = int(request.form['vida'])

    nuevo_p = Personaje(nombre, clase, nivel, vida)
    lista_personajes.append(nuevo_p)

    return redirect('/personajes')

if __name__ == '__main__':
    app.run(debug=True)