class Dog:
    def __init__(self, name: str, breed: str) -> None:
        self.name = name
        self.breed = breed
    
    def bark(self):
        print("{name} barks!".format(name=self.name))
    
    def eat(self):
        print("{name} eats".format(name=self.name))
    
    def show_details(self):
        print("Name: {name}\nBreed: {breed}".format(name=self.name,breed=self.breed))


# create instance of a dog!
bark_twain = Dog("Bark Twain","Poodle")
toto = Dog("Toto", "Cairn Terrier")
lassie = Dog("Lassie", "Rough Collie")


bark_twain.bark()
toto.eat()
lassie.show_details()