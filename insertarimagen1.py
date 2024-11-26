#import matplotlib as plt
#import matplotlib.image as mpimg # esto lee la imagen

#primero vamos a cargar la imagen
#ruta_imagen=r"C:\Users\Usuario\Desktop\REPOSITORIOS DE OTRA CUENTA DE GITHUB\CURSO-PYTHON-B-SICO\prueba1.png"
#imagen=mpimg.imread(ruta_imagen) # Aqui va  la ruta de archivo

#ahora vamos a mostrar la imagen
#plt.imshow(imagen)
#plt.axis('off' ) # esto oculta los ejes, esto quiere decir que no muestra los bordes, informacion irrelevante cuando queremos mostrar graficos
#plt.show()

import cv2
 #vamos a cargar la imagen
imagen= cv2.imread(r"C:\Users\Usuario\Desktop\REPOSITORIOS DE OTRA CUENTA DE GITHUB\CURSO-PYTHON-B-SICO\prueba1.png")
 # vamos a mostrar una imagen en una ventana
cv2.imshow("Imagen de digrama de UML",imagen)
cv2.waitKey(0)
cv2.destroyAllWindows() 