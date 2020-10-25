#!/usr/bin/python3
# Monopole solver for Dr. Ecco challenege
# by Merlin Carson

import sys
import time


def parse_args(args):

    if len(args) < 3:
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

def verify_all_monos(solution, num_monos):
    
    for mono in range(1, num_monos+1):
        for i, (_, values) in enumerate(solution.items(), start=1):
            if mono in values:
                break 
            if i == len(solution.keys()):
                return False

    return True

def verify_solution(solution, num_monos):

    # check to make sure all monopoles have been placed in rooms
    if not verify_all_monos(solution, num_monos):
        print('[Invalid Solution]: not all monopoles placed in rooms!')
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
                        print(f'[Invalid Solution]: additive monopole combination found in room {key}!')
                        return None

    print('Solution verified.')
    return solution

def solver(num_monos, num_rooms):

    # lists of all possible monopoles and rooms
    monos = list(range(1,num_monos+1))
    monos.append(-1) # add stopping condition
    rooms = [str(i) for i in range(1, num_rooms+1)]

    # data struct for final solution set
    solution = {i: [] for i in rooms}

    return solve(monos, monos.pop(0), rooms, solution)


def solve(monos, mono, rooms, solution):

    # base case
    if mono == -1:
        return solution

    # place monopole
    for room in rooms:
        if place_mono(solution[room], mono) is True:
            solution[room].append(mono)
            solution = solve(monos, monos.pop(0), rooms, solution)
            if len(monos) == 0:
                return solution
            solution[room].pop()

    monos.insert(0, mono)
    return solution
    
def show_results(solution):

    if solution is None:
        print('\nunsat')
    else:
        print('\nSolution:\n')
        for i, key in enumerate(solution.keys()):
            print(f'Room {chr(i+65)}:', end=' ')
            for value in solution[key]:
                print(value, end=' ')
            print()
    print()

def main():
    start = time.time()

    num_monos, num_rooms = parse_args(sys.argv)
    print(f'Solving for {num_monos} monopoles in {num_rooms} rooms.')

    solution = solver(num_monos, num_rooms)

    print(f'Solution found in {time.time()-start:.8f} secs.')

    solution = verify_solution(solution, num_monos)
    show_results(solution)

    print(f'Script completed in {time.time()-start:.8f} secs.')

    return 0

if __name__ == '__main__':
    sys.exit(main())
