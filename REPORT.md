# Sokoban Analysis

#### Peter Mavronicolas
#### Old Dominion University
#### Fall 2022, CS 580
#### February 28, 2022

## Solutions
### Breadth-First Search
*************************************
GAME 1
Solution Found with cost of 45 in search time of 0.421875 sec
Nodes expanded = 16426, states generated = 40639, states cycle check pruned = 24213, states cost bound pruned = 0
*************************************
GAME 2
Solution Found with cost of 22 in search time of 3.65625 sec
Nodes expanded = 131358, states generated = 288550, states cycle check pruned = 157192, states cost bound pruned = 0
*************************************
GAME 3
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 448981, states generated = 953991, states cycle check pruned = 505010, states cost bound pruned = 0
*************************************
GAME 4
Solution Found with cost of 126 in search time of 14.5 sec
Nodes expanded = 467618, states generated = 1116646, states cycle check pruned = 649028, states cost bound pruned = 0
*************************************
GAME 5
Solution Found with cost of 34 in search time of 4.015625 sec
Nodes expanded = 129208, states generated = 310746, states cycle check pruned = 181538, states cost bound pruned = 0
*************************************
GAME 6
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 469814, states generated = 1048462, states cycle check pruned = 578648, states cost bound pruned = 0

### Depth-First Search
*************************************
GAME 1
Solution Found with cost of 51 in search time of 0.546875 sec
Nodes expanded = 16660, states generated = 41707, states cycle check pruned = 25047, states cost bound pruned = 0
*************************************
GAME 2
Solution Found with cost of 81 in search time of 0.078125 sec
Nodes expanded = 3039, states generated = 7911, states cycle check pruned = 4872, states cost bound pruned = 0
*************************************
GAME 3
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 1915632, states generated = 4763797, states cycle check pruned = 2848165, states cost bound pruned = 0
*************************************
GAME 4
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 1969160, states generated = 4763646, states cycle check pruned = 2794486, states cost bound pruned = 0
*************************************
GAME 5
Solution Found with cost of 49 in search time of 1.546875 sec
Nodes expanded = 48684, states generated = 129806, states cycle check pruned = 81122, states cost bound pruned = 0
*************************************
GAME 6
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 1841171, states generated = 4913299, states cycle check pruned = 3072128, states cost bound pruned = 0

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
calculated man_dist: 9
*************************************
### GAME 4
calculated man_dist: 8
*************************************
### GAME 5
calculated man_dist: 7
*************************************
### GAME 6
calculated man_dist: 7

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
Solution Found with cost of 45 in search time of 0.421875 sec
Nodes expanded = 11856, states generated = 27992, states cycle check pruned = 16136, states cost bound pruned = 0
Solution Found with cost of 45 in search time of 0.0 sec
Nodes expanded = 11977, states generated = 28305, states cycle check pruned = 16312, states cost bound pruned = 16
Solution Found with cost of 45 in search time of 0.0 sec
Nodes expanded = 12013, states generated = 28440, states cycle check pruned = 16395, states cost bound pruned = 32
Solution Found with cost of 45 in search time of 0.015625 sec
Nodes expanded = 12382, states generated = 29487, states cycle check pruned = 17030, states cost bound pruned = 75
Search Failed! No solution found.
Nodes expanded = 16027, states generated = 40482, states cycle check pruned = 23962, states cost bound pruned = 493
*************************************
### GAME 2
Solution Found with cost of 26 in search time of 0.40625 sec
Nodes expanded = 11881, states generated = 25178, states cycle check pruned = 13297, states cost bound pruned = 0
Solution Found with cost of 26 in search time of 0.0 sec
Nodes expanded = 11882, states generated = 25181, states cycle check pruned = 13297, states cost bound pruned = 2
Solution Found with cost of 26 in search time of 0.0 sec
Nodes expanded = 11883, states generated = 25201, states cycle check pruned = 13309, states cost bound pruned = 9
Solution Found with cost of 26 in search time of 0.0 sec
Nodes expanded = 11884, states generated = 25236, states cycle check pruned = 13329, states cost bound pruned = 23
Solution Found with cost of 26 in search time of 0.0 sec
Nodes expanded = 11885, states generated = 25319, states cycle check pruned = 13384, states cost bound pruned = 50
Solution Found with cost of 26 in search time of 0.109375 sec
Nodes expanded = 14333, states generated = 31761, states cycle check pruned = 16743, states cost bound pruned = 685
Solution Found with cost of 25 in search time of 0.03125 sec
Nodes expanded = 14981, states generated = 33426, states cycle check pruned = 17594, states cost bound pruned = 851
Solution Found with cost of 25 in search time of 0.0 sec
Nodes expanded = 15139, states generated = 33939, states cycle check pruned = 17849, states cost bound pruned = 951
Solution Found with cost of 24 in search time of 0.03125 sec
Nodes expanded = 16122, states generated = 36015, states cycle check pruned = 18798, states cost bound pruned = 1095
Solution Found with cost of 22 in search time of 0.375 sec
Nodes expanded = 25626, states generated = 57652, states cycle check pruned = 29935, states cost bound pruned = 2091
Search Failed! No solution found.
Nodes expanded = 83769, states generated = 236566, states cycle check pruned = 122252, states cost bound pruned = 30545
*************************************
### GAME 3
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 337898, states generated = 693902, states cycle check pruned = 356004, states cost bound pruned = 0
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 612260, states generated = 1292582, states cycle check pruned = 680322, states cost bound pruned = 0
*************************************
### GAME 4
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 315090, states generated = 733931, states cycle check pruned = 418841, states cost bound pruned = 0
*************************************
### GAME 5
Solution Found with cost of 34 in search time of 0.765625 sec
Nodes expanded = 15784, states generated = 35863, states cycle check pruned = 20079, states cost bound pruned = 0
*************************************
### GAME 6
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 343306, states generated = 790567, states cycle check pruned = 447261, states cost bound pruned = 0

### Non-Trivial Heuristic
*************************************
### GAME 1
Solution Found with cost of 45 in search time of 0.03125 sec
Nodes expanded = 1140, states generated = 2613, states cycle check pruned = 1473, states cost bound pruned = 0
*************************************
### GAME 2
Solution Found with cost of 32 in search time of 0.015625 sec
Nodes expanded = 743, states generated = 1257, states cycle check pruned = 514, states cost bound pruned = 0
*************************************
### GAME 3
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 221985, states generated = 527200, states cycle check pruned = 305215, states cost bound pruned = 0
*************************************
### GAME 4
Solution Found with cost of 164 in search time of 1.484375 sec
Nodes expanded = 39309, states generated = 86500, states cycle check pruned = 47191, states cost bound pruned = 0
*************************************
### GAME 5
Solution Found with cost of 34 in search time of 0.03125 sec
Nodes expanded = 943, states generated = 2057, states cycle check pruned = 1114, states cost bound pruned = 0
*************************************
### GAME 6
TRACE: Search has exceeded the time bound provided.
Search Failed! No solution found.
Nodes expanded = 210849, states generated = 522941, states cycle check pruned = 312092, states cost bound pruned = 0

## Comparison
*************************************
Out of all the algorithms implemented, the Greedy-Best algorithm showed the greatest success rate by solving 3/6 games. Among all the remaining algorithms, 2/6 games were solved. By increasing the time interval for all algorithms, results improved based on the additional attempts at searching the tree. 


## Analysis
*************************************

### Breadth-First Search
*************************************
Of 6 initial games, 4 were solved in less than 15 seconds by this solver.
Games that remain unsolved in the set are Games: [3, 6]
The benchmark implementation solved 14 out of the 40 practice problems given 4 seconds.

### Depth-First Search
*************************************
Of 6 initial games, 3 were solved in less than 15 seconds by this solver.
Games that remain unsolved in the set are Games: [3, 4, 6]
The benchmark implementation solved 14 out of the 40 practice problems given 4 seconds.

### Manhattan Heuristic
*************************************
In the problem set provided, you calculated the correct Manhattan distance for 2 states out of 6.
States that were incorrect: [2, 3, 5, 6]

### Greedy Best
*************************************
Of 6 initial problems, 4 were solved in less than 60 seconds by this solver.
Of the 4 problems that were solved, the cost of 1 matched or outperformed the benchmark.
Problems that remain unsolved in the set are Problems: [3, 6]
The benchmark implementation solved 6 out of the 10 practice problems given 8 seconds.

### A Star
*************************************
Of 6 initial problems, 3 were solved in less than 15 seconds by this solver.
Of the 3 problems that were solved, the cost of 2 matched or outperformed the benchmark.
Games that remain unsolved in the set are Problems: [3, 4, 6]
The benchmark implementation solved 6 out of the 10 practice games given 8 seconds.

### Non-Trivial Heuristic
*************************************
Of 6 initial problems, 4 were solved in less than 8 seconds by this solver.
Problems that remain unsolved in the set are Problems: [3, 6]
The benchmark implementation solved 14 out of the 40 practice problems given 4 seconds.

## References
*************************************
 #### Fung, A (angusfung), sokoban-AI, Github, accessed September 27, 2022, https://github.com/angusfung/sokoban-AI
