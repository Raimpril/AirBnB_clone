#!/usr/bin/python3
"""
Here we are creating a console application for the AIRbnb project
"""
import cmd
class HBNBCommand(cmd.Cmd):
    """
    command class interprete
    """
<<<<<<< HEAD
    prompt = '(hbnb)'
    def do_quit(self, line):
=======
     prompt = '(hbnb) '
    def quit(self, line):
>>>>>>> c40c10f61eb5bbca8f5ac583f2da496cb714286c
        """The function or method used to quit the console"""
        quit()

    def EOF(self, line):
        """The function we will used to handle end of line"""
        print()
        exit()
