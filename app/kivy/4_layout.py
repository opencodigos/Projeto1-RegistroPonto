from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=2) 
        layout.add_widget(Label(text='Hello world 1', font_size='20sp'))
        layout.add_widget(Label(text='Hello world 2', font_size='20sp'))
        layout.add_widget(Button(text='Botão 1'))
        layout.add_widget(Button(text='Botão 2')) 
        return layout
    
if __name__ == '__main__':
    MyApp().run()