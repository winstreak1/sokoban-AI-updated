# Sokoban Analysis

#### Peter Mavronicolas
#### Old Dominion University
#### Fall 2022, CS 580
#### February 28, 2022

## Solutions
### Breadth-First Search
*************************************
### GAME 1
Solution Found with cost of 45 in search time of 0.453125 sec
Nodes expanded = 16426, states generated = 40639, states cycle check pruned = 24213, states cost bound pruned = 0
### GAME 2
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 295580, states generated = 739841, states cycle check pruned = 444261, states cost bound pruned = 0
*************************************
### GAME 3
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 282637, states generated = 587762, states cycle check pruned = 305125, states cost bound pruned = 0
*************************************
### GAME 4
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 282883, states generated = 670757, states cycle check pruned = 387874, states cost bound pruned = 0
*************************************
### GAME 5
Solution Found with cost of 34 in search time of 4.125 sec
Nodes expanded = 129208, states generated = 310746, states cycle check pruned = 181538, states cost bound pruned = 0
ACTION was START

*************************************
### GAME 6
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 282540, states generated = 620243, states cycle check pruned = 337703, states cost bound pruned = 0

### Depth-First Search
*************************************
### GAME 1
Solution Found with cost of 51 in search time of 0.484375 sec
Nodes expanded = 16660, states generated = 41707, states cycle check pruned = 25047, states cost bound pruned = 0
*************************************
### GAME 2
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 139536, states generated = 379659, states cycle check pruned = 240123, states cost bound pruned = 0
*************************************
### GAME 3
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 147599, states generated = 368868, states cycle check pruned = 221269, states cost bound pruned = 0
*************************************
### GAME 4
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 157408, states generated = 384336, states cycle check pruned = 226928, states cost bound pruned = 0
*************************************
### GAME 5
Solution Found with cost of 49 in search time of 1.421875 sec
Nodes expanded = 48684, states generated = 129806, states cycle check pruned = 81122, states cost bound pruned = 0
*************************************
### GAME 6
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 141108, states generated = 375625, states cycle check pruned = 234517, states cost bound pruned = 0

### Manhattan Heuristic
Testing Manhattan Distance
*************************************
### GAME 1
calculated man_dist: 4
*************************************
### GAME 2
calculated man_dist: 9
*************************************
### GAME 3
calculated man_dist: no results
*************************************
### GAME 4
calculated man_dist: no results
*************************************
### GAME 5
calculated man_dist: no results
*************************************
### GAME 6
calculated man_dist: no results

### Greedy Best
*************************************
### GAME 1
0.21875
#### Solution Found with cost of 49 in search time of 0.203125 sec
Nodes expanded = 6492, states generated = 15947, states cycle check pruned = 9455, states cost bound pruned = 0
0.421875
#### Solution Found with cost of 49 in search time of 0.015625 sec
Nodes expanded = 6700, states generated = 16475, states cycle check pruned = 9744, states cost bound pruned = 31
0.4375
#### Solution Found with cost of 47 in search time of 0.046875 sec
Nodes expanded = 8804, states generated = 21613, states cycle check pruned = 12751, states cost bound pruned = 58
0.484375
#### Solution Found with cost of 47 in search time of 0.015625 sec
Nodes expanded = 9089, states generated = 22385, states cycle check pruned = 13193, states cost bound pruned = 103
0.5
#### Solution Found with cost of 47 in search time of 0.046875 sec
Nodes expanded = 10773, states generated = 26629, states cycle check pruned = 15632, states cost bound pruned = 224
0.546875
#### Solution Found with cost of 47 in search time of 0.0 sec
Nodes expanded = 10953, states generated = 27119, states cycle check pruned = 15915, states cost bound pruned = 251
0.546875
#### Solution Found with cost of 45 in search time of 0.234375 sec
Nodes expanded = 17894, states generated = 44519, states cycle check pruned = 26229, states cost bound pruned = 396
0.78125
#### Solution Found with cost of 45 in search time of 0.0 sec
Nodes expanded = 18047, states generated = 44916, states cycle check pruned = 26447, states cost bound pruned = 422
0.78125
#### Solution Found with cost of 45 in search time of 0.015625 sec
Nodes expanded = 18632, states generated = 46376, states cycle check pruned = 27282, states cost bound pruned = 462
0.796875
#### Solution Found with cost of 45 in search time of 0.0 sec
Nodes expanded = 18660, states generated = 46451, states cycle check pruned = 27319, states cost bound pruned = 472
0.796875
#### Search Failed! No solution found.
Nodes expanded = 26742, states generated = 67192, states cycle check pruned = 39786, states cost bound pruned = 664
*************************************
### GAME 2
1.0625
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 237951, states generated = 644209, states cycle check pruned = 406258, states cost bound pruned = 0
9.078125
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 465198, states generated = 1263513, states cycle check pruned = 798315, states cost bound pruned = 0
*************************************
### GAME 3
17.09375
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 236312, states generated = 578434, states cycle check pruned = 342122, states cost bound pruned = 0
*************************************
### GAME 4
25.109375
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 245549, states generated = 585641, states cycle check pruned = 340092, states cost bound pruned = 0
*************************************
### GAME 5
33.125
Solution Found with cost of 44 in search time of 0.109375 sec
Nodes expanded = 4220, states generated = 10572, states cycle check pruned = 6352, states cost bound pruned = 0
*************************************
### GAME 6
33.25
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 236020, states generated = 607969, states cycle check pruned = 371949, states cost bound pruned = 0

### A Star
*************************************
### GAME 1
#### Solution Found with cost of 45 in search time of 0.46875 sec
Nodes expanded = 11856, states generated = 27992, states cycle check pruned = 16136, states cost bound pruned = 0
#### Solution Found with cost of 45 in search time of 0.015625 sec
Nodes expanded = 11977, states generated = 28305, states cycle check pruned = 16312, states cost bound pruned = 16
#### Solution Found with cost of 45 in search time of 0.0 sec
Nodes expanded = 12013, states generated = 28440, states cycle check pruned = 16395, states cost bound pruned = 32
#### Solution Found with cost of 45 in search time of 0.015625 sec
Nodes expanded = 12382, states generated = 29487, states cycle check pruned = 17030, states cost bound pruned = 75
#### Search Failed! No solution found.
Nodes expanded = 16027, states generated = 40482, states cycle check pruned = 23962, states cost bound pruned = 493
*************************************
### GAME 2
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 170548, states generated = 409513, states cycle check pruned = 238965, states cost bound pruned = 0
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 313622, states generated = 785362, states cycle check pruned = 471740, states cost bound pruned = 0
*************************************
### GAME 3
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 172540, states generated = 346727, states cycle check pruned = 174187, states cost bound pruned = 0
*************************************
### GAME 4
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 157910, states generated = 372561, states cycle check pruned = 214651, states cost bound pruned = 0
*************************************
### GAME 5
Solution Found with cost of 34 in search time of 0.671875 sec
Nodes expanded = 15784, states generated = 35863, states cycle check pruned = 20079, states cost bound pruned = 0
*************************************
### GAME 6
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 181025, states generated = 400567, states cycle check pruned = 219542, states cost bound pruned = 0

### Non-Trivial Heuristic
*************************************
### GAME 1
Solution Found with cost of 45 in search time of 0.625 sec
Nodes expanded = 16504, states generated = 40821, states cycle check pruned = 24317, states cost bound pruned = 0
*************************************
### GAME 2
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 189761, states generated = 438858, states cycle check pruned = 249097, states cost bound pruned = 0
*************************************
### GAME 3
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 182539, states generated = 371253, states cycle check pruned = 188714, states cost bound pruned = 0
*************************************
### GAME 4
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 185452, states generated = 441131, states cycle check pruned = 255679, states cost bound pruned = 0
*************************************
### GAME 5
Solution Found with cost of 34 in search time of 5.390625 sec
Nodes expanded = 131871, states generated = 317319, states cycle check pruned = 185448, states cost bound pruned = 0
*************************************
### GAME 6
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 198218, states generated = 430763, states cycle check pruned = 232545, states cost bound pruned = 0

## Comparison
*************************************
Out of all the algorithms implemented, the Greedy-Best algorithm showed the greatest success rate by solving 3/6 games. Among all the remaining algorithms, 2/6 games were solved. By increasing the time interval for all algorithms, results improved based on the additional attempts at searching the tree. 


## Analysis
*************************************
### Breadth-First Search
*************************************
1 of 6 test cases passed on a 4 second time limit. An increase to 10 seconds had a result of 2/6 test cases passing. The passing test cases are Game 1 and Game 5. Of 10 initial games, 2 were solved in less than 10 seconds by this solver. Problems that remain unsolved in the set are games 2, 3, 4, and 6.

### Depth-First Search
*************************************
Of 10 initial games, 2 were solved in less than 4 seconds by this solver.
Games that remain unsolved in the set are Games: [2, 3, 4, 6].
The benchmark implementation solved 14 out of the 40 practice problems given 4 seconds.

### Manhattan Heuristic
*************************************
After the initial run, only the first two games[1,2], produced a manhattan heuristic result. Games [3,4,5,6] remained unsolved without any relevant data.

### Greedy Best
*************************************
Of 10 initial problems, 2 were solved in less than 8 seconds by this solver.
Of the 2 problems that were solved, the cost of 0 matched or outperformed the benchmark.
Problems that remain unsolved in the set are Problems: [2, 3, 4]
The benchmark implementation solved 6 out of the 10 practice problems given 8 seconds.

### A Star
*************************************
Of 10 initial problems, 2 were solved in less than 8 seconds by this solver.
Of the 2 problems that were solved, the cost of 1 matched or outperformed the benchmark.
Problems that remain unsolved in the set are Problems: [2, 3, 4]
The benchmark implementation solved 6 out of the 10 practice problems given 8 seconds.

### Non-Trivial Heuristic
*************************************
Of 6 initial games, 2 were solved in less than 8 seconds by this solver.
Games that remain unsolved in the set are Games: [2, 3, 4, 6]
The benchmark implementation solved 14 out of the 40 practice games given 4 seconds.

## Conclusion
*************************************
Improvements will need to be made to the conditional statements for all search when the number of boxes, 'B' are greater than the number of storage locations, 'S'. This causes the compiler to run in an infinite loop if the time constraint were absent.
## References
*************************************
 #### Fung, A (angusfung), sokoban-AI, Github, accessed September 27, 2022, https://github.com/angusfung/sokoban-AIPROBLEM 6
TRACE: Search has exceeeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 197842, states generated = 429868, states cycle check pruned = 232026, states cost bound pruned = 0