# Gale Shapley Algorithm Implementation - by Elaine Nelson


This is my version to implement the Gale-Shapley Algorithm. This was an **optional** project I did for my Algorithm Design and Analysis course with some modifications.

Code needs to be run in the command line as ' gs.py n k '. Where n is the number of two equally sized sets(for this example we have hospitals and students as the two sets) and k is the number of possible ranking lists. We are assuming that there are only a few possible rankings.

Some clarification (in this example n = 5): 
         
      0 1 2 0 2 1 <-- which row in prefence list each element prefers for set 1. So element 0 (at index 0) prefers rank list 0 
      
      0 0 0 1 2 2 <-- which row in prefence list each element prefers for set 2. So element 3 (at index 3) prefers rank list 1 
      
Output example: 
```
gs.py 5 3

Possible ranking/preference lists a hospital chooses from:
Rank list  1 : 1 2 4 0 3
Rank list  2 : 4 1 0 2 3
Rank list  3 : 0 1 3 2 4

Possible ranking/preference lists set a student chooses from:
Rank list  1 : 4 1 2 0 3
Rank list  2 : 1 0 4 2 3
Rank list  3 : 3 4 2 0 1

Indexes of chosen preference lists for hospitals:
Indexes for each:  2 1 0 0 2

Indexes of chosen preference lists for students:
Indexes for each:  1 0 0 0 0

Stable matches that have been created:
Hospital  1 matches with student 4
Hospital  0 matches with student 0
Hospital  4 matches with student 1
Hospital  2 matches with student 2
Hospital  3 matches with student 3
Algorithm complete!
```

