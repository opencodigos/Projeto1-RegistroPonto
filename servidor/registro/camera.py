import cv2 
import os

class VideoCamera(object):
    def __init__(self): 
        self.face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        self.video = cv2.VideoCapture(0)  # Abertura da câmera no meu caso é notebook então, é index=0 
        
        if not self.video.isOpened(): # Verifica se camera está aberta
            print("Erro ao acessar a câmera.")
        
        self.img_dir = "./tmp" 
        
        # Garanta que o diretório tmp seja criado
        if not os.path.exists(self.img_dir):
            os.makedirs(self.img_dir)  # Cria a pasta `tmp` se não existir
        
    def __del__(self):
        self.video.release()  # Libera a câmera ao destruir a classe
    
    def restart(self):
        self.video.release()  # Reinicia a câmera
        self.video = cv2.VideoCapture(0) # Cria instancia, se vc não ficar isso a camera nao inicia mais.
    
    # Retorna o frame modo normal do objeto
    def get_camera(self):
        ret, frame = self.video.read()  # Leitura do frame 
        if not ret:  # Verifica se a captura do frame foi bem-sucedida
            print("Falha ao capturar o frame.")
            return None 
        
        return ret, frame

    def detect_face(self): 
        ret, frame = self.get_camera()  # Leitura do frame
        if not ret:  # Verifica se a captura do frame foi bem-sucedida
            print("Falha ao capturar o frame.")
            return None 
        
        # Defina a região de interesse (ROI) onde o rosto será detectado
        altura, largura, _ = frame.shape
        centro_x, centro_y = int(largura/2), int(altura/2)
        a, b = 140, 180
        x1, y1 = centro_x - a, centro_y - b
        x2, y2 = centro_x + a, centro_y + b
        roi = frame[y1:y2, x1:x2]
         
        # Converta a ROI em escala de cinza para a detecção de faces 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        # Detecta faces no frame
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        cv2.ellipse(frame, (centro_x, centro_y), (a, b), 0, 0, 360, (0, 0, 255), 10)

        for (x, y, w, h) in faces:
            cv2.ellipse(frame, (centro_x, centro_y), (a, b), 0, 0, 360, (0, 255, 0), 10)
    
        # Retorna o frame com a face detectada como imagem JPEG
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()  # Converte o frame para formato JPEG em bytes
    
    def sample_faces(self, frame):
        ret, frame = self.get_camera()
        frame = cv2.flip(frame, 180)
        frame = cv2.resize(frame, (480, 360))

        # Detecta a face
        faces = self.face_cascade.detectMultiScale(
            frame, minNeighbors=20, minSize=(30, 30), maxSize=(400, 400))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
            cropped_face = frame[y:y+h, x:x+w]
            return cropped_face  # Retorna o rosto recortado