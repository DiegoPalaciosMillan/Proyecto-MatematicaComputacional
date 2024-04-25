import numpy as np
import cv2

def FiltroMedia(img,valor):
    aux = np.zeros_like(img)  # Crear una matriz auxiliar del mismo tamaño que la imagen de entrada
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            # Sumar los valores de los píxeles en la vecindad del píxel actual
            suma_vecindad = np.sum(img[i-1:i+2, j-1:j+2])
            # Calcular el valor promedio y asignarlo al píxel correspondiente en la matriz auxiliar
            aux[i, j] = suma_vecindad * valor  # Usamos // para asegurar que el resultado sea un entero
    return np.sort(aux)
def filtro_mediana(imagen, tamano_mascara):
    imagen_filtrada = cv2.medianBlur(imagen, tamano_mascara)
    return imagen_filtrada
def blanco_y_negro(imagen):
    # Convertir la imagen a escala de grises
    imagen_bn = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    return imagen_bn

ruta_imagen = input("Por favor, ingresa la ruta de la imagen: ")
imagen = cv2.imread(ruta_imagen)
leer=input("Media, mediana o blanco y negro(bn): ")
if(leer=='media'):
    valor= int(input("Ingrese valor de mascara: "))
    imagen = cv2.resize(imagen, (800, 700))
    imagen_filtrada = FiltroMedia(imagen,valor)
if(leer=='mediana'):
    valor= int(input("Ingrese tamano de mascara: "))
    imagen = cv2.resize(imagen, (800, 700))
    imagen_filtrada = filtro_mediana(imagen,valor)
if(leer=='bn'):
    imagen = cv2.resize(imagen, (800, 700))
    imagen_filtrada = blanco_y_negro(imagen)  
if imagen is not None:
    print("Imagen ingresada correctamente...")
    # Mostrar imagen original y filtrada
    cv2.imshow('Imagen Original', imagen)
    cv2.imshow('Imagen Filtrada', imagen_filtrada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No se pudo cargar la imagen. Por favor, verifica la ruta proporcionada.")