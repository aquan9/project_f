#A recipe object definition. Using trees
#Author: Andres Quan
#Date: 21 July 2017

import step
import time

class Recipe:
    """A new class to hold a recipe to be built by the chef"""
    def __init__(self):
        self.name = input("What is the title of this Recipe? ")
        self.author = input("Who is the author? ")
        self.description = input("Please give a description: ")
        self.cooktime = input("Approximate cook time? ")
        self.ingredients = {}
        self.date = time.strftime("%d/%m/%y")
        while True:
            more = input("Do you have an ingredient to add?")
            more = more.lower()
            if more == "yes":
                ingredient = input("What is the name of the ingredient? ")
                quantity = input("How much " + ingredient + " do you use?")
                self.ingredients[ingredient] = quantity
            elif more == "no":
                break
            else:
                print("I did not understand please say (yes/no)")

        self.steps = step.Step()


    def genDict(self):
        """Convert the recipe to a dictionary"""
        outDict = {}
        outDict["name"] = self.name
        outDict["author"] = self.author
        outDict["descript"] = self.description
        outDict["cooktime"] = self.cooktime
        outDict["ingredients"] = self.ingredients
        outDict["steps"] = self.steps.genDict()
        outDict["date"] = self.date
        return outDict


def main():
    x = Recipe()
    print(x.genDict())

if __name__ == "__main__":
    main()



