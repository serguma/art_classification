from flask import Flask, request, render_template, jsonify
import os
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

from src import funciones as fc

app = Flask(__name__)


@app.route('/')
def entry_page():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':

        f = request.files['file']
        nombre_arc = request.files['file'].filename
        datos_cuadro = fc.buscar_datos_por_nombre(nombre_arc)
        print(datos_cuadro)
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        result = fc.modelo_predict(file_path)

        return jsonify(result, datos_cuadro)
    return None    


if __name__ == '__main__':
    app.run(debug=True)