# AirBnB Clone - The Console

## Project Description

The AirBnB Clone is a full-stack web application project that replicates the core functionality of the AirBnB platform. This first phase focuses on building a command interpreter to manage application objects such as `User`, `State`, `City`, `Place`, `Amenity`, and `Review`. Objects are stored in memory and serialized to a JSON file.

## Description of the Command Interpreter

The command interpreter is a Python-based console that mimics a Unix shell, allowing users to create, retrieve, update, and delete objects.

### How to Start It

Requirements: Python 3.8+ on a Unix-like OS.

    Clone the repository
    cd into AirBnB_clone
    type ./console.py

Non-interactive mode:

    echo "help" | ./console.py

### How to Use It

Once started, a `(hbnb) ` prompt appears.

| Command | Description |
|---------|-------------|
| `create <class>` | Creates a new instance and prints its `id`. |
| `show <class> <id>` | Prints the string representation of an instance. |
| `destroy <class> <id>` | Deletes an instance. |
| `all [class]` | Prints all instances, optionally filtered by class. |
| `update <class> <id> <attribute> <value>` | Updates an instance's attribute. |
| `quit` / `EOF` | Exits the console. |
| `help` | Displays help information. |

### Examples

    $ ./console.py
    (hbnb) create User
    7f9d3c1e-2b6a-4d9b-8c1a-1f2e3d4c5b6a
    (hbnb) show User 7f9d3c1e-2b6a-4d9b-8c1a-1f2e3d4c5b6a
    [User] (7f9d3c1e-2b6a-4d9b-8c1a-1f2e3d4c5b6a) {'id': '7f9d3c1e-2b6a-4d9b-8c1a-1f2e3d4c5b6a', ...}
    (hbnb) update User 7f9d3c1e-2b6a-4d9b-8c1a-1f2e3d4c5b6a first_name "Betty"
    (hbnb) all User
    (hbnb) destroy User 7f9d3c1e-2b6a-4d9b-8c1a-1f2e3d4c5b6a
    (hbnb) quit
    $

    $ echo "create Place" | ./console.py
    (hbnb) 5a8b7c6d-4e3f-2a1b-9c8d-7e6f5a4b3c2d
    $

