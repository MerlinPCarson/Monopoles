# Monopoles
Solver for Dr. Ecco's Monopole challenge from Dr. Dobb's Journel Of Computer Calisthenics and Orthodontia September 01, 1999

by Merlin Carson

written using Python3


# Usage
./monodfs \<number of monopoles\> \<number of rooms\>

This program uses a depth first search of the state space, placing m monopoles in n rooms with the constraint that no room contains two monopoles whose sum equal another monopole in the same room.

I first tried filling rooms 1 at a time, moving on to the next room once the constraint for the current room would be violated by placing the next monopole. I then tried placing each monopole in the first available room that fit the constraint. Both worked for m=5 and n=2, but got stuck on m=23 and n=3. Once stuck, I tried discarding entire rooms in order, trying to place their contents in other rooms before filling the discared room back up. This also got stuck. I then implemented a depth first search, placing each monopole in the first room that would accept it. I created a dictionary with lists for each room and passed this to each recursive call, so I didn't have to create duplicates of my data structure. I appended placed monopoles to the list corresponding to the room it was placed in and popped them out of the list if I every got stuck. Once all monopoles are placed the recursion unwinds, the solution is verfied and then printed to the screen, with each row of values representing the monopoles placed in that room. If all combinations are exhausted without a correct solution, the dictionary returns with all room lists empty and 'unsat' is printed to the screen.

# Experiments
All experiements were conduction on a Dell 3400 Latitude laptop with a 2.3 GHz i3 processor.

23 monopoles were placed in 3 rooms in ~0.01 secs

24 monopoles in 3 rooms was determined to be unsatisfiable in ~0.5 secs

53 monopoles were placed in 4 rooms in ~0.1 secs

54 monopoles were placed in 4 rooms in ~8 mins
