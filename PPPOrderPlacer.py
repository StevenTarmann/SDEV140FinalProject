"""
Author: Steven Tarmann
Date: 07/22/2022
Program that Allows a user to place an order for pizza
"""

# Import window classes
from DeliveryMode import *
from MenuOfferings import *
from Payment import *


# Simple main function that creates the three windows
def main():
    root = PickupOrDelivery()
    order = MenuChoices()
    payment = PaymentScreen(deliverymodeinfo, orders)

# Run main
main()