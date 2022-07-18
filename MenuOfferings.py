from breezypythongui import EasyFrame
from tkinter import *
"""
Author: Steven Tarmann
Date: 07/17/2022
Program to allow the user to select menu offerings PPPORderPlacer
"""

""" Need to offer a selection of pizza types and sizes - both should be radio buttons
        Once a pizza is selected the next window should offer a customizable menu with additional offerings
    Allow user to add pizza to cart
    Once pizza is added the user should be able to add another pizza or continue to payment selection
    Once the user selects a payment option display a time estimate based on number of items ordered - add an addition amount of time if delivery
"""

class MenuChoices(EasyFrame):
    """Window interface to select menu offerings and customize them"""
    def __init__(self):
        """Creates the initial window and adds items on the screen"""
        EasyFrame.__init__(self)

        self.windowLabel = self.addLabel(text="Select a pizza option", row=0, column=0)

        # List to hold menu offerings and create a modular display on the screen
        self.PIZZAS = [
            "Pepperoni",
            "Triple Cheese",
            "Hawaiian",
            "Supreme",
            "Meat Lovers",
            "Chicken Bacon Ranch",
            "Margarita"
        ]
        
        # Creates a radio button object with a modular length
        self.pizzaGroup = self.addRadiobuttonGroup(row=1, column=0, rowspan=len(self.PIZZAS), columnspan=2)

        # Creates the radio buttons and stores them in a list so they can be accessed with a modular approach
        self.pizzaButtons = []
        self.selectedPizza = StringVar()
        for text in self.PIZZAS:
            self.pizzaButtons.append(self.pizzaGroup.addRadiobutton(text=text))
        self.pizzaGroup.setSelectedButton(self.pizzaButtons[0])

        # Submit button that calls the customize method
        self.submit_btn = self.addButton(text="Customize >>", row=len(self.PIZZAS)+1, column=3, command=self.customize)


    def customize(self):
        """Method to provide customization for selected menu offering"""
        self.windowLabel["text"] = "Select additional toppings"

        # Get the value of the selected pizza before deleting the radio buttons
        self.selectedPizza = self.pizzaGroup.getSelectedButton()["text"]

        # Clear the previous screen objects to make way for new ones
        self.pizzaGroup.destroy()
        self.submit_btn.destroy()

        # Creates a list of strings for modular check box creation
        self.CUSTOMIZABLES = [
            "Extra Cheese",
            "Extra Sauce",
            "Extra Meat",
            "Thin Crust",
            "Extra Veggies",
            "Square Cut",
            "Well Done",
            "Extra Dipping Sauce"
        ]

        # Int to keep track of current row for adding items modular to the grid
        self.custRow = IntVar()
        self.custRow = 1

        # Creates a list of checkboxes and adds them to the grid
        self.checkboxes = []
        for text in self.CUSTOMIZABLES:
            self.checkboxes.append(self.addCheckbutton(text=text, row=self.custRow, column=0, sticky=W))
            self.custRow += 1

        # Submit button that calls the addtoCart method
        self.submit_btn = self.addButton(text="Add to Cart", row=self.custRow, column=1, command=self.addtoCart)
        self.custRow += 1


    def addtoCart(self):
        """Method that displays the menu choices and gives user option to add more items or continue to payment screen"""

        # Create a list of all the checked boxes in the list
        self.checked = []
        for box in self.checkboxes:
            if box.isChecked():
                self.checked.append(box)
        
        # Reset screen prompt
        self.windowLabel["text"] = "Cart Items:"

        # Display the pizza selection with the customization items
        self.pizzaLabel = self.addLabel(text=self.selectedPizza, row=self.custRow, column=0)
        self.custRow += 1
        self.customlabels = []
        for checkedbox in self.checked:
            self.customlabels.append(self.addLabel(text="\t-" + checkedbox["text"], row=self.custRow, column=0))
            self.custRow += 1
        
        # Clear the screen
        self.submit_btn.destroy()
        for box in self.checkboxes:
            box.destroy()
        
        # Create the buttons for starting over or continuing to payment
        self.keepShopping_btn = self.addButton(text="Add another item", row = self.custRow, column=1, command=self.startover)
        self.custRow += 1
        self.orlabel = self.addLabel(text="or", row=self.custRow, column=1)
        self.custRow += 1
        self.continuetopay_btn = self.addButton(text="Select payment option", row=self.custRow, column=1)
        self.custRow += 1


    def startover(self):
        """ Clears the screen and starts over with the initial items
            NOTE: Does not use the __init__ method because it will create a new window
                POSSIBLE SOLUTION: Use a global variable to track all of the items so far and destroy the current window with self.destoy() and then use self.__init__()
                
                Current solution uses a 'copy paste' of the __init__ method"""

                
        self.windowLabel.destroy()
        self.pizzaLabel.destroy()
        for label in self.customlabels:
            label.destroy()
        self.keepShopping_btn.destroy()
        self.orlabel.destroy()
        self.continuetopay_btn.destroy()

        self.windowLabel = self.addLabel(text="Select a pizza option", row=0, column=0)

        self.PIZZAS = [
            "Pepperoni",
            "Triple Cheese",
            "Hawaiian",
            "Supreme",
            "Meat Lovers",
            "Chicken Bacon Ranch",
            "Margarita"
        ]
        
        self.pizzaGroup = self.addRadiobuttonGroup(row=1, column=0, rowspan=len(self.PIZZAS), columnspan=2)
        self.pizzaButtons = []
        self.selectedPizza = StringVar()
        for text in self.PIZZAS:
            self.pizzaButtons.append(self.pizzaGroup.addRadiobutton(text=text))
        self.pizzaGroup.setSelectedButton(self.pizzaButtons[0])

        
        
            


        self.submit_btn = self.addButton(text="Customize >>", row=len(self.PIZZAS)+1, column=3, command=self.customize)

    def customize(self):
        self.windowLabel["text"] = "Select additional toppings"
        self.selectedPizza = self.pizzaGroup.getSelectedButton()["text"]
        self.pizzaGroup.destroy()
        self.submit_btn.destroy()

        self.CUSTOMIZABLES = [
            "Extra Cheese",
            "Extra Sauce",
            "Extra Meat",
            "Thin Crust",
            "Extra Veggies",
            "Square Cut",
            "Well Done",
            "Extra Dipping Sauce"
        ]
        self.custRow = IntVar()
        self.custRow = 1

        self.checkboxes = []
        for text in self.CUSTOMIZABLES:
            self.checkboxes.append(self.addCheckbutton(text=text, row=self.custRow, column=0, sticky=W))
            self.custRow += 1

        self.submit_btn = self.addButton(text="Add to Cart", row=self.custRow, column=1, command=self.addtoCart)
        self.custRow += 1
        

def main():
    MenuChoices().mainloop()

main()