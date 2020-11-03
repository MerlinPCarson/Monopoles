#!/usr/bin/python3
# Monopole DFS solver for Dr. Ecco challenege
# by Merlin Carson

import sys
import time
import numpy as np


# verifies and returns correct number of comman line arguments
def parse_args(args):

    if len(args) < 3:
        sys.exit("Usage: ./mono.py <num monopoles (<=52)> <num rooms>")

    return int(sys.argv[1]), int(sys.argv[2])

def L(num_monos, mono_num, room_num):
    return num_monos * room_num + mono_num

# Monopole constraining X + Y = Z
def is_additive(x, y, z):

    if (x + y == z):
        return True

    return False

# each monopole is placed
def constraint1(num_monos, num_rooms):
    for m in range(1, num_monos+1):
        for n in range(num_rooms):
            print(f'{L(num_monos, m, n)}', end=' ')
        print(0)

# no monopoles in 2 places
def constraint2(num_monos, num_rooms):
    for m in range(1, num_monos+1):
        for n in range(num_rooms):
            print(f'-{L(num_monos, m, n)}', end=' ')
        print(0)

# sums exclude monopoles
def constraint3(num_monos, num_rooms):
    monos = np.arange(1, num_monos+1)

    for n in range(num_rooms):
        for i, x in enumerate(monos[:-2]):
            for y in monos[i+1:-1]:
                for z in monos[i+2:]:
                    if is_additive(x, y, z) is True:
                        print(f'-{L(num_monos, x, n)} -{L(num_monos, y, n)} -{L(num_monos, z, n)} 0')

def print_cnf_dimax(num_monos, num_rooms):

    # all monopoles are placed
    constraint1(num_monos, num_rooms)

    # no monopoles in 2 places
    constraint2(num_monos, num_rooms)

    # sums exclude monopoles
    constraint3(num_monos, num_rooms)

def main():

    # verify and load correct number of command line arguments
    #num_monos, num_rooms = parse_args(sys.argv)
    num_monos, num_rooms = 8, 2

    print_cnf_dimax(num_monos, num_rooms)

    return 0

if __name__ == '__main__':
    sys.exit(main())