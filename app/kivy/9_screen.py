from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label

class ScreenOne(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Tela 1", font_size=40))
        
        button = Button(text="Ir para Tela 2 >>", size_hint=(None, None), size=(200, 60))
        button.bind(on_press=self.change_screen)
        self.add_widget(button)

    def change_screen(self, instance):
        self.manager.current = 'screen2'

class ScreenTwo(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Tela 2", font_size=40))
        
        button = Button(text="<< Voltar para Tela 1", size_hint=(None, None), size=(200, 60))
        button.bind(on_press=self.change_screen)
        self.add_widget(button)

    def change_screen(self, instance):
        self.manager.current = 'screen1'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ScreenOne(name='screen1'))
        sm.add_widget(ScreenTwo(name='screen2'))
        return sm

if __name__ == '__main__':
    MyApp().run()