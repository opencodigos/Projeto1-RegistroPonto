from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.animation import Animation

class MyApp(App):
    def build(self):
        layout = AnchorLayout(anchor_x='center', anchor_y='center')
        button = Button(text='Clique Aqui', size_hint=(None, None), 
                        size=(200, 60), background_color=(1, 0, 0, 1))

        button.bind(on_press=self.on_button_click) 
        layout.add_widget(button) 
         
        return layout

    def on_button_click(self, instance):
        print('Botão clicado!')
        self.animate_button(instance)

    def animate_button(self, button):
        anim = Animation(size=(200, 100), duration=1)
        anim.start(button)
    
if __name__ == '__main__':
    MyApp().run()