"""Для объявления статического метода, вам нужно указать дескриптор @staticmethod перед названием метода, как показано ниже:"""

class Car:

    @staticmethod
    def get_class_details():
        print ("Это класс Car")

Car.get_class_details()