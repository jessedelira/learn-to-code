# Import Statements
from Donut import *

class DonutShop:
    def __init__(self) -> None:
        pass
    

    def start_shop(self) -> None:
        is_in_shop = input("Hello, would you like to come into the donut shop (Yes or No)?\n")
        if(is_in_shop == "Yes"):
            donut_frosting_flavor = input("Welcome to the donut shop!\nWhat type of donut frosting flavor do you want?\nWe have chocolate, vanilla, strawberry, or anything else you like!\n")
            new_donut = Donut(donut_frosting_flavor)

            sprinkles = input("Do you want sprinkles on your donut(Yes or No)?")
            if(sprinkles == "Yes"):
                add_sprinkles(new_donut)
            

            print(new_donut.type, "coming right up!\n")

            print("Your total is: {total}\n".format(total=giveTotal(new_donut)))
        
        elif(is_in_shop == "No"):
            print("\nNo worries! See you next time!")
        
        else:
            print("\nDon't know what the heck you just said, leave immediatley!")
    
    
def add_sprinkles(donut) -> None:
        donut.has_sprinkles = True
        print("Sprinkles were added to your donut!")
    
# TODO: add x

# TODO: add y



def giveTotal(donut) -> float:
    total = 0.00

    # donut costs 3.00, regardless of flavor
    total += 3.00

    if(donut.has_sprinkles == True):
        total += 1.00
    
    return total
