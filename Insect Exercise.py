# Clas exercise for insect class
import random


class insect:
    def __init__(self):
        self.__wings = 2
        self.__legs = 4

    def flight(self):
        self.__distance = random.randint(1, 10)
        return self.__distance

    def wings(self):
        return self.__wings

    def legs(self):
        return self.__legs


def main():
    again = "y"
    while again == "y":
        again = input("Would you like to create an insect? (y/n) \n")
        if again == "y":
            my_insect = insect()
            print(
                "The insect has "
                + str(my_insect.wings())
                + " wings and "
                + str(my_insect.legs())
                + " legs."
            )
            print("The insect can fly " + str(my_insect.flight()) + " miles.")
        else:
            print("Ok, thank you!")


main()
