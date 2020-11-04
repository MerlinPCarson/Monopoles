#!/usr/bin/python3
# Monopole sat solver CNF DIMEX decoder for Dr. Ecco challenege
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

def decode_dimex(num_monos, num_rooms, soln):
    if soln[0].strip() != 'SAT':
        sys.exit('UNSATISFIABLE')

    solution = {room: [] for room in np.arange(1, num_rooms + 1)}

    for atom in soln[1].split(' '):
        if atom.strip() == '0':
            break
        if atom[0] == '-':
            continue
        room = (int(atom)-1) // num_monos + 1
        monopole = (int(atom)-1) % num_monos + 1
        solution[room].append(monopole)

    return solution

def show_solution(solution):
    if solution is None:
        print('Invalid solution!!!')
    else:
        for key in solution.keys():
            for value in solution[key]:
                print(value, end=' ')
            print()

# verifies solution adhears to constraints
def verify_solution(solution, num_monos):

    # check to make sure all monopoles have been placed in rooms
    if not verify_all_monos(solution, num_monos):
        return None

    # check to make sure there are no duplcates of monopoles
    if not verify_no_duplicates(solution, num_monos):
        return None

    for key in solution.keys():
        # if there are less than 3 monopoles in a room, don't need to check if there is an additive combo
        if len(solution[key]) < 3:
            continue

        # check all combinations for additive combo
        for i, x in enumerate(solution[key][:-2]):
            for y in solution[key][i+1:-1]:
                for z in solution[key][i+2:]:
                    if is_additive(x, y, z) is True:
                        return None

    return solution

# verifies solution contains all monopoles 
def verify_all_monos(solution, num_monos):
    
    for mono in range(1, num_monos+1):
        for i, (_, values) in enumerate(solution.items(), start=1):
            if mono in values:
                break 
            if i == len(solution.keys()):
                return False

    return True

# verify there are no duplicate monopoles
def verify_no_duplicates(solution, num_monos):

    for mono in range(1, num_monos+1):
        mono_cnt = 0
        for _, value in solution.items():
            if value == mono:
                mono_cnt += 1
                if mono_cnt > 1:
                    return False    # duplicate monopole found
    # no duplicates found 
    return True



# Monopole constraining X + Y = Z
def is_additive(x, y, z):

    if (x + y == z):
        return True

    return False

def main():

    # verify and load correct number of command line arguments
    num_monos, num_rooms, soln = parse_args(sys.argv)
    #num_monos, num_rooms = 8, 2

    solution = decode_dimex(num_monos, num_rooms, soln)

    # verify solution follows constraints
    solution = verify_solution(solution, num_monos)

    # print solution
    show_solution(solution)

    return 0

if __name__ == '__main__':
    sys.exit(main())