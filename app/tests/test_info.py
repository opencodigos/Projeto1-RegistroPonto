from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager 
from kivy.core.window import Window  

from datetime import datetime

Window.size = (340, 680)

class MainScreen(MDScreen):   
    def show_recognized_user(self):
        # Define informações fictícias para exibição
        funcionario = {
            "foto": "./assets/teste.jpg",
            "nome": "Letícia Lima",
            "cpf": "123.456.789-00", 
        }

        print(funcionario) 
        
        # Atribui os valores aos widgets
        self.ids.foto.source = funcionario["foto"]
        self.ids.nome.text = f"Nome: {funcionario['nome']}"
        self.ids.cpf.text = f"CPF: {funcionario['cpf']}"
        self.ids.data_hora.text = f"Data e Hora: {datetime.now().strftime('%d/%m/%Y às %H:%M')}" 


        # Torna o cartão visível
        self.ids.card.opacity = 1
        

class ScreenManagerApp(ScreenManager):
    def show_recognized_user(self):
        # Chama o método de MainScreen para abrir a câmera
        self.get_screen('main').show_recognized_user()


class MainApp(MDApp):
    def build(self):
        return Builder.load_string("""
ScreenManagerApp:
    MainScreen:
        name: "main"

<MainScreen>:
    MDBoxLayout:
        orientation: "vertical"   
        pos_hint: {"center_x": 0.5, "center_y": 0.6} 
        MDLabel:
            text: "Clique no botão para reconhecimento"
            halign: "center"
            theme_text_color: "Secondary"

    MDRaisedButton:
        text: "Iniciar Reconhecimento"
        size_hint: None, None
        size: "200dp", "50dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.1}
        on_press: root.show_recognized_user() 
        
    MDCard:
        id: card
        size_hint: None, None
        size: "280dp", "300dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        opacity: 0
        
        BoxLayout:
            orientation: "vertical"
            padding: "10dp"
            spacing: "10dp"
            AsyncImage:
                id: foto
                size_hint: (1, 0.5)
                pos_hint: {"center_x": 0.5}
            MDLabel:
                id: nome
                adaptive_size: True
                theme_text_color: "Secondary"
                size_hint_y: None  
                pos_hint: {"center_x": .5, "center_y": .5}  
                padding: "4dp", "4dp"
            MDLabel:
                id: cpf
                adaptive_size: True
                theme_text_color: "Secondary"
                size_hint_y: None  
                pos_hint: {"center_x": .5, "center_y": .5}  
                padding: "4dp", "4dp"
            MDLabel:
                id: data_hora
                adaptive_size: True
                theme_text_color: "Secondary"
                size_hint_y: None  
                pos_hint: {"center_x": .5, "center_y": .5}  
                padding: "4dp", "4dp"    
    
""") 

if __name__ == '__main__':
    MainApp().run()
