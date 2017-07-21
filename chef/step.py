#A Step object that can be used to make a tree of steps
#Author: Andres Quan
#Date: 21 July 2017
import json

class Step():
    def __init__(self):
        """Constructor for new step"""
        self.instruction = input("What is the instruction?")
        self.children = []
        more = True
        while more:
            still_more = input("Does " + self.instruction +" depend on anything else?")
            still_more = still_more.lower()

            if still_more == "yes":
                self.children.append(Step())
            elif still_more == "no":
                more = False
            else:
                print("Unknown response please write (yes/no)")
                continue

    def postOrderTrav(self):
        """Traverse the step tree in post order"""
        for child in self.children:
            if child.children:
                child.postOrderTrav()
            else:
                pass
                #This might be a place where different work paths can be broken down
                #print("---Path---")
            print(child.instruction)

#Testing for the step class
def main():
    chicken_soup_steps = Step()
    chicken_soup_steps.postOrderTrav()

if __name__ == "__main__":
    main()
