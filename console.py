#!/usr/bin/python3
"""
Console module for HBNBCommand
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class definition for the command interpreter
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        return True

    def help_quit(self):
        """
        Quit command to exit the program
        """
        print("Quit command to exit the program")

if __name__ == '__main__':
    HBNBCommand().cmdloop()