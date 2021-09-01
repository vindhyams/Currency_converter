import kivy
from kivy.app import App
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label 
kivy.require('2.0.0')
from kivy.uix.behaviors import ButtonBehavior


Builder.load_file('design.ky')


class ConvertScreen(Screen):
    def convert(self):
        self.manager.current="convert_screen" 
    def dollar(self,val):
        if(val.isalpha()):
            self.ids.answer.text="Enter a valid amount"
        elif(int(val)<=0):
            self.ids.answer.text="Enter A greater value"
        else:
            dollarvalue=int(val)*0.014
            passing="The Dollar value is"
            self.ids.answer.text=passing+" "+str(dollarvalue)
        
         
    def yen(self,val):
        
        if(val.isalpha()):
            self.ids.answer.text="Enter a valid amount"
        elif(int(val)<=0):
            self.ids.answer.text="Enter A greater value"
        else:
            yenvalue=int(val)*1.49
            passing="The Yen value is"
            self.ids.answer.text=passing+" "+str(yenvalue)
       
    def euro(self,val):
        if(val.isalpha()):
            self.ids.answer.text="Enter a valid amount"
        elif(int(val)<=0):
            self.ids.answer.text="Enter A greater value"
        else:
            eurovalue=int(val)*0.012
            passing="The Euro value is"
            self.ids.answer.text=passing+" "+str(eurovalue)
        
    def won(self,val):
        if(val.isalpha()):
            self.ids.answer.text="Enter a valid amount"
        elif(int(val)<=0):
            self.ids.answer.text="Enter A greater value"
        else:
            wonvalue=int(val)*15.81
            passing="The Won value is"
            self.ids.answer.text=passing+" "+str(wonvalue)
        


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__=='__main__':
    MainApp().run()
#to import file we use builder file