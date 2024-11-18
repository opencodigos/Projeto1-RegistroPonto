from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        input_field = TextInput(hint_text='Digite algo aqui') 
        layout.add_widget(input_field)

        button = Button(text='Imprimir Texto')
        button.bind(on_press=self.on_button_click)
        layout.add_widget(button)

        self.input_field = input_field

        return layout

    def on_button_click(self, instance):
        print(self.input_field.text)

if __name__ == '__main__':
    MyApp().run()