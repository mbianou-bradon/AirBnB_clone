#!/usr/bin/python3
"""
Console module for the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program when End-of-File (EOF) is encountered.
        """
        return True

    def emptyline(self):
        """
        Called when an empty line is entered.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
