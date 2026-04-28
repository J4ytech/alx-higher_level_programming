#!/usr/bin/python3

if __name__=="__main__":
    from sys import argv

    arguments = len(argv) - 1

    if arguments == 0:
        print("0 arguments.")
    elif arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arguments))
    
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))