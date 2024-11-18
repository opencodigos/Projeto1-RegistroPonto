from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout

class MyApp(App):
    def build(self): 
        layout = AnchorLayout(anchor_x='center', anchor_y='center')
        button = Button(text='Clique Aqui')
        button.bind(on_press=self.on_button_click) 
        layout.add_widget(button) 
        return layout

    def on_button_click(self, instance):
        print('Botão clicado!')

if __name__ == '__main__':
    MyApp().run()