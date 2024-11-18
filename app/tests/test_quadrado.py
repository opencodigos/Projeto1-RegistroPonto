import cv2
import numpy as np

# Defina os parâmetros da imagem
altura, largura = 480, 360
frame = np.zeros((altura, largura, 3), dtype=np.uint8)  # Imagem preta

# Defina os parâmetros do quadrado
lado = 200  # Tamanho do lado do quadrado
centro_x, centro_y = int(largura / 2), int(altura / 3)
top_left = (centro_x - lado // 2, centro_y - lado // 2)
bottom_right = (centro_x + lado // 2, centro_y + lado // 1)
cor = (144, 238, 144)  # Verde claro (em BGR)

# Desenhe o quadrado
cv2.rectangle(frame, top_left, bottom_right, cor, 5)

# Exiba a imagem com o quadrado
cv2.imshow("Quadrado Verde Claro", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
