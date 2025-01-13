from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.metrics import dp
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.text import LabelBase
<<<<<<< HEAD
=======
from plyer import filechooser
import uuid
import os
>>>>>>> a4447ad (Updated)

# Load KV Files
Builder.load_file('kv/main.kv')
Builder.load_file('kv/forgotpassword.kv')
Builder.load_file('kv/signup.kv')
Builder.load_file('kv/verifynum.kv')
Builder.load_file('kv/home.kv')
Builder.load_file('kv/earthquake.kv')
Builder.load_file('kv/fire.kv')
Builder.load_file('kv/eruption.kv')
Builder.load_file('kv/typhoon.kv')
Builder.load_file('kv/landslide.kv')
Builder.load_file('kv/emergency.kv')

# Font Registration
LabelBase.register(name='Montserrat', fn_regular='assets/fonts/Montserrat-Light.ttf')
LabelBase.register(name='Regular', fn_regular='assets/fonts/Montserrat-Regular.ttf')
LabelBase.register(name='Medium', fn_regular='assets/fonts/Montserrat-Medium.ttf')

# Emergency Popup Class
class EmergencyPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (0.8, 0.7)
        self.title = "Emergency Report"

        layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))

        layout.add_widget(Label(text="[color=000000ff][b]REPORT AN EMERGENCY[/b][/color]", markup=True, size_hint=(None, None), height=dp(30)))
        layout.add_widget(Label(text="[color=000000ff]Type of Disaster[/color]", markup=True))
        layout.add_widget(TextInput(size_hint=(None, None), size=(dp(200), dp(30)), multiline=False))
        layout.add_widget(Label(text="[color=000000ff]Send Location[/color]", markup=True))
        layout.add_widget(TextInput(size_hint=(None, None), size=(dp(200), dp(30)), multiline=False))

        btn_layout = BoxLayout(size_hint=(1, None), height=dp(50), spacing=dp(20))
        submit_button = Button(text="Submit", size_hint=(None, None), size=(dp(100), dp(40)))
        cancel_button = Button(text="Cancel", size_hint=(None, None), size=(dp(100), dp(40)))

        submit_button.bind(on_press=self.submit)
        cancel_button.bind(on_press=self.dismiss)

        btn_layout.add_widget(submit_button)
        btn_layout.add_widget(cancel_button)
        layout.add_widget(btn_layout)

        self.content = layout

    def submit(self, instance):
        print("Emergency Report Submitted")
        self.dismiss()

# Main Screen with Emergency Button
class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=dp(10), spacing=dp(10))
        self.popup = None

        self.add_widget(
            Button(
                text="[color=000000ff][b]EMERGENCY[/b][/color]",
                markup=True,
                font_size=dp(20),
                size_hint=(None, None),
                size=(dp(350), dp(55)),
                on_press=self.show_report_popup,
                background_color=(1, 0.957, 0.129, 1)
            )
        )

    def show_report_popup(self, instance):
        if not self.popup:
            self.popup = EmergencyPopup()
        self.popup.open()

# Login Page
class LoginPage(Screen):
    def login(self):
        self.manager.current = 'home'
        print("User Logged In")
    
    def signup(self):
        self.manager.current = 'signup'
        print('Redirecting to Signup Page')

    def forgotpassword(self):
        self.manager.current = 'forgot'
        print('Redirecting to Forgot Password')

# Forgot Password Page
class ForgotPasswordPage(Screen):
    def sendotp(self):
        self.manager.current = 'verify'
        print('OTP Sent to User')

    def submit(self):
        self.manager.current = 'login'
        print('OTP Verified')

# Signup Page
class SignUpPage(Screen):
    def submit(self):
        self.manager.current = 'verify'
        print('Proceeding to Verify Number')

    def cancel(self):
        self.manager.current = 'login'
        print("Signup Cancelled")

# Verify Page
class VerifyPage(Screen):
    def submit(self):
        self.manager.current = 'login'
        print('Verification Complete')
    
    def sendotp(self):
        print("Verification Code Resent")

# Home Page with Disaster Navigation
class HomePage(Screen):
    def logout(self):
        self.manager.current = 'login'
        print('Logged Out')

    def emergency(self):
        self.manager.current = 'emergency'
    
    def landslide(self):
        self.manager.current = 'landslide'
    
    def typhoon(self):
        self.manager.current = 'bagyo'

    def lindol(self):
        self.manager.current = 'lindol'
    
    def eruption(self):
        self.manager.current = 'eruption'
    
    def fire(self):
        self.manager.current = 'fire'

# Disaster Screens
class Earthquake(Screen):
    def back(self):
        self.manager.current = 'home'

    def emergency(self):
        self.manager.current = 'emergency'

class FireDisaster(Screen):
    def back(self):
        self.manager.current = 'home'

    def emergency(self):
        self.manager.current = 'emergency'

class Eruption(Screen):
    def back(self):
        self.manager.current = 'home'

    def emergency(self):
        self.manager.current = 'emergency'

class Typhoon(Screen):
    def back(self):
        self.manager.current = 'home'

    def emergency(self):
        self.manager.current = 'emergency'

class Landslide(Screen):
    def back(self):
        self.manager.current = 'home'

    def emergency(self):
        self.manager.current = 'emergency'

# Emergency Report Screen
class Emergency(Screen):
    def cancel(self):
        self.manager.current = 'home'

    def open_camera(self):
        filename=f'Phone storage/DCIM/Camera/{uuid.uuid4().hex}.jpg'
        try:
            camera.take_picture(
                filename=filename,
                on_complete=self.picture_taken
            )
        except Exception as e:
            print('Error Accessing Camera: {e}')
    
    def picture_taken(self, path):
        if path:
            new_path = os.path.join('Phone storage/DCIM/Camera', os.path.basename(path))
            print(f'Picture saved at {path}')

    def submit(self):
        self.manager.current = 'home'
        print('Emergency Reported Successfully')

# App Class with Screen Manager
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.transition = SlideTransition(direction='left')

        sm.add_widget(LoginPage(name='login'))
        sm.add_widget(ForgotPasswordPage(name='forgot'))
        sm.add_widget(SignUpPage(name='signup'))
        sm.add_widget(VerifyPage(name='verify'))
        sm.add_widget(HomePage(name='home'))
        sm.add_widget(Earthquake(name='lindol'))
        sm.add_widget(FireDisaster(name='fire'))
        sm.add_widget(Eruption(name='eruption'))
        sm.add_widget(Typhoon(name='bagyo'))
        sm.add_widget(Landslide(name='landslide'))
        sm.add_widget(Emergency(name='emergency'))

        Window.bind(size=self.adjust_fonts)
        return sm
    
    def adjust_fonts(self, *args):
        pass  # Implement dynamic font scaling if needed

if __name__ == '__main__':
    MyApp().run()
