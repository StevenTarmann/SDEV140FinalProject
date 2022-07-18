from breezypythongui import EasyFrame
from tkinter import *

"""
Author: Steven Tarmann
Date: 07/15/2022
Program to decide between delivery or pickup for PPPORderPlacer
"""

# Should create a "clear screen" function that will destroy all the items on screen instead of typing .destoy() for all items

"""
INPUT
    User clicks a radio button that asks the user if they are using delivery or pickup
    Prompts for user address if delivery - asks for zipcode if pickup to find nearest store

OUTPUT
    pickup or delivery option will be saved
        if delivery the address will be saved
        if pickup the zipcode will only be saved
        in both situations the zipcode will be used to select a store number (this can be generated generically for the purposes of this project or an API call can be used somehow)

PROCESSING
    Display a window with radio buttons, a title, a label with instructions, and a submit button
    clears the grid once submit is clicked and either a delivery or a pickup screen shows up
        delivery screen: has address boxes, a label with insturctions, and a submit button, also has a back button
        pickup screen: has a zipcode box, a label with instruction, and a submit button, also has a back button
    displays your closest store at the bottom on both options, and if on delivery it displays that your address has been saved for delivery
"""

class PickupOrDelivery(EasyFrame):
    """Window that guides a user through selecting pickup or delivery"""
    def __init__(self):
        """Creates window and adds Labels, radio buttons, and submit buttons"""
        EasyFrame.__init__(self)

        self.prompt = self.addLabel(text="Pickup or Delivery?", row=0, column=0,  sticky="NSEW")

        self.deliveryModeGroup = self.addRadiobuttonGroup(row=1, column=0, rowspan=2)
        defaultRB = self.deliveryModeGroup.addRadiobutton(text="Pickup")
        self.deliveryModeGroup.addRadiobutton(text="Delivery")

        self.deliveryModeGroup.setSelectedButton(defaultRB)

        self.submit_btn = self.addButton(text="Submit", row=3, column=0, command=self.submitmode)
    

    def submitmode(self):
        """Prompts the user for pickup or delivery information based on radio button input
        SHOULD HAVE THE IF STATEMENTS EXECUTE FUNCTIONS INSTEAD OF HARD CODING INSIDE THE STATEMENTS"""

        # Clear the screen and add information and a textfield for adding zipcode information to locate closest store
        if self.deliveryModeGroup.getSelectedButton()["text"] == "Pickup":
            self.mode = "Pickup"
            self.prompt["text"] = "Enter pickup information"
            self.deliveryModeGroup.destroy()
            self.submit_btn.destroy()
            self.submit_btn = self.addButton(text="Submit", row=4, column=1, command=self.store)
            self.back_btn = self.addButton(text="<< Back", row=4, column=0, command=self.back)
            self.zipcode_label = self.addLabel(text="Zipcode:", row=3, column=0)
            self.zipcode = self.addTextField(row=3, column=1, width=20, text="")

        # Clear the screen and add information and a textfield for adding address information to locate closest store
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

        # Clears the screen, saves zipcode, and displays message to user
        if self.mode == "Pickup":
            self.prompt["text"] = "Your Pickup information has been saved\nYour order will be sent to:"
            self.zip = self.zipcode.getText()
            self.ziplabel = self.addLabel(text="The store closest to zipcode " + self.zip, row=4, column=0)
            self.zipcode.destroy()
            
            self.zipcode_label.destroy()
            self.submit_btn.destroy()
            self.back_btn.destroy()

        # Clears the screen, saves address values, and displays message to user
        elif self.mode == "Delivery":
            self.prompt["text"] = "Your Delivery information has been saved\nYour order will be sent to:"
   
            self.f_name_value = self.f_name.getText()
            self.l_name_value = self.l_name.getText()
            self.address_value = self.address.getText()
            self.city_value = self.city.getText()
            self.state_value = self.state.getText()
            self.zipcode_value = self.zipcode.getText()

            self.ziplabel = self.addLabel(text="The store closest to zipcode " + self.zipcode_value, row=4, column=0)

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



def main():
    root = PickupOrDelivery()
    root.mainloop()

main()