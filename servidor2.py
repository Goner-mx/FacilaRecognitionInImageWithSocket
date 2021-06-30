import socket #un socket = (dir Ip, dir TCP)
import json
import numpy
import base64
import cv2 #para abrir imagen
from PIL import Image 
import rekognition_facial
#creando el socket con sus protocolos
socket_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#definiendo puertos
socket_server.bind( ("0.0.0.0", 9999) ) 

#Cuantos host sevan a comunicar con el servidor
#Esta funcion tambien pone al servidor en modo escuchar: espera una peticion
socket_server.listen(1)

#Acceptando la peticion. Existe la creacion de un cliente
socket_client , ( remote_client_ip , remote_client_tcp ) = socket_server.accept()
print("ip client: ",remote_client_ip)
print("tcp client: ",remote_client_tcp)

#Recibir un mensaje 
while True:
        mensaje=socket_client.recv(1024)
        for i in range (50):
            mensaje2 = socket_client . recv (409600000)
            mensaje = mensaje + mensaje2
       
        with open("generatedImage32.png", 'wb+') as image:
               image.write(base64.b64decode(mensaje))
        
      
        ### MOSTRAR IMAGEN DENTRO DE LA IMA
        #BWimage=cv2.imread('generatedImage32.png',cv2.IMREAD_GRAYSCALE)
        #print("mensaje recibido")
        #cv2.imshow('imgBW',BWimage)#muestra imagen
        #cv2.waitKey(0)#espera a que se presione enter
        #cv2.destroyAllWindows()#libera recursos

        ### FACIAL REKOGNITION####

        try:
            rekognition_facial.compare_face("generatedImage32.png")
        except Exception as ex:
            print(f"Error Rekognition: {ex}")
        
        break 
print("Correcto...")
socket_client.close()
socket_server.close()




