"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.

Hint
Use __init__ method to construct some parameters
"""

class ex3:

    def __init__(self):
        self.mess = "Mensaje"

    def getString(self):
        self.mess = input("Type something: ")
        return print(self.mess)

    def printString(self):
        print(self.mess.upper())

level1_ex3 = ex3()
level1_ex3.getString()
level1_ex3.printString()