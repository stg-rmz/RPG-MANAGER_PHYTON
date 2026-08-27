from flask import Flask, jsonify
from models.repositorio import lista_personajes

app = Flask(__name__)

@app.route('/personajes', methods=['GET'])
def obtener_personajes():
    
    datos = [
        {
            "nombre": p.nombre,
            "clase": p.clase_personaje,
            "nivel": p.nivel,
            "vida": p.vida
        } 
        for p in lista_personajes
    ]
    return jsonify(datos)

if __name__ == '__main__':
    app.run(debug=True, port=5000)