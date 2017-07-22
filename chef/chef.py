#This is a script to create new recipes
#Author: Andres Quan
#Date: 21 July 2017

import Recipe
import json

def main():
    while True:
        more = "Would you like to create a new recipe? "
        if more == "yes":
            out = Recipe()
        elif more == "no":
            print("Have a nice day!")
            return
        else:
            print("I didn't quite understand that. Please say (yes/no)")



if __name__ == "__main__":
    main()
