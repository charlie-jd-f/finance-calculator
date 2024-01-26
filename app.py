import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

import finance_calcutions

# Set initial window parameters
Window.size = (300,450)
Window.minimum_width = 300
Window.minimum_height= 450
Window.clearcolor = (0.95,0.95,0.95,1)

# Main window (Homescreen)
class MainWindow(Screen): 
    pass

# Window which calculate the investments
class InvestmentWindow(Screen):
    
    # Increases the number of years button is clicked
    def increase_year(self):
        number = int(self.years.text)
        number += 1
        self.years.text = str(number)
        
    # Decreases the number of years when button is clicked
    def decrease_year(self):
        if int(self.years.text) == 0:
            pass
        else:
            number = int(self.years.text)
            number -= 1
            self.years.text = str(number)
    
    # Displayed a pop up to the user when interest is calculated
    def show_interest(self):
        deposit = float(self.deposit.text)
        rate = float(self.invest_rate.text)
        time = int(self.years.text)
        
        # Calculates the simple and compound interest
        simple = round(finance_calcutions.simple_interest(deposit,rate,time),2)
        compound = round(finance_calcutions.compound_interest(deposit,rate,time),2)
        
        # Displays the simple and compound interest as a pop up
        layout = FloatLayout(size=(150,150))
        
        interest_popup = Label(
            text="Your results:\n\n"\
                "Simple Interest:\n"\
                f"£{simple}\n\n"\
                "Compound:\n"
                f"£{compound}\n\n"\
                "To discuss your investents options\n"\
                "either contact us on 0161XXXXXX or\n"\
                "visit us in your local branch.",
            font_size=14,
            size=(0.6,0.5),
            pos_hint = {"center_x":0.5,"center_y":0.5},
            halign="center")
        layout.add_widget(interest_popup)
        
        popup = Popup(title = "Interest",content = layout,size=(150,150),size_hint=(0.9,0.6))
        popup.open()
        
        # resets values to 0
        self.deposit.text="0.00"
        self.invest_rate.text="0.00"
        self.years.text="0"
            
        


class MortgageWindow(Screen):
    
    # Increases the number of months when button is clicked
    def increase_month(self):
        number = int(self.months.text)
        number += 1
        self.months.text = str(number)
        
    # Decreases the number of months which button is clicked
    def decrease_month(self):
        if int(self.months.text) == 0:
            pass
        else:
            number = int(self.months.text)
            number -= 1
            self.months.text = str(number)
        
    # Displays the bond repayment as a pop up    
    def show_bond(self):
        value = float(self.value.text)
        rate = float(self.bond_rate.text)
        time = int(self.months.text)
        
        # Accounts for division by zero errors
        if rate == 0 or time == 0:
            layout = FloatLayout(size=(150,150))
            error_popup = Label(
                text="Division by zero error! Try again!",
                font_size=14,
                size=(0.6,0.5),
                pos_hint={"center_x":0.5,"center_y":0.5},
                halign="center")
            layout.add_widget(error_popup)
            
            popup = Popup(
                title = "Warning",
                content = layout,
                size = (150,150),
                size_hint = (0.9,0.6))
            popup.open()
        else:
            # Calculates the bond repayment
            bond = round(finance_calcutions.bond_repayment(value,rate,time),2)
                
            # Displays the bond repayment cost to the user
            layout = FloatLayout(size=(150,150))
            
            interest_popup = Label(
                text="Your results:\n\n"\
                    "Monthly Payments:\n"\
                    f"£{bond}\n\n"\
                    "To discuss your mortgage options\n"\
                    "either contact us on 0161XXXXXX or\n"\
                    "visit us in your local branch.",
                font_size=14,
                size=(0.6,0.5),
                pos_hint = {"center_x":0.5,"center_y":0.5},
                halign="center")
            layout.add_widget(interest_popup)
            
            popup = Popup(
                title = "Interest",
                content = layout,
                size=(150,150),
                size_hint=(0.9,0.6))
            popup.open()
            
            self.value.text="0.00"
            self.bond_rate.text="0.00"
            self.months.text="0"

# Class to manage the different windows
class WindowManager(ScreenManager):
    pass

# Imports the kivy file
kv = Builder.load_file("my.kv")

# Compiles and runs the app
class MyMainApp(App):
    def build(self):
        return kv

    
if __name__== "__main__":
    MyMainApp().run()