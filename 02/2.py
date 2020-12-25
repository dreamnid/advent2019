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
print(input)

def run(input):
    idx = 0
    while True:
        opcode = input[idx]

        if opcode == 99 or idx >= len(input):
            break
        elif opcode == 1:
            # add
            input[input[idx+3]] = input[input[idx+1]] + input[input[idx+2]]
        elif opcode == 2:
            # mult
            input[input[idx+3]] = input[input[idx+1]] * input[input[idx+2]]
        else:
            assert False, 'Bad opcode'

        idx += 4
    return input

input[1] = 12
input[2] = 2
print('part a:', run(input)[0])
