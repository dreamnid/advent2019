#!/usr/bin/env python3
from collections import defaultdict
from functools import partial, reduce
from itertools import chain, cycle, takewhile
import math
from operator import mul
import os
import pprint
import re
from time import time
from typing import Dict, List, Set, Tuple, Union

from humanize import intcomma

# Fix path so we can do a relative import: https://stackoverflow.com/a/27876800
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

        # Relative imports here
        from util import *

INPUT_FILE='2-input.txt'
#INPUT_FILE='2a-example.txt'

input = [int(el) for el in get_file_contents(INPUT_FILE)[0][0].split(',')]
#print(input)

def run(input):
    prog_counter = 0
    while True:
        opcode = input[prog_counter]

        if opcode == 99 or prog_counter >= len(input):
            break
        elif opcode == 1:
            # add
            input[input[prog_counter+3]] = input[input[prog_counter+1]] + input[input[prog_counter+2]]
        elif opcode == 2:
            # mult
            input[input[prog_counter+3]] = input[input[prog_counter+1]] * input[input[prog_counter+2]]
        else:
            assert False, 'Bad opcode'

        prog_counter += 4
    return input

start_a = time()
input_a = input.copy()
input_a[1] = 12
input_a[2] = 2
print('part a:', run(input_a)[0])
print('part a timing:', time() - start_a)
print()

start_b = time()
found = False
for i in range(100):
    for j in range(100):
        input_attempt = input.copy()
        input_attempt[1] = i
        input_attempt[2] = j

        try:
            res = run(input_attempt)
            if res[0] == 19690720:
                found = True
                break
        except IndexError:
            continue
    if found:
        break

if found:
    print('part b:', input_attempt[1], input_attempt[2], 100 * input_attempt[1] + input_attempt[2])
    print('part b timing:', time() - start_b)
else:
    print('Ruh-roo, no answer found')
