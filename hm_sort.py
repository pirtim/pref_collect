#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Acquires user's preferences by simple bisect search using human binary input.
'''

__version__ = "0.6"

__author__ = "Przemysław Kowalczyk <kontakt@pkowalczyk.pl>"
__license__ = "MIT"

from humanfriendly.prompts import prompt_for_confirmation, prompt_for_input

def insort_left(a, x, key=None, lo=0, hi=None):
    'Edited insort_left from: https://docs.python.org/3.5/library/bisect.html'
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    if key is None:
        key = lambda x,y: x<y
    while lo < hi:
        mid = (lo+hi)//2
        if key(a[mid],x): lo = mid+1
        else: hi = mid 
    a.insert(lo, x)
    return lo

def get_pref(line, result):
    key = lambda x,y: prompt_for_confirmation("Is '{}' better then '{}'?".format(y, x), padding=False)
    insort_left(result, line, key)  

if __name__ == "__main__":
    path_load = None
    path_save = None
    
    path_load = 'filmy3.txt' #DELETE
    path_save = 'filmy3save.txt' #DELETE

    if path_load == None:
        path_load = prompt_for_input("Insert load file path: ")

    if path_save == None:
        path_save = prompt_for_input("Insert save file path: ")

    with open(path_load) as f:
        lines = [line.rstrip() for line in  f.readlines()]

    result = []
    result.append(lines[0])

    for line in lines[1:]:
        get_pref(line, result)

    print (result)
    with open(path_save, 'w') as f:
        f.writelines([line+'\n' for line in  result])
