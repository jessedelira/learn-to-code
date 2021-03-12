

# Declaring Type of Variables

# int type variable
int_var = 10

# float type variable
float_var = 10.1

# string type variable, using double quotes
double_quote_string_var = "this is a string"

# string type variable, using single quotes
single_quote_string_var = 'this is a string'

# bool type variable
isApteraAcademyCool = True

# list type variable
grocery_list = ["Bag of peaches","Loaf of Bread","Bottle of water"]

# dict type variable
# contains a key then value for every index
grocery_dict = {"Bag of Peaches":1,"Loaf of Bread": 3, "Bottle of water": 10}

len_grocery_dict = len(grocery_dict)
temp = 0

for a in grocery_dict:
    print("Get {key} and I need {value} of them".format(key=a,value=grocery_dict.get(a)))
    temp += 1
    # if temp value is the same number as the length of grocery_dict (3) then print a new line
    if(temp == len_grocery_dict):
        print("\n")

print("The keys to grocery_dict are", grocery_dict.keys(),"\n")
print("The values to grocery_dict are",grocery_dict.values(),"\n")


