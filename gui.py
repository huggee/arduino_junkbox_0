from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout 
from kivy.properties import StringProperty, ListProperty

class TextWidget(Widget):
    text = StringProperty()
    color = ListProperty([1,1,1,1])

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = 'start'

    def buttonClicked(self):
        self.text = 'Good morning'
        self.color = [1, 0, 0, 1]

    def buttonClicked2(self):
        self.text = 'Hello'
        self.color = [0, 1, 0, 1]

    def buttonClicked3(self):
        self.text = 'Good evening'
        self.color = [0, 0, 1, 1]

class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'greeting'

    def build(self):
        return TextWidget()

class Widgets(Widget):
    pass

class kvfile(App):
    def build(self):
        return FloatLayout()
        # return Widgets()

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Username:"))
        self.username=TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text="Password:"))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)

        self.add_widget(Label(text="Two Factor Auth:"))
        self.tfa = TextInput(multiline=False, password=True)
        self.add_widget(self.tfa)

class IntroKivy(App):
    def build(self):
        return LoginScreen()

if __name__ == "__main__":
    TestApp().run()
    # kvfile().run()
    # IntroKivy().run()
