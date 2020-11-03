#!/usr/bin/python3
# Monopole DFS solver for Dr. Ecco challenege
# by Merlin Carson

import sys
import time
import fileinput
import numpy as np


# verifies and returns correct number of comman line arguments
def parse_args(args):

    if len(args) < 3:
        sys.exit("Usage: ./mono.py <num monopoles (<=52)> <num rooms> <std input of .soln file>")

    return int(sys.argv[1]), int(sys.argv[2]), fileinput.input(sys.argv[3:]) 

def L(num_monos, mono_num, room_num):
    return num_monos * room_num + mono_num

def print_solution(num_monos, num_rooms, soln):
    if soln[0].strip() != 'SAT':
        sys.exit('UNSATISFIABLE')

    for atom in soln[1].split(' '):
        if atom.strip() == '0':
            break

        print(atom.strip())

def main():

    # verify and load correct number of command line arguments
    num_monos, num_rooms, soln = parse_args(sys.argv)
    #num_monos, num_rooms = 8, 2

    print_solution(num_monos, num_rooms, soln)

    return 0

if __name__ == '__main__':
    sys.exit(main())