import socket
#definiendo cliente
#cliente
import numpy
import sys
import json
import base64
import cv2
#from scipy.sparse import csr_matrix 
#from scipy.fftpack import dct
#from scipy.fftpack import idct#funcion inversa
from time import time
import math
from PIL import Image
import time

#**********
def send_image(path_image):
    with open(path_image, "rb") as image:
        imagen = base64.b64encode(image.read())

#Coding as "b" string

#blistastr=imagen.encode()
    socket_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2.tcp.ngrok.io:12096
    socket_client.connect(("127.0.0.1",9999))
#socket_client.connect(("localhost",9999))
#Mensaje

    while True:
        mensaje=imagen
        socket_client.send(mensaje)
      
      #if mensaje==b"quit":
        break

#cierre
    print(f"send{path_image}")
    socket_client.close()

def main():
    paths_images = ["img/kalev.jpg","img/fernando.png","img/imagen_input.jpg","img/paul.jpg","img/rosario.jpg"]
    for path in paths_images:
        send_image(path)
        time.sleep(15)


if __name__ == '__main__':
    main()
