#!/usr/bin/python3

def safe_print_division(a, b):
    div_result = None  # Start with None in case division fails
    
    try:
        div_result = a / b
    except ZeroDivisionError:
        # If b is 0, div_result remains None
        pass
    finally:
        # This block executes regardless of whether an error occurred
        print("Inside result: {}".format(div_result))
        
    return div_result
