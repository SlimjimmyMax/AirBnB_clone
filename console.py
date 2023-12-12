#!/usr/bin/python3
"""
Entry point of the command interpreter
"""
import cmd
import json
import shlex

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command processor
    """
    prompt = "(hbnb) "
    l_classes = ['BaseModel', 'User', 'Amenity', 'Place', 'City', 'State', 'Review']
    l_c = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, arg):
        """
        Parses command input
        """
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cnd = cls[1].split('(')
            args = cnd[1].split(')')
            if cls[0] in HBNBCommand.l_classes and cnd[0] in HBNBCommand.l_c:
                arg = f"{cnd[0]} {cls[0]} {args[0]}"
        return arg

    def help_help(self):
        """
        Prints help command description
        """
        print("Provides description of a given command")

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass

    def do_count(self, cls_name):
        """
        Counts the number of instances of a class
        """
        count = sum(1 for obj in storage.all().values() if obj.__class__.__name__ == cls_name)
        print(count)

    def do_create(self, type_model):
        """
        Creates an instance according to a given class
        """
        if not type_model:
            print("** class name missing **")
        elif type_model not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        else:
            class_dict = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                          'City': City, 'Amenity': Amenity, 'State': State, 'Review': Review}
            my_model = class_dict[type_model]()
            print(my_model.id)
            my_model.save()

    def do_show(self, arg):
        """
        Shows string representation of an instance passed
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_id = args[1].strip('"')
            obj = storage.get_object_by_id(args[0], obj_id)
            if obj:
                print(obj)
                return
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance passed
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_id = args[1].strip('"')
            obj = storage.get_object_by_id(args[0], obj_id)
            if obj:
                storage.delete_object(obj)
                storage.save()
                return
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints string representation of all instances of a given class
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        else:
            instances = [str(obj) for obj in storage.all().values() if obj.__class__.__name__ == args[0]]
            print(instances)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_id = args[1].strip('"')
            obj = storage.get_object_by_id(args[0], obj_id)
            if obj:
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(obj, args[2], args[3])
                    storage.save()
                return
            print("** no instance found **")

    def do_quit(self, line):
        """
        Quit command to exit the command interpreter
        """
        return True

    def do_EOF(self, line):
        """
        EOF command to exit the command interpreter
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
