"""
Author: Steven Tarmann
Date: 07/15/2022
Program to decide between delivery or pickup for PPPORderPlacer
"""

# Import modules
from breezypythongui import EasyFrame
from tkinter import *



class PickupOrDelivery(EasyFrame):
    """Window that guides a user through selecting pickup or delivery"""
    def __init__(self):
        """Creates window and adds Labels, radio buttons, and submit buttons"""
        EasyFrame.__init__(self)

        # Global dictionary to store pickup or delivery information so other .py files can use it once the window is closed
        global deliverymodeinfo
        deliverymodeinfo = {}
        
        # Heading prompt
        self.prompt = self.addLabel(text="Pickup or Delivery?", row=0, column=0,  sticky="NSEW")

        # Create radio buttons
        self.deliveryModeGroup = self.addRadiobuttonGroup(row=1, column=0, rowspan=2)
        defaultRB = self.deliveryModeGroup.addRadiobutton(text="Pickup")
        self.deliveryModeGroup.addRadiobutton(text="Delivery")

        self.deliveryModeGroup.setSelectedButton(defaultRB)

        # Submit button that calls the submitmode method
        self.submit_btn = self.addButton(text="Submit", row=3, column=0, command=self.submitmode)
    

    def submitmode(self):
        """Prompts the user for pickup or delivery information based on radio button input"""

        # Clear the screen and add information and a textfield for adding information to locate closest store
        if self.deliveryModeGroup.getSelectedButton()["text"] == "Pickup":
            self.mode = "Pickup"
            self.prompt["text"] = "Enter pickup information"
            self.deliveryModeGroup.destroy()
            self.submit_btn.destroy()
            self.submit_btn = self.addButton(text="Submit", row=4, column=1, command=self.store)
            self.back_btn = self.addButton(text="<< Back", row=4, column=0, command=self.back)

            self.zipcode_label = self.addLabel(text="Zipcode:", row=3, column=0)
            self.zipcode = self.addTextField(row=3, column=1, width=20, text="")
            self.f_name_label = self.addLabel(text="First Name", row=1, column=0)
            self.l_name_label = self.addLabel(text="Last Name", row=2, column=0)
            self.f_name = self.addTextField(row=1, column=1, width=20, text="")
            self.l_name = self.addTextField(row=2, column=1, width=20, text="")

            

        # Clear the screen and add information and a textfield for adding information to locate closest store
        elif self.deliveryModeGroup.getSelectedButton()["text"] == "Delivery":
            self.mode = "Delivery"
            self.prompt["text"] = "Enter delivery information"
            self.deliveryModeGroup.destroy()
            self.submit_btn.destroy()
            self.submit_btn = self.addButton(text="Submit", row=7, column=1, command=self.store)
            self.back_btn = self.addButton(text="<< Back", row=7, column=0, command=self.back)

            self.f_name_label = self.addLabel(text="First Name", row=1, column=0)
            self.l_name_label = self.addLabel(text="Last Name", row=2, column=0)
            self.address_label = self.addLabel(text="Address",  row=3, column=0)
            self.city_label = self.addLabel(text="City", row=4, column=0)
            self.state_label = self.addLabel(text="State", row=5, column=0)
            self.zipcode_label = self.addLabel(text="Zipcode", row=6, column=0)

            self.f_name = self.addTextField(row=1, column=1, width=20, text="")
            self.l_name = self.addTextField(row=2, column=1, width=20, text="")
            self.address = self.addTextField(row=3, column=1, width=20, text="")
            self.city = self.addTextField(row=4, column=1, width=20, text="")
            self.state = self.addTextField(row=5, column=1, width=20, text="")
            self.zipcode = self.addTextField(row=6, column=1, width=20, text="")

    def store(self):
        """Notifies the user that their info has been saved, informs them of their service location, and saves their information"""

        # Clears the screen, saves address info, and displays message to user
        if self.mode == "Pickup":

            # Creates a list of values to be added to the global dictionary
            self.pickuplist = []

            self.prompt["text"] = "Your Pickup information has been saved\nYour order will be sent to:"
            self.zip = self.zipcode.getText()
            self.fname = self.f_name.getText()
            self.lname = self.l_name.getText()

            # Appends the list of values with the address info
            self.pickuplist.append(self.zip)
            self.pickuplist.append(self.fname)
            self.pickuplist.append(self.lname)

            # Adds the list and delivery mode to the dictionary
            deliverymodeinfo.update({self.mode:self.pickuplist})
            
            # Displays store information and clears the screen
            self.ziplabel = self.addLabel(text="The store closest to zipcode " + self.zip, row=4, column=0)
            self.zipcode.destroy()
            self.f_name.destroy()
            self.l_name.destroy()
            
            self.zipcode_label.destroy()
            self.f_name_label.destroy()
            self.l_name_label.destroy()
            self.submit_btn.destroy()
            self.back_btn.destroy()


        # Clears the screen, saves address values, and displays message to user
        elif self.mode == "Delivery":

            # Creates a list of values to be added to the global dictionary
            self.deliverylist = []


            self.prompt["text"] = "Your Delivery information has been saved\nYour order will be sent to:"
   
            self.f_name_value = self.f_name.getText()
            self.l_name_value = self.l_name.getText()
            self.address_value = self.address.getText()
            self.city_value = self.city.getText()
            self.state_value = self.state.getText()
            self.zipcode_value = self.zipcode.getText()

            # Appends the list of values with the address info
            self.deliverylist.append(self.f_name_value)
            self.deliverylist.append(self.l_name_value)
            self.deliverylist.append(self.address_value)
            self.deliverylist.append(self.city_value)
            self.deliverylist.append(self.state_value)
            self.deliverylist.append(self.zipcode_value)

            # Updates the global dictionary with mode and delivery address info
            deliverymodeinfo.update({self.mode:self.deliverylist})

            # Displays store information
            self.ziplabel = self.addLabel(text="The store closest to zipcode " + self.zipcode_value, row=4, column=0)

            # Clear the screen
            self.f_name.destroy()
            self.f_name_label.destroy()
            self.l_name.destroy()
            self.l_name_label.destroy()
            self.address.destroy()
            self.address_label.destroy()
            self.city.destroy()
            self.city_label.destroy()
            self.state.destroy()
            self.state_label.destroy()
            self.zipcode.destroy()
            self.zipcode_label.destroy()
            self.submit_btn.destroy()
            self.back_btn.destroy()
            
    def back(self):
        """Clears the screen and starts over from the delivery mode prompt window"""
        self.destroy()
        self.__init__()


# Main method to create window
def main():
    root = PickupOrDelivery()
    root.mainloop()

main()