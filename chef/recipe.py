#A recipe object definition. Using trees
#Author: Andres Quan
#Date: 21 July 2017

import step
import time

class Recipe:
    """A new class to hold a recipe to be built by the chef"""
    def __init__(self):
        this.name = input("What is the title of this Recipe? ")
        this.author = input("Who is the author? ")
        
        this.ingredients = {}
        while True:
            more = input("Do you have an ingredient to add?")
            more = more.lower()
            if more == "yes":
                ingredient = input("What is the name of the ingredient? ")
                quantity = input("How much " + ingredient + " do you use?")
                this.ingredients[ingredient] = quantity
            elif more == "no":
                break
            else:
                print("I did not understand please say (yes/no)"



        this.steps = Step()
        this.date = time.strftime("%d/%m/%y")

