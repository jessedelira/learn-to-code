class Dog:
    def __init__(self, name: str, breed: str) -> None:
        self.name = name
        self.breed = breed
        self.detailFormat = "\nName: {name}\nBreed: {breed}"
        self.FrDetailFromat = "\nNom: {name}\nRace: {breed}"
    
    def bark(self):
        print("{name} barks!".format(name=self.name))
    
    def eat(self):
        print("{name} eats".format(name=self.name))
    
    def show_details(self):
        print(self.detailFormat.format(name=self.name,breed=self.breed))

    def show_detail_two(self):
        print("\nName:", self.name, "\nBreed: ", self.breed)
    
    def drool(self, adverb=None):
        if(adverb == None):
            print("{name} drools".format(name=self.name))
        else:
            print("{name} drools {adverb}".format(name=self.name,adverb=adverb))
        


# create instance of a dog!
breed_name = "Poodle"

#                 0              1                  2 
name_list = ["Bark Twain","Kurt the great!","Bonnie the terrible"]
print(name_list[0], "is happy")


bark_twain = Dog(name_list[0],breed_name)
kurt = Dog(name_list[1], breed_name)
bonnie = Dog(name_list[2], breed_name)
toto = Dog("Toto", "Cairn Terrier")
lassie = Dog("Lassie", "Rough Collie")

kurt.drool()
lassie.drool("uncontrollably")


# bark_twain.bark()
# bark_twain.eat()

# toto.eat()

# lassie.show_details()