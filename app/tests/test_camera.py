from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.lang import Builder 
from kivymd.uix.label import MDLabel 

from kivymd.uix.boxlayout import MDBoxLayout 
from kivymd.uix.screenmanager import ScreenManager 
from kivymd.uix.screen import MDScreen  

import cv2

Window.size = (360, 600) 

class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Chama o construtor da classe Screen 
        
        layout = MDBoxLayout(orientation="vertical") 
        self.add_widget(layout) 
         
        # Adiciona o widget de imagem
        self.image = Image()
        layout.add_widget(self.image) 
        
        
    def load_video(self, *args): 
        ret, frame = self.cap.read() # Leitura
        if not ret:
            print("Falha ao capturar o frame")
            return
        
        altura, largura, _ = frame.shape
        
        # Defina os parâmetros da elipse
        centro_x, centro_y = int(largura / 2), int(altura / 2)
        a, b = 140, 180  # Eixos maior e menor
        cor = (144, 238, 144)  # Verde claro (em BGR)

        # Desenhe a elipse com a cor verde claro
        cv2.ellipse(frame, (centro_x, centro_y), (a, b), 0, 0, 360, cor, 5)
 
        # Inverte a imagem e converte para o formato de textura
        buffer = cv2.flip(frame, 0).tobytes()
        
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt="bgr")
        texture.blit_buffer(buffer, colorfmt="bgr", bufferfmt="ubyte")
        self.image.texture = texture


    def open_camera_for_recognition(self): 
        # Remove a mensagem (Opcional) 
        # camera meio que sobrescreve esse widget.
        for widget in self.children:
            if isinstance(widget, MDLabel):
                self.remove_widget(widget)	
    
        # Iniciar captura de vídeo
        self.cap = cv2.VideoCapture(0) # index 0
        if self.cap.isOpened():
            print("Mostrando a câmera")         

            # Chama a função para carregar o vídeo
            Clock.schedule_interval(self.load_video, 1.0 / 60.0)
        
            print("Abriu a camera") 
        else:
            print("Falha ao abrir a câmera")

class ScreenManagerApp(ScreenManager):
    def open_camera_for_recognition(self):
        # Chama o método de MainScreen para abrir a câmera
        self.get_screen('main').open_camera_for_recognition()


class MainApp(MDApp):
    def build(self):
        return Builder.load_string("""
ScreenManagerApp:
    MainScreen:
        name: "main"
        MDLabel:
            text: "Clique no botão para reconhecimento"
            halign: "center"
            theme_text_color: "Secondary"
        
        MDRaisedButton:
            text: "Iniciar Reconhecimento"
            size_hint: None, None
            size: "200dp", "50dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.1}
            on_press: root.open_camera_for_recognition()
""") 

if __name__ == '__main__':
    MainApp().run()