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

def is_additive(a, b, c):

    monos = sorted([a,b,c])

    if (monos[0] + monos[1] == monos[2]):
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

def solve(monos, rooms):

    # lists of all possible monopoles and rooms
    monos = np.arange(1, monos+1) 
    rooms = np.array([str(i) for i in range(1, rooms+1)])

    # data struct for final solution set
    solution = {i: [] for i in rooms}

    room_order = np.array(rooms)
    for room_start in rooms:
        for room in room_order:
            remove_list = []
            for idx, mono in enumerate(monos):
                if place_mono(solution[room], mono) is True:
                    solution[room].append(mono)
                    remove_list.append(idx)
            # removed the placed monopoles from the list of available monopoles
            monos = np.delete(monos, remove_list)   

        if len(monos) > 0:
            monos = np.append(monos, solution[room_start])
            monos.sort()
            solution[room_start] = []
            room_order = np.delete(room_order, 0)
            room_order = np.append(room_order, room_start)
        else:
            return solution

    return False 

def solve2(monos, rooms):

    # lists of all possible monopoles and rooms
    monos = np.arange(1, monos+1) 
    rooms = np.array([str(i) for i in range(1, rooms+1)])

    # data struct for final solution set
    solution = {i: [] for i in rooms}

    for mono in monos:
        for room in rooms:
            if place_mono(solution[room], mono) is True:
                solution[room].append(mono)
                break 
            if room == rooms[-1]:
                return False
            
#    if len(monos) > 0:
#        return False

    return solution

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
    monos, rooms = 5, 2
    monos, rooms = 23, 3
    #monos, rooms = 24, 3
    print(f'Solving for {monos} monopoles in {rooms} rooms')

    solution = solve(monos, rooms)

    show_results(solution)

    print(f'Script completed in {time.time()-start:.8f} secs')

    return 0

if __name__ == '__main__':
    sys.exit(main())
