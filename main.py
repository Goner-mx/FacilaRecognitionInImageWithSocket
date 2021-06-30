""" importando modulos """
import facial_recognition
import receive_image
import time

def get_image_socket():
    """
    Ejecuta la conexion con el socket para descargar la image,
    """
    try:
        receive_image.get_image()
    except Exception as ex:
        print(f"Exception in get_image_socket():\n{ex}")

def get_facial_recognition():
    try:
        facial_recognition.compare_face("generatedImage32.png")
    except Exception as ex:
        print(f"Exception in get_facial_recognition():\n{ex}")

"""[2]Funcion que ejecuta las demas funciones"""
def main():
    get_image_socket()
    get_facial_recognition()
    time.sleep(10)
    main()

"""[1]Funcion de Entrada"""
if __name__ == '__main__':
    main()
