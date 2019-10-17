import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import random,string
Builder.load_string('''
<updlbl>:
    orientation: 'vertical'
    Label:
        id: updlbl
        text: 'Update Label'
    Button:
        text: 'Click me'
        on_press: root.upd('updated text')
 ''')

class updlbl(BoxLayout):
     def __init__(self, **kwargs):
       super(updlbl,self).__init__(**kwargs)
       pass

     def upd(self,txt):
       self.ids.updlbl.text = txt




class UpdateLabel(App):
     def build(self):
         self.title = "Update Label"
         return updlbl()

if __name__ == '__main__':
    UpdateLabel().run()
