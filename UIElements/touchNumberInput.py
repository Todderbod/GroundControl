'''

This allows the user to touch or keyboard input a number when it is the content of a popup

'''
from   kivy.uix.gridlayout                       import   GridLayout
from   kivy.properties                           import   ObjectProperty
from   kivy.properties                           import   StringProperty

class TouchNumberInput(GridLayout):
    cancel = ObjectProperty(None)
    done   = ObjectProperty(None)
    
    inputText = StringProperty("this")
    
    def addText(self, text):
        self.inputText = self.inputText + text