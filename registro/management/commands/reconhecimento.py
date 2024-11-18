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
        reconhecedor = cv2.face.EigenFaceRecognizer_create()

        # Carregar o modelo de treinamento
        treinamento = Treinamento.objects.first()
        if not treinamento:
            print("Modelo de treinamento não encontrado.")
            return

        model_path = os.path.join(settings.MEDIA_ROOT, treinamento.modelo.name) # classificadorEigen.yml
        reconhecedor.read(model_path) 

        camera = cv2.VideoCapture(0)
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
                imagemFace = cv2.resize(imagemCinza[y:y+a,x:x+l], (largura, altura))  
                cv2.rectangle(frame,(x,y),(x+l,y+a),(0,255,0),2)
                label, result = reconhecedor.predict(imagemFace)  
                print(label)
                funcionario = Funcionario.objects.get(id=label)
                if funcionario:   
                    cv2.putText(frame, str(funcionario.nome).strip("(),'"), (x, y + a + 30), font, 1, (0, 255, 0), 2)
                else:
                    cv2.putText(frame, "Nenhum user encontrado", (x, y + a + 30), font, 1, (0, 0, 255), 2)
 
            cv2.imshow("Reconhecimento Facial", frame)

            # Parar ao pressionar a tecla 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        camera.release()
        cv2.destroyAllWindows()