#This is a script to create new recipes
#Author: Andres Quan
#Date: 21 July 2017

import recipe
import json

def main():
    print("What's cookin' good lookin'?")
    while True:
        more = input("Would you like to create a new recipe? ")
        if more == "yes":
            outDict = recipe.Recipe().genDict()
            filename = "recipes/"+ outDict["name"].replace(" ", "-") + ".json"
            with open(filename, 'w') as outfile:
                json.dump(outDict, outfile, indent=4)
        elif more == "no":
            print("Have a nice day!")
            return
        else:
            print("I.. didn't quite understand that. Please say (yes/no)")



if __name__ == "__main__":
    main()
