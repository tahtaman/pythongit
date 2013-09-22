import sys

name_argument = sys.argv[1]
location_argument = sys.argv[2]

def i_here(name, location):
    print('My name is {0}. I am in {1}'.format(name, location))

i_here(name_argument, location_argument)
