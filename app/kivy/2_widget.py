from kivy.app import App 
from kivy.lang import Builder

# A string do layout KV
layout = '''
BoxLayout:
    orientation: 'vertical'
    Button:
        text: 'Botão 1'
    Button:
        text: 'Botão 2'
'''

class MyApp(App):
    def build(self): 
        return Builder.load_string(layout)

if __name__ == '__main__':
    MyApp().run() 

# class MyApp(App):
#     def build(self):
#         layout = BoxLayout(orientation='horizontal')
#         layout.add_widget(Button(text='Botão 1'))
#         layout.add_widget(Button(text='Botão 2'))
#         return layout 
        
# if __name__ == '__main__':
#     MyApp().run()