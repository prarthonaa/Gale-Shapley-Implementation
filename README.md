# Gale Shapley Algorithm Implementation


This is my version to implement the Gale-Shapley Algorithm. This was an optional project I did for my COMP 3600 (Algorithm Design and Analysis) course.

1. The random instance generator creates a file in the 'sampleinput.txt' (or below) format. Code needs to be run in the command line as randomInstanceGenerator.py n k. Where n is the number of two equally sized sets and k is the number of possible ranking lists. We are assuming that there are only a few possible rankings. The last two lines in the input file show the indexes of each ranking that each element prefers. So for example if we have input such that:
      
      6 (value of n)
      3 (value of k)
      
      0 1 2 3 4 5 <-- preference list of set 1 ( we start at 0 )
   \  0 4 3 2 1 5
   \  2 4 5 1 3 0
      
      5 4 3 2 1 0 <-- preference list of set 2
   \  1 2 4 5 3 0
   \  4 3 1 0 2 5
      
      0 1 2 0 2 1 <-- which row in prefence list each element prefers for set 1. So element 0 (at index 0) prefers rank list 0 (which is 0 1 2 3 4 5) and so on
      
      0 0 0 1 2 2 <-- which row in prefence list each element prefers for set 2. So element 3 (at index 3) prefers rank list 1 (which is 1 2 4 5 3 0) and so on
      
3. This file is later taken as an input to 'galeshapley.py' to produce an output file of matches, in the format similar to 'sampleoutput.txt' or below: 
      (this is not the actual result of the algorithm for input example above!)
      0 3
      1 2
      4 4
      5 1
      2 0
      3 5    
5. 'gstest.py' is a file used to test the running time of the code without the tedious process of converting the input file to arrays

