#!/usr/bin/python3
"""
Console module for the command interpreter.
"""

import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]

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

    def do_create(self, arg):
        """
        Create new instance of BaseModel, save it, and print the id.
        """
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Print string representation of instance based on class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id
        objects = models.storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete instance based on class name and id. save change into JSON file
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id
        objects = models.storage.all()
        if key in objects:
            objects.pop(key)
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Print all string representations of instances based on class name.
        """
        objects = models.storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
            return

        class_name = arg.split()[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        print([str(obj) for obj in objects.values() if obj.__class__.__name__ == class_name])

    def do_update(self, arg):
        """
        Update instance based on class name and id by updating an attribute
        (save the change into the JSON file).
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id
        objects = models.storage.all()
        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attr_value = args[3].strip('"')
        instance = objects[key]
        setattr(instance, attr_name, attr_value)
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
