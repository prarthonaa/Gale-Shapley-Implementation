# Gale Shapley Algorithm Implementation


This is my version to implement the Gale-Shapley Algorithm. This was an optional project I did for my Algorithm Design and Analysis course.

1. The random instance generator creates a file in the 'sampleinput.txt' (or below) format. Code needs to be run in the command line as ' randomInstanceGenerator.py n k '. Where n is the number of two equally sized sets and k is the number of possible ranking lists. We are assuming that there are only a few possible rankings. The last two lines in the input file show the indexes of each ranking that each element prefers. For example:     
         
      0 1 2 0 2 1 <-- which row in prefence list each element prefers for set 1. So element 0 (at index 0) prefers rank list 0 
      
      0 0 0 1 2 2 <-- which row in prefence list each element prefers for set 2. So element 3 (at index 3) prefers rank list 1 
      
3. This file is later taken as an input to 'galeshapley.py' to produce an output file of matches, in the format similar to 'sampleoutput.txt' or below: 
     
5. 'gstest.py' is a file used to test the running time of the code without the tedious process of converting the input file to arrays

