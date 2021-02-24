# Gale Shapley Algorithm Implementation


This is my version to implement the Gale-Shapley Algorithm. This was an optional project I did for my Algorithm Design and Analysis course.

Code needs to be run in the command line as ' gs.py n k '. Where n is the number of two equally sized sets(for this example we have hospitals and students as the two sets) and k is the number of possible ranking lists. We are assuming that there are only a few possible rankings. The last two lines in the input file show the indexes of each ranking that each element prefers. For example:     
         
      0 1 2 0 2 1 <-- which row in prefence list each element prefers for set 1. So element 0 (at index 0) prefers rank list 0 
      
      0 0 0 1 2 2 <-- which row in prefence list each element prefers for set 2. So element 3 (at index 3) prefers rank list 1 
      


