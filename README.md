# Gale Shapley Algorithm Implementation - by Elaine Nelson


This is my version to implement the Gale-Shapley Algorithm. This was an optional project I did for my Algorithm Design and Analysis course with some modifications.

Code needs to be run in the command line as ' gs.py n k '. Where n is the number of two equally sized sets(for this example we have hospitals and students as the two sets) and k is the number of possible ranking lists. We are assuming that there are only a few possible rankings.

Some clarification (in this example n = 5): 
         
      0 1 2 0 2 1 <-- which row in prefence list each element prefers for set 1. So element 0 (at index 0) prefers rank list 0 
      
      0 0 0 1 2 2 <-- which row in prefence list each element prefers for set 2. So element 3 (at index 3) prefers rank list 1 
      


