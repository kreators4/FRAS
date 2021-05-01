import os
import check_camera
import Capture_Image
import Train_Image
import Recognize


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols = 1
        
        self.submit = Button(text = "Check Camera",font_size=20)
        self.submit.bind(on_press = self.check)
        self.add_widget(self.submit)
        
        self.submit = Button(text = "Capture camera",font_size=20)
        self.submit.bind(on_press = self.capture)
        self.add_widget(self.submit)
        
        self.submit = Button(text = "Train images",font_size=20)
        self.submit.bind(on_press = self.train)
        self.add_widget(self.submit)
        
        self.submit = Button(text = "Recognise Faces",font_size=20)
        self.submit.bind(on_press = self.recognise)
        self.add_widget(self.submit)
        
    
    def check(self, instance):
        check_camera.camer()
        
    def capture(self, instance):
        Capture_Image.takeImages()
    
    def train(self, instance):
        Train_Image.TrainImages()
        
    def recognise(self, instance):
        Recognize.recognize_attendence()
      
class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()
    



