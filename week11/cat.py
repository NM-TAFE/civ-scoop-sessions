class Cat():
    SPECIES_SCIENTIFIC_NAME='Felis domesticus' # class attributes
    NUMBER_OF_LIVES = 9

    # constructor or initialiser
    def __init__(self, name, coat):
        self.__name = name # object attributes
        self.__coat = coat

    @classmethod
    def hivemind_meow(cls):
        print("The very concept of cats themselves meow")

    def describe(self):
        print(f"{self.__name} is a {Cat.SPECIES_SCIENTIFIC_NAME} who all have {Cat.NUMBER_OF_LIVES} lives")

    def get_name(self):
        return self.__name

    def set_name(self):
        print("How dare you!")

    def meow(self):
        print(f"{self.name} meows loudly")


# initialising objects:
loofy = Cat(name="Loofy", coat="grey")
rufous = Cat(name="Rufous", coat="ginger")

loofy.describe()
Cat.hivemind_meow()
