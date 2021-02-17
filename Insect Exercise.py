# Clas exercise for insect class
import random


class insect:
    def __init__(self, w, l, f):
        self.__wings = w
        self.__legs = l
        self.__flight = f

    def flight(self):
        self.__flight = random.randint(1, 10)
        return self.__flight

    def wings(self):
        return self.__wings

    def legs(self):
        return self.__legs


def main():
    again = "y"
    while again == "y":
        again = input("Would you like to create an insect? (y/n) \n")
        if again == "y":
            my_insect = insect(0, 0, 0)
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
