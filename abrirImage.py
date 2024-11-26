from PIL import Image
#carga la imagen
imagen=Image.open("C:\\Users\\Usuario\\Desktop\\REPOSITORIOS DE OTRA CUENTA DE GITHUB\\CURSO-PYTHON-B-SICO\\prueba.png")
#esta funcion show() muestra la imagen
#imagen.show()
#ahora vamos a redimensionar la imagen
imagen_redimensionada=imagen.resize((200,200))
imagen_redimensionada.save("C:\\Users\\Usuario\\Desktop\\REPOSITORIOS DE OTRA CUENTA DE GITHUB\\CURSO-PYTHON-B-SICO\\prueba.png")
imagen.show()