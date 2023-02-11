#!/usr/bin/python3
"""
Here we are creating a console application for the AIRbnb project
"""
import cmd
class HBNBCommand(cmd.Cmd):
    """
    command class interprete
    """
    prompt = '(hbnb)'
    def do_quit(self, line):
        """The function or method used to quit the console"""
        quit()

    def do_EOF(self, line):
        """The function we will used to handle end of line"""
        print()
        exit()
