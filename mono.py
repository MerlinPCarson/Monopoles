#!/usr/bin/python3
# Monopole solver
# by Merlin Carson

import sys
import time


def parse_args(args):

    if len(args) < 3 or int(sys.argv[1]) > 52:
        sys.exit("Usage: ./mono.py <num monopoles (<=52)> <num rooms>")

    return int(sys.argv[1]), int(sys.argv[2])
   
def solve(monos, rooms):
  
    solution = {str(i): [] for i in range(1, rooms+1)},  
    print(solution)
    for room in range(rooms):
        for mono in range(monos):
            pass
            
        
def main():
    start = time.time()

    monos, rooms = parse_args(sys.argv)
    print(f'Solving for {monos} monopoles in {rooms} rooms')

    solve(monos, rooms)

    print(f'Script completed in {time.time()-start:.2f} secs')

    return 0

if __name__ == '__main__':
    sys.exit(main())
