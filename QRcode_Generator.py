from turtle import title
import qrcode
from tkinter import Button, dialog
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog

class QRApp(MDApp):
    def build(self):

        screen=Screen()
        self.theme_cls.theme_style="Light"
        self.textinput_link=MDTextField (hint_text='Enter a URL to generate QR code',
        pos_hint= {'center_x': 0.5,'center_y': 0.6},size_hint_x= None,width=300)
        self.pngsave_link=MDTextField (hint_text='Enter file name to save QR code',
        pos_hint= {'center_x': 0.5,'center_y': 0.5},size_hint_x= None,width=300)
        button=MDRectangleFlatButton(text="Generate QR code", pos_hint= {'center_x': 0.5,'center_y': 0.4},
        on_release= self.generate_code)
        screen.add_widget(self.textinput_link)
        screen.add_widget(self.pngsave_link)
        screen.add_widget(button)
        return screen



    def generate_code(self,obj):
    
        qr = qrcode.QRCode(version = 1, error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size = 10,
                   border = 5)
    
        qr.add_data(self.textinput_link.text)
        qr.make(fit=True)
        a=self.pngsave_link.text + ".png"
        print(a)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(a)
        #QRApp.destroy_settings
            

QRApp().run()


