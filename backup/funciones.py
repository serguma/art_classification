import cv2 as cv
import os
import pickle as pc

path_data = 'data/'
path_train = 'imagenes_color/train/'
path_test = 'imagenes_color/test/'
path_validar = 'imagenes_color/validar/'
path_features = 'features/'
path_training = 'training/'

estilos = ['abstract-art', 'realism']
tipos = ['train', 'test', 'validar']

pags_train = list(range(1, 11))
pags_test = list(range(11, 14))
pags_validar = list(range(20, 23))

tamano = (256, 256)

def obtener_archivo(path_archivo):
    archivo = ''
    with (open(path_archivo, 'rb')) as pc_file:
        try:
            archivo = pc.load(pc_file)
        except EOFError as e:
            print(e)
            
    return archivo

def guardar_archivo(contenido, path_archivo):
    archivo = ''
    with (open(path_archivo, 'wb')) as pc_file:
        try:
            pc.dump(contenido, pc_file)
        except EOFError as e:
            print(e)
            
    return True    