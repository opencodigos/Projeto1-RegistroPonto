from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
         
        self.img = Image() 
        layout.add_widget(self.img)
 
        button = Button(text='Mostrar imagem')
        button.bind(on_press=self.on_button_click_1)
        layout.add_widget(button)

        button = Button(text='Remover imagem')
        button.bind(on_press=self.on_button_click_2)
        layout.add_widget(button)
        
        return layout

    def on_button_click_1(self, instance):
        print("Cliquei 1")
        img = '../assets/teste.jpg'
        self.img.source = img

    def on_button_click_2(self, instance):
        print("Cliquei 2")
        self.img.source = ''
        
if __name__ == '__main__':
    MyApp().run()



# class MyApp(App):
#     def build(self): 
#         return Image(source='../assets/teste.jpg') 
    
# if __name__ == '__main__':
#     MyApp().run()