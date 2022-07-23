"""
Author: Steven Tarmann
Date: 07/22/2022
Program to display total and process payment for PPPOrderPlacer
"""

# Import modules
from breezypythongui import EasyFrame
from tkinter import *
from DeliveryMode import *
from MenuOfferings import *


class PaymentScreen(EasyFrame):
    """Window that guides a user through payment"""
    def __init__(self, dORpform, orderform):
        """Creates the window and it's attributes and displays them on the screen"""
        EasyFrame.__init__(self)
    
        # Creates a list of the values from the dictionary to read them in to determine if the order was delivery or pickup
        self.dORpkey = list(dORpform)

        # Displays information for pickup and creates an option to pay at the store
        if self.dORpkey[0] == "Pickup":
            self.prompt = self.addLabel(text="Pickup Order", row=0, column=0)
            self.payatstore_btn = self.addButton(text="Pay at Store", row=2, column=1, command=self.payatstore)

        # Displays information for delivery and creates an option to pay with cash upon the driver's arrival
        if self.dORpkey[0] == "Delivery":
            self.prompt = self.addLabel(text="Delivery Order", row=0, column=0)
            self.paycash_btn = self.addButton(text="Pay with Cash", row=2, column=1, command=self.paycash)

        # Creates a label and button that allows the user to pay now with card - button calls paycard method
        self.choosepayment_lbl = self.addLabel(text="Select a payment option", row=1, column=0)
        self.paycard_btn = self.addButton(text="Pay Now with Card", row=3, column=1, command=self.paycard)

        # Create number variables for calculating cost
        self.pizzanum = IntVar()
        self.toppingsnum = IntVar()
        self.totalcost = DoubleVar()
        self.costperpizza = DoubleVar()
        self.costpertopping = DoubleVar()
        self.salesTax = DoubleVar()
        self.deliveryFee = DoubleVar()
        self.subtotal = DoubleVar()

        # Initialize cost variables
        self.pizzanum = 0
        self.toppingsnum = 0
        self.costperpizza = 9.50
        self.costpertopping = 0.50
        self.salesTax = 0.08
        self.deliveryFee= 5.00

        # Create a list of keys from the imported orderform dictionary
        self.orderlist = orderform.items()

        # Create empty lists for creating and storing labels in case they need to be deleted off the screen later
        self.pizzalabellist = []
        self.toppingslabellist = []

        # Create variable for modular row creation
        self.custRow = IntVar()
        self.custRow = 4

        # Heading for order receipt
        self.orderlabel = self.addLabel(text="Your Order:", row=self.custRow, column=0)
        self.custRow += 1

        # Loops through the items in the list created earlier
        for pizza, toppings in self.orderlist:
            # Creates pizza label and adds to list
            self.pizzalabellist.append(self.addLabel(text=pizza, row=self.custRow, column=0))
            self.custRow += 1
            # Increment the pizza counter for cost calculation
            self.pizzanum += 1
            for topping in toppings:
                # Create customization/toppings label and adds to list
                self.toppingslabellist.append(self.addLabel(text="\t-" + topping, row=self.custRow, column=0))
                self.custRow += 1
                # Increment the customization/toppings counter for cost calculation
                self.toppingsnum += 1
        


        # Calculates and creates cost based on pickup scenario for food ordered
        if self.dORpkey[0] == "Pickup":
            self.totalcost = (self.pizzanum * self.costperpizza + self.toppingsnum * self.costpertopping)  +  (self.pizzanum * self.costperpizza + self.toppingsnum * self.costpertopping) * self.salesTax
            self.subtotallabel = self.addLabel(text="Subtotal: $" + str(self.pizzanum * self.costperpizza + self.toppingsnum * self.costpertopping), row=self.custRow, column=1)
            self.custRow += 1
            self.taxlabel = self.addLabel(text="Tax: $" + str((self.pizzanum * self.costperpizza + self.toppingsnum * self.costpertopping) * self.salesTax), row=self.custRow, column=1)
            self.custRow += 1
            self.totalcostlabel = self.addLabel(text="Total cost: $" + str(self.totalcost), row=self.custRow, column=1)
            self.custRow += 1

        # Calculates and creates cost based on delivery scenario for food ordered
        if self.dORpkey[0] == "Delivery":
            self.foodcostlabel = self.addLabel(text="Food Cost: $" + str(self.pizzanum * self.costperpizza + self.toppingsnum * self.costpertopping), row=self.custRow, column=1)
            self.custRow += 1
            self.deliveryfeelabel = self.addLabel(text="Delivery Fee: $" + str(self.deliveryFee), row=self.custRow, column=1)
            self.custRow += 1
            self.taxlabel = self.addLabel(text="Tax: $" + str((self.pizzanum * self.costperpizza + self.toppingsnum * self.costpertopping + self.deliveryFee) * self.salesTax), row=self.custRow, column=1)
            self.custRow += 1
            self.totalcost = (self.pizzanum * self.costperpizza + self.toppingsnum * self.costpertopping + self.deliveryFee)  +  (self.pizzanum * self.costperpizza + self.toppingsnum * self.costpertopping + self.deliveryFee) * self.salesTax
            self.totalcostlabel = self.addLabel(text="Total cost: $" + str(self.totalcost), row=self.custRow, column=1)
            self.custRow += 1
 

    def payatstore(self):
        """Method to display comfirmation of paying at the store selection"""
        self.prompt["text"] = "You have selected to pay at the store"

        # String variable for selection in orderReceived method
        self.payvalue = StringVar()
        self.payvalue.set("Pay at Store")

        # Change the value of the submit button and call the orderReceived method
        self.submit_btn = self.addButton(text="Submit Order", row=1, column=1, command=self.orderReceived)

        # Clear elements
        self.payatstore_btn.destroy()
        self.paycard_btn.destroy()
        self.choosepayment_lbl.destroy()


    def paycash(self):
        """Method to display comfirmation of paying in cash selection"""
        self.prompt["text"] = "You have selected to pay cash"

        # String variable for selection in orderReceived method
        self.payvalue = StringVar()
        self.payvalue.set("Pay Cash")

        # Change the value of the submit button and call the orderReceived method
        self.submit_btn = self.addButton(text="Submit Order", row=1, column=1, command=self.orderReceived)

        # Clear elements
        self.paycash_btn.destroy()
        self.paycard_btn.destroy()
        self.choosepayment_lbl.destroy()
        

    def paycard(self):
        """Method to display comfirmation of paying with card selection and provide a form to enter card information"""
        
        # Clear screen
        if self.dORpkey[0] == "Pickup":
            self.payatstore_btn.destroy()
        if self.dORpkey[0] == "Delivery":
            self.paycash_btn.destroy()
        self.paycard_btn.destroy()
        self.choosepayment_lbl.destroy()

        # Update heading
        self.prompt["text"] = "Enter Payment Card Details Below"

        # String variable for selection in orderReceived method
        self.payvalue = StringVar()
        self.payvalue.set("Pay Card")

        # Disclaimer for peer review/instructor review testing
        self.disclaimer = self.addLabel(text="(For the purposes of this class obviously\ndo not enter real payment information)", row=1, column=0)

        # labels for entering card information
        self.cardname_lbl = self.addLabel(text="Cardholder Name: ", row=2, column=0)
        self.exp_lbl = self.addLabel(text="Expiration Date (**/**): ", row=3, column=0)
        self.csc_lbl = self.addLabel(text="Enter Security Code: ", row=4, column=0)
        
        # Textfields for entering card information
        self.cardname = self.addTextField(row=2, column=1, width=20, text="")
        self.exp = self.addTextField(row=3, column=1, width=20, text="")
        self.csc = self.addTextField(row=4, column=1, width=20, text="")

        # Change the value of the submit button and call the orderReceived method
        self.submit_btn = self.addButton(text="Submit Order", row=5, column=1, command=self.orderReceived)

    def orderReceived(self):
        """Method that notifies the user the the order has been recived, clears the screen, and notifies user they may close the window"""

        # Selection structure that clears the screen based on payment method chose and the elements created as a result
        if self.payvalue.get() == "Pay Card":
            self.disclaimer.destroy()
            self.cardname_lbl.destroy()
            self.exp_lbl.destroy()
            self.csc_lbl.destroy()
            self.cardname.destroy()
            self.exp.destroy()
            self.csc.destroy()
            self.submit_btn.destroy()

        if self.payvalue.get() == "Pay Cash" or self.payvalue.get() == "Pay at Store":
            self.submit_btn.destroy()

        # Updates prompt and adds new label
        self.prompt["text"] = "Order Received"
        self.addLabel(text="You may now close this window", row=1, column=0)


# Main method to display window
def main():
    payscreen = PaymentScreen(deliverymodeinfo, orders)
    payscreen.mainloop()
main()