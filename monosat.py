#!/usr/bin/python3
# Monopole sat solver CNF DIMEX encoder for Dr. Ecco challenege
# by Merlin Carson

import sys
import time
import numpy as np


# verifies and returns correct number of comman line arguments
def parse_args(args):

    if len(args) < 3:
        sys.exit("Usage: ./monosat.py <num monopoles> <num rooms>")

    return int(sys.argv[1]), int(sys.argv[2])

# create CNF variable atom
def L(num_monos, mono_num, room_num):
    return num_monos * room_num + mono_num

# Monopole constraining X + Y = Z
def is_additive(x, y, z):
    if (x + y == z):
        return True
    return False

# each monopole is placed
def constraint1(num_monos, num_rooms, cnf):
    for m in range(1, num_monos+1):
        clause = ''
        for n in range(num_rooms):
            clause += f'{L(num_monos, m, n)} '
        clause += '0'
        cnf.append(clause)

# no monopoles in 2 places
def constraint2(num_monos, num_rooms, cnf):
    for m in range(1, num_monos+1):
        clause = ''
        for n in range(num_rooms):
            clause += f'{L(num_monos, m, n)} '
        clause += '0'
        cnf.append(clause)

# sums exclude monopoles
def constraint3(num_monos, num_rooms, cnf):
    monos = np.arange(1, num_monos+1)
    for n in range(num_rooms):
        for i, x in enumerate(monos[:-2]):
            for y in monos[i+1:-1]:
                for z in monos[i+2:]:
                    if is_additive(x, y, z) is True:
                        cnf.append(f'-{L(num_monos, x, n)} -{L(num_monos, y, n)} -{L(num_monos, z, n)} 0')

def generate_cnf_dimax(num_monos, num_rooms):

    cnf = []

    # all monopoles are placed
    constraint1(num_monos, num_rooms, cnf)

    # no monopoles in 2 places
    constraint2(num_monos, num_rooms, cnf)

    # sums exclude monopoles
    constraint3(num_monos, num_rooms, cnf)

    return cnf

# prints final CNF in DIMAX format
def print_cnf(num_vars, cnf):

    print(f'p cnf {num_vars} {len(cnf)}')
    for clause in cnf:
        print(clause)

def main():

    # verify and load correct number of command line arguments
    num_monos, num_rooms = parse_args(sys.argv)

    # number of variables in CNF
    num_vars = num_monos * num_rooms

    # encode monopole problem as CNF en DIMAX format
    cnf = generate_cnf_dimax(num_monos, num_rooms)

    # display the CNF in DIMAX format
    print_cnf(num_vars, cnf)

    return 0

if __name__ == '__main__':
    sys.exit(main())