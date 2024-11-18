import cv2
import numpy as np

# Defina os parâmetros da imagem
altura, largura = 400, 400
frame = np.zeros((altura, largura, 3), dtype=np.uint8)  # Imagem preta

# Defina os parâmetros da elipse
centro_x, centro_y = int(largura / 2), int(altura / 2)
a, b = 140, 180  # Eixos maior e menor
cor = (144, 238, 144)  # Verde claro (em BGR)

# Desenhe a elipse com a cor verde claro
cv2.ellipse(frame, (centro_x, centro_y), (a, b), 0, 0, 360, cor, 10)

# Exiba a imagem com a elipse
cv2.imshow("Elipse Verde Claro", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()