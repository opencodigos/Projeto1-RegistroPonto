from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout

class MyForm(GridLayout):
    def __init__(self, **kwargs):
        super(MyForm, self).__init__(**kwargs)
        self.cols = 2

        # Título do Formulário
        self.add_widget(Label(text="Cadastro de Usuário", 
                              font_size=24, bold=True, color=[1, 1, 0, 1]))
        self.add_widget(Label()) 

        
        self.add_widget(Label(text="First Name: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.add_widget(self.lastName)

        self.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)
        
        # Campo Senha
        self.add_widget(Label(text="Senha:"))
        self.senha_input = TextInput(password=True, hint_text="Digite sua senha")
        self.add_widget(self.senha_input)
        
        # Opção de Aceitação dos Termos
        self.add_widget(Label(text="Aceita os termos de uso?"))

        # Layout Horizontal para o CheckBox e o Label
        checkbox_layout = BoxLayout(orientation='horizontal')
        self.checkbox = CheckBox()  # Criação do CheckBox
        self.checkbox.bind(active=self.on_checkbox_active)  # Função que reage ao clique
        checkbox_layout.add_widget(self.checkbox)
        self.add_widget(checkbox_layout)
        
        # Botão Enviar
        self.submit_button = Button(text="Enviar")
        self.submit_button.bind(on_press=self.enviar_formulario)
        self.add_widget(self.submit_button)
        
        # Botão Limpar
        self.submit_button = Button(text="Limpar")
        self.submit_button.bind(on_press=self.limpar_fomrulario)
        self.add_widget(self.submit_button)
        
    def enviar_formulario(self, instance):
        nome = self.name.text
        sobrenome = self.lastName.text
        email = self.email.text
        senha = self.senha_input.text
        if self.checkbox.active:
            print(f"Nome: {nome}, Sobrenome: {sobrenome}, Email: {email}, Senha: {senha}")
        else:
            print("Por favor, aceite os termos antes de enviar.")

    def limpar_fomrulario(self, instance):
        self.name.text = ''
        self.lastName.text = ''
        self.email.text = ''
        self.senha_input.text = ''
        self.checkbox.active = False
        print("Limpo")
            
    def on_checkbox_active(self, checkbox, value):
        if value:
            print("Checkbox está marcado!")
        else:
            print("Checkbox desmarcado!")

class MyApp(App):
    def build(self):
        return MyForm()
        
if __name__ == '__main__':
    MyApp().run()