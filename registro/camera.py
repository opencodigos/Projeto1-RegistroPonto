import cv2 

class VideoCamera(object):
    def __init__(self): 
        self.video = cv2.VideoCapture(0)  # Abertura da câmera no meu caso é notebook então, é index=0 
        
        if not self.video.isOpened(): # Verifica se camera está aberta
            print("Erro ao acessar a câmera.")
         
    def __del__(self):
        self.video.release()  # Libera a câmera ao destruir a classe
    
    def restart(self):
        self.video.release()  # Reinicia a câmera
        self.video = cv2.VideoCapture(0) # Cria instancia, se vc não ficar isso a camera nao inicia mais.
    
    def get_camera(self):
        ret, frame = self.video.read()  # Leitura do frame
        if not ret:  # Verifica se a captura do frame foi bem-sucedida
            print("Falha ao capturar o frame.")
            return None
            
        # Retorna o frame  como imagem JPEG
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()  # Converte o frame para formato JPEG em bytes
