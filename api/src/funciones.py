from skimage import feature, exposure, io
import pickle as pc
import cv2 as cv
import mahotas
from PIL import Image
import numpy as np
import pandas as pd

#datos del cuadro
def leer_datos(archivo):
    df = pd.read_csv(archivo)
    return df

def buscar_datos_por_nombre(nombre):
    df = leer_datos('data/datos-validar.csv')

    df_validar = df[['artistName', 'image', 'title', 'year', 'estilo']].copy()
    df_validar['image'] = df_validar['image'].apply(lambda x: x.split('/')[-1])

    nombre = nombre.split('-')
    nombre = '-'.join(nombre[1:])
    datos = df_validar[(df_validar['image'] == nombre)]

    return datos.iloc[0].to_json()

#Obtener archivos
def obtener_archivo(path_archivo):
    archivo = ''
    with (open(path_archivo, 'rb')) as pc_file:
        try:
            archivo = pc.load(pc_file)
        except EOFError as e:
            print(e)
            
    return archivo

#Funciones para obtener features
def hu_moments(imagen):
    imagen = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
    feature = cv.HuMoments(cv.moments(imagen)).flatten()
    return feature

def textura(imagen):
    gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
    haralick = mahotas.features.haralick(gris).mean(axis=0)
    return haralick

def histograma_color(imagen, mask = None):
    imagen = cv.cvtColor(imagen, cv.COLOR_BGR2HSV)
    hist  = cv.calcHist([imagen], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    cv.normalize(hist, hist)
    return hist.flatten()


#Predicción utilizando RF
def modelo_predict(img_path):
    tamano = (256, 256)
    estilos = ['abstract-art', 'realism' ]

    modelo = obtener_archivo('training/rdf.ckpt')
    image = cv.imread(img_path)
    image = cv.resize(image, tamano)

    hu = hu_moments(image)
    haralick_im   = textura(image)
    histograma_im  = histograma_color(image)

    features_imagen = np.hstack([histograma_im, haralick_im, hu])

    prediction = modelo.predict(features_imagen.reshape(1,-1))[0]
    print(modelo.predict_proba(features_imagen.reshape(1,-1)))
    return estilos[prediction]