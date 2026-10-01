#!/usr/bin/python3
"""Console module for AirBnB clone"""

import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance"""

        if not arg:
            print("** class name missing **")
            return

        if arg not in classes:
            print("** class doesn't exist **")
            return

        obj = classes[arg]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Show an instance"""

        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])

        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """Destroy an instance"""

        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])

        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Print all instances"""

        objects = []

        if arg:
            if arg not in classes:
                print("** class doesn't exist **")
                return

            for key, obj in storage.all().items():
                if key.startswith(arg + "."):
                    objects.append(str(obj))
        else:
            for obj in storage.all().values():
                objects.append(str(obj))

        print(objects)

    def do_update(self, arg):
        """Update an instance"""

        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])

        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        obj = storage.all()[key]

        attr_name = args[2]
        attr_value = args[3].strip('"')

        setattr(obj, attr_name, attr_value)
        obj.save()

    def default(self, line):
        """Handle <class name>.<method name>() syntax"""
        match = re.match(r'^(\w+)\.(\w+)\((.*)\)$', line)
        
        if not match:
            print(f"*** Unknown syntax: {line}")
            return
        
        class_name = match.group(1)
        method_name = match.group(2)
        args = match.group(3)
        
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        
        if method_name == "all":
            self.do_all(class_name)
        
        elif method_name == "count":
            count = 0
            for key in storage.all().keys():
                if key.startswith(class_name + "."):
                    count += 1
            print(count)
        
        elif method_name == "show":
            obj_id = args.strip('"\'')
            self.do_show(f"{class_name} {obj_id}")
        
        elif method_name == "destroy":
            obj_id = args.strip('"\'')
            self.do_destroy(f"{class_name} {obj_id}")
        
        elif method_name == "update":
            self.do_update(f"{class_name} {args}")
        
        else:
            print(f"*** Unknown syntax: {line}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()