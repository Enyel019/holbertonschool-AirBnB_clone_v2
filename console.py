#!/usr/bin/python3
"""The entry point of the command interpreter."""


import json
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


CLASSES = {
    'BaseModel',
    'User',
    'State',
    'City',
    'Amenity',
    'Place',
    'Review',
}


class HBNBCommand(cmd.Cmd):
    """It's a command line interpreter
        that inherits from the cmd module."""

    prompt = '(hbnb)'

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing."""
        pass

    def do_EOF(self, line):
        """Print the string "EOF" and then exits the program."""
        print("EOF")
        return True

    def do_create(self, line):
        """Create a new instance of BaseModel."""
        if len(line) == 0:
            print("** class name missing **")
        else:
            if line not in CLASSES:
                print("** class doesn't exist **")
            else:
                str = line + "()"
                base_inst = eval(str)
                base_inst.save()
                print(base_inst.id)

    def do_show(self, line):
        """Print the value of the variable named."""
        arg = line.split()
        obj_dict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg[0], arg[1])])

    def do_destroy(self, line):
        """Destroys the current room and all items in it."""
        args = line.split()
        obj_dict = storage.all()

        if not line:
            print("** class name missing **")
            return
        elif not args[0] or args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        instance_key = "{}.{}".format(args[0], args[1])
        if instance_key not in obj_dict:
            print("** no instance found **")
            return
        else:
            del obj_dict[instance_key]
            storage.save()

    def do_all(self, line):
        """Print all instances of a class."""
        arg = line.split()
        obj_dict = storage.all()
        res = []

        if not arg:
            res = [str(obj_dict[obj]) for obj in obj_dict.keys()]
        elif arg[0] not in CLASSES:
            print("** class doesn't exist **")
        else:
            res = [str(obj_dict[obj]) for obj in obj_dict
                   if obj.startswith(arg[0])]
        print(res)

    def do_update(self, line):
        """Update an instance by adding/updating a key-value pair."""
        args = line.split()
        obj_dict = storage.all()

        if not line:
            print("** class name missing **")
            return
        elif not args[0] or args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        instance_key = "{}.{}".format(args[0], args[1])
        if instance_key not in obj_dict:
            print("** no instance found **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        else:
            setattr(obj_dict[instance_key], args[2], args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
