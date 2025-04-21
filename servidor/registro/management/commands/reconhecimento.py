import cv2
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from registro.models import Funcionario, Treinamento

class Command(BaseCommand):
    help = "Comando para teste de reconhecimento facial com exibição ao vivo da câmera"

    def handle(self, *args, **kwargs): 
        self.reconhecer_faces()

    def reconhecer_faces(self): 
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        reconhecedor = cv2.face.LBPHFaceRecognizer_create(radius=2, neighbors=12, grid_x=8, grid_y=8)

        # Carregar o modelo de treinamento
        treinamento = Treinamento.objects.first()
        if not treinamento:
            print("Modelo de treinamento não encontrado.")
            return

        model_path = os.path.join(settings.MEDIA_ROOT, treinamento.modelo.name) # classificadorEigen.yml
        reconhecedor.read(model_path) 

        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            print("Unable to open camera")
            exit()
            
        largura, altura = 220, 220
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL 
        
        while True:
            ret, frame = camera.read()
            if not ret:
                print("Erro ao acessar a câmera.")
                break
                 
            frame = cv2.resize(frame, (480, 360))
            imagemCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces_detectadas = face_cascade.detectMultiScale(imagemCinza, minNeighbors=20, minSize=(30, 30), maxSize=(400, 400))

            for (x,y,l,a) in faces_detectadas:
                # imagemFace = imagemCinza[y-10:y+a+10, x-10:x+l+10]
                
                imagemFace = imagemCinza[y:y+a, x:x+l]
                if imagemFace.size == 0:
                    continue
                imagemFace = cv2.resize(imagemFace, (largura, altura))

                imagemFace = cv2.resize(imagemFace, (largura, altura))
                
                # Aplicar mesmo pré-processamento usado no treinamento
                imagemFace = cv2.equalizeHist(imagemFace)
                imagemFace = cv2.normalize(imagemFace, None, 0, 255, cv2.NORM_MINMAX)
                
                cv2.rectangle(frame,(x,y),(x+l,y+a),(0,255,0),2) 
                label, confidence = reconhecedor.predict(imagemFace)
                
                # Só mostrar reconhecimento se confiança for boa
                if confidence < 50:  # ajuste este valor conforme necessário
                    try:
                        funcionario = Funcionario.objects.get(id=label)
                        nome = str(funcionario.nome).strip("(),'")
                        conf = f"{nome} ({int(confidence)})"
                        cv2.putText(frame, conf, (x, y + a + 30), font, 1, (0, 255, 0), 2)
                    except Funcionario.DoesNotExist:
                        cv2.putText(frame, "Desconhecido", (x, y + a + 30), font, 1, (0, 0, 255), 2)
                else:
                    cv2.putText(frame, f"Conf: {int(confidence)}", (x, y + a + 50), font, 1, (255, 255, 0), 2)

                    # cv2.putText(frame, "Baixa confiança", (x, y + a + 30), font, 1, (0, 0, 255), 2)
 
            cv2.imshow("Reconhecimento Facial", frame)

            # Parar ao pressionar a tecla 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        camera.release()
        cv2.destroyAllWindows()