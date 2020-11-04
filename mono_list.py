#!/usr/bin/python3
# Monopole solver
# by Merlin Carson

import sys
import time
import numpy as np


def parse_args(args):

    if len(args) < 3 or int(sys.argv[1]) > 52:
        sys.exit("Usage: ./mono.py <num monopoles (<=52)> <num rooms>")

    return int(sys.argv[1]), int(sys.argv[2])

def is_additive(x, y, z):

    if (x + y == z):
        return True

    return False

def place_mono(cur_monos, new_mono):

    # base case, not enough monopoles in room to be additive
    if len(cur_monos) < 2:
        return True

    for i, x in enumerate(cur_monos[:-1]):
        for y in cur_monos[i+1:]:
            if is_additive(x, y, new_mono) is True:
                return False
    return True

def solver(monos, rooms):

    # lists of all possible monopoles and rooms
    monos = list(range(1,monos+1)) 
    rooms = [str(i) for i in range(1, rooms+1)]

    # data struct for final solution set
    solution = {i: [] for i in rooms}

    return solve(monos, rooms, solution)

def solve(monos, rooms, solution):

    # base case
    if len(monos) == 0:
        return solution

    mono = monos.pop(0)

    # place monopole
    for room in rooms:
        if place_mono(solution[room], mono) is True:
            solution[room].append(mono)
            solution = solve(monos, rooms, solution)
            return solution

    monos.insert(0, mono)
    solution = solve(monos, rooms, solution)
    
def show_results(solution):

    if solution is False:
        print('unsat')
    else:
        for key in solution.keys():
            solution[key] = sorted(solution[key])
            for value in solution[key]:
                print(value, end=' ')
            print()

def main():
    start = time.time()

    #monos, rooms = parse_args(sys.argv)
    monos, rooms = 8, 2
    #monos, rooms = 23, 3
    #monos, rooms = 24, 3
    print(f'Solving for {monos} monopoles in {rooms} rooms')

    solution = solver(monos, rooms)

    show_results(solution)

    print(f'Script completed in {time.time()-start:.8f} secs')

    return 0

if __name__ == '__main__':
    sys.exit(main())
