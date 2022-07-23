"""
Author: Steven Tarmann
Date: 07/17/2022
Program to allow the user to select menu offerings PPPORderPlacer
"""

# Import modules
from breezypythongui import EasyFrame
from tkinter import *



class MenuChoices(EasyFrame):
    """Window interface to select menu offerings and customize them"""
    def __init__(self):
        """Creates the initial window and adds items on the screen"""
        EasyFrame.__init__(self)

        # Create a global variable to store the order in a dictionary for other .py files to use once the window is closed
        global orders
        orders = {}

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
        self.customlabels = []
        self.toppingslist = []
        for checkedbox in self.checked:
            #self.customlabels.append(self.addLabel(text='\t-' + checkedbox['text'], row=self.custRow, column=0))
            self.toppingslist.append(checkedbox['text'])
            #self.custRow += 1
        
        # Update the orders dictionary
        orders.update({self.selectedPizza:self.toppingslist})
        self.orderitems = orders.items()

        # Create labels for the pizza and toppings ordered
        for pizza, customlist in self.orderitems:
            self.pizzaLabel = self.addLabel(text=pizza, row=self.custRow, column=0)
            self.custRow += 1
            for item in customlist:
                self.customlabels.append(self.addLabel(text="\t-" + item, row=self.custRow, column=0))
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
        self.continuetopay_btn = self.addButton(text="Order Complete", row=self.custRow, column=1, command=self.complete)
        self.custRow += 1


    def startover(self):
        """ Clears the screen and starts over with the initial items
            NOTE: Does not use the __init__ method because it will create a new window"""

        # Clear the screen
        self.windowLabel.destroy()
        self.pizzaLabel.destroy()
        for label in self.customlabels:
            label.destroy()
        self.keepShopping_btn.destroy()
        self.orlabel.destroy()
        self.continuetopay_btn.destroy()

        # Create a new heading
        self.windowLabel = self.addLabel(text="Select a pizza option", row=0, column=0)

        # List of pizza options
        self.PIZZAS = [
            "Pepperoni",
            "Triple Cheese",
            "Hawaiian",
            "Supreme",
            "Meat Lovers",
            "Chicken Bacon Ranch",
            "Margarita"
        ]
        
        # Create the radio buttons
        self.pizzaGroup = self.addRadiobuttonGroup(row=1, column=0, rowspan=len(self.PIZZAS), columnspan=2)
        self.pizzaButtons = []
        self.selectedPizza = StringVar()
        for text in self.PIZZAS:
            self.pizzaButtons.append(self.pizzaGroup.addRadiobutton(text=text))
        self.pizzaGroup.setSelectedButton(self.pizzaButtons[0])

        # Create button run the customize method
        self.submit_btn = self.addButton(text="Customize >>", row=len(self.PIZZAS)+1, column=3, command=self.customize)

    def customize(self):
        """Method to allow the user to customize their pizza selection"""

        # Create heading
        self.windowLabel["text"] = "Select additional toppings"

        # Get the value of the selected pizza before the screen is cleared
        self.selectedPizza = self.pizzaGroup.getSelectedButton()["text"]

        # Clear the screen
        self.pizzaGroup.destroy()
        self.submit_btn.destroy()

        # Create a list of possible toppings for check box creation
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

        # Create a custom row int variable to have a modular row display when adding new toppings
        self.custRow = IntVar()
        self.custRow = 1

        # Create a list of checkboxes corresponding to the list above
        self.checkboxes = []
        for text in self.CUSTOMIZABLES:
            self.checkboxes.append(self.addCheckbutton(text=text, row=self.custRow, column=0, sticky=W))
            self.custRow += 1

        # Submit button that calls addtoCart method
        self.submit_btn = self.addButton(text="Add to Cart", row=self.custRow, column=1, command=self.addtoCart)
        self.custRow += 1


    def complete(self):
        """Method to provide instruction to move on a notification of completion of this module"""
        self.windowLabel["text"] = "Close this window to continue to payment"
        self.addLabel(text="Your Order:", row=1, column=0)
        self.keepShopping_btn.destroy()
        self.orlabel.destroy()
        self.continuetopay_btn.destroy()

        


# Main method to run the window
def main():
    order = MenuChoices()
    order.mainloop()

main()