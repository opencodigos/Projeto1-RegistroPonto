from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from datetime import datetime

Window.size = (340, 680)


class MainScreen(MDScreen):
    def show_recognized_user(self):

        # Navegar para a tela 'usuario' usando self.manager
        self.manager.current = 'usuario'

        # Define informações fictícias para exibição
        funcionario = {
            "foto": "./assets/teste.jpg",
            "nome": "Letícia Lima",
            "cpf": "123.456.789-00",
        }

        print(funcionario)

        # Atribui os valores aos widgets na tela UsuarioScreen
        usuario_screen = self.manager.get_screen('usuario')
        usuario_screen.ids.foto.source = funcionario["foto"]
        usuario_screen.ids.nome.text = f"Nome: {funcionario['nome']}"
        usuario_screen.ids.cpf.text = f"CPF: {funcionario['cpf']}"
        usuario_screen.ids.data_hora.text = f"Data e Hora: {datetime.now().strftime('%d/%m/%Y às %H:%M')}"

        # Torna o cartão visível na tela 'usuario'
        usuario_screen.ids.card.opacity = 1


class UsuarioScreen(MDScreen):
    pass


class ComprovanteScreen(MDScreen):
    pass


class ScreenManagerApp(ScreenManager):
    def show_recognized_user(self):
        # Chama o método de MainScreen para abrir a câmera
        self.get_screen('main').show_recognized_user()


class MainApp(MDApp):
    def build(self):
        return Builder.load_string("""
ScreenManagerApp:  
    MainScreen:
    UsuarioScreen:
    ComprovanteScreen:  
    
<MainScreen>:
    name: "main"
    MDScreen:  
        MDTopAppBar: 
            title: "Reconhecimento" 
            specific_text_color: 1, 1, 1, 1
            anchor_title: "center"
            md_bg_color: 0.173, 0.243, 0.314, 1
            elevation: 0.5
            pos_hint: {"top": 1}
        MDBoxLayout:
            orientation: "vertical" 
            adaptive_size: True
            spacing: "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.6}
            MDCard:
                id: headimage 
                size_hint: None, None
                size: "300dp", "300dp"
                pos_hint: {"center_x": 0.5} 
                AsyncImage: 
                    size_hint: (1, 1)
                    pos_hint: {'center_x': 0.5}
                    source: './assets/teste.jpg'
        MDRaisedButton:
            text: 'Registrar'
            font_size: '20sp'
            pos_hint: {'center_x': 0.5, 'center_y': 0.25}
            md_bg_color: 1, 0.388, 0.278, 1
            size_hint: (0.7, 0.1)  
            elevation: 0.5   
            on_press: root.show_recognized_user()
        
<UsuarioScreen>:
    name: "usuario"
    MDScreen: 
        md_bg_color: 0.941, 0.957, 0.973, 1
        MDTopAppBar: 
            title: "Usuário Identificado" 
            specific_text_color: 1, 1, 1, 1
            anchor_title: "center"
            md_bg_color: 0.173, 0.243, 0.314, 1
            elevation: 0.5
            pos_hint: {"top": 1}
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
        MDRaisedButton:
            text: 'Confirmar'
            font_size: '20sp'
            pos_hint: {'center_x': 0.5, 'center_y': 0.25}
            size_hint: (0.7, 0.1)
            elevation: 0.5   
            md_bg_color: 0.298, 0.686, 0.314, 1
            on_press: root.manager.current = 'comprovante' 
        MDRaisedButton:
            text: 'Não sou eu'
            font_size: '20sp'
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            size_hint: (0.7, 0.1)
            elevation: 0.5   
            md_bg_color: 0.9, 0.3, 0.3, 1
            on_press: root.manager.current = 'main'
                    
<ComprovanteScreen>:
    name: "comprovante"
    MDScreen: 
        md_bg_color: 0.941, 0.957, 0.973, 1
        MDTopAppBar: 
            title: "Comprovante" 
            specific_text_color: 1, 1, 1, 1
            anchor_title: "center"
            md_bg_color: 0.173, 0.243, 0.314, 1
            elevation: 0.5
            pos_hint: {"top": 1}
        MDCard:
            id: card_comprovante
            size_hint: None, None
            size: "280dp", "300dp"
            md_bg_color: 1.0, 0.976, 0.912, 1 
            pos_hint: {"center_x": 0.5, "center_y": 0.6}
            opacity: 1
            BoxLayout:
                orientation: "vertical"
                padding: "10dp"
                spacing: "10dp" 
                MDLabel:
                    text: 'Comprovante'
                    halign: 'center'
        MDRaisedButton:
            text: 'Fechar' 
            font_size: '20sp'
            pos_hint: {'center_x':0.5, 'center_y':0.2}
            md_bg_color: 1, 0.388, 0.278, 1
            size_hint: (0.7, 0.1)   
            elevation: 0.5    
            on_press: root.manager.current = 'main' 
""")


if __name__ == '__main__':
    MainApp().run()
