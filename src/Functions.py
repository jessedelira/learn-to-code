# We want to create a function that figures 
# out a how much a person pay for gas per week


#   name of function     parameters of function
def cost_of_gas_per_week(miles_driven: float, price_per_gallon: float, miles_per_gallon: float) -> float:
    total_cost = (miles_driven/miles_per_gallon)*price_per_gallon
    return total_cost

def greeting_message(name: str) -> None:
    print("Hi {one}, great to see you!".format(one=name))


print("The cost of week is: ", cost_of_gas_per_week(100,10.5,15))

greeting_message("everyone")
