#!/usr/bin/python3
for x in range(10):
    for z in range(x, 10):
        if x < z:
            print("{:d}{:d}".format(x, z),
                    end="\n" if x == 8 and z == 9 else ", ")
