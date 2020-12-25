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

INPUT_FILE='1-input.txt'
#INPUT_FILE='1a-example.txt'

input = [int(line) for line in get_file_contents(INPUT_FILE)[0]]

def calc_fuel(mass: int) -> int:
    return int(mass / 3) - 2

def calc_fuel_inc_fuel(mass: int) -> int:
    """
    Calculate the fuel required taking account the fuel for the fuel mass

    :param mass:
    :return:
    """
    res = []
    res.append(calc_fuel(mass))
    # Init to 1 to run while loop at least once
    fuel_for_fuel = calc_fuel(res[-1])
    while fuel_for_fuel > 0:
        res.append(fuel_for_fuel)
        fuel_for_fuel = calc_fuel(res[-1])

    return sum(res)

#print(list(map(calc_fuel, input)))
start_a = time()
print('part a - total fuel:', sum(map(calc_fuel, input)))
print('part a timing:', time() - start_a)

start_b = time()
print('part b - total fuel:', sum(map(calc_fuel_inc_fuel, input)))
print('part a timing:', time() - start_b)
