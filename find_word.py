"""
Module for search word in file. Takes the command line arguments.
First, file name. Second, required word.

python 3.x
"""

import sys

#file name and required word
file_name = sys.argv[1]
find_word = sys.argv[2]

def count_func(fl, word):
    global count
    count = 0
    find_file = open(fl)
    find_word = word
    index = 0
    for line in find_file.readlines():
        x = line
        if find_word in x:
            count += 1
        else: continue

def find(fl, word):
    find_file = open(fl)
    find_word = word
    index = 0
    for line in find_file.readlines():
        x = line
        index += 1
        if find_word in x:
            print('line', index, '-', 'have', find_word)
        else: continue

if __name__ == '__main__':
    count_func(file_name, find_word)
    print('In file {0} contains {1} words "{2}"'.format(file_name, count, find_word))
    find(file_name, find_word)
