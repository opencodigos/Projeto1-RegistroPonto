from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = AnchorLayout(anchor_x='center', anchor_y='center')
        button = Button(text='Clique Aqui', size_hint=(None, None), size=(200, 100), background_color=(1, 0, 0, 1))
        layout.add_widget(button) 
        return layout  
        
if __name__ == '__main__':
    MyApp().run()