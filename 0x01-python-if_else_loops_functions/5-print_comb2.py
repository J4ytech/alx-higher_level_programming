#!/usr/bin/python3

for count in range(0, 100):
    if count < 99:
        print(f"{count:02d}, ", end="")
    
    else:
        print(f"{count:02d}")