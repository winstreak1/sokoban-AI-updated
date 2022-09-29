
# import student's functions
from solution import *
from search import *

#Select algorithm to test by changinge False to True
test_BFS = False
test_DFS = False
test_manhattan = False
test_anytime_gbfs = False
test_anytime_weighted_astar = False
test_non_trivial = True
test_fval_function = False


if test_BFS:
    ##############################################################
    # TEST ALTERNATE HEURISTIC
    print('Testing alternate heuristic with breadth-first search')

    solved = 0
    unsolved = []
    benchmark = 0
    timebound = 15  # 4 second time limit
    for i in range(0, len(PROBLEMS)):
        print("*************************************")
        print("GAME {}".format(i+1))

        s0 = PROBLEMS[i]  # Problems get harder as i gets bigger
        se = SearchEngine('breadth_first', 'full')
        se.init_search(s0, goal_fn=sokoban_goal_state, heur_fn=heur_alternate)
        # se.init_search(s0, goal_fn=sokoban_goal_state, heur_fn=heur_euclidean_distance)
        final = se.search(timebound)

        if final:
            #final.print_path()
            solved += 1
        else:
            unsolved.append(i)

    print("\n*************************************")
    print("Of 10 initial games, {} were solved in less than {} seconds by this solver.".format(solved, timebound))
    print("Games that remain unsolved in the set are Games: {}".format(unsolved))
    print("The benchmark implementation solved 14 out of the 40 practice problems given 4 seconds.")
    print("*************************************\n")
    ##############################################################


if test_DFS:
    ##############################################################
    # TEST ALTERNATE HEURISTIC
    print('Testing alternate heuristic with depth-first search')

    solved = 0
    unsolved = []
    benchmark = 0
    timebound = 15  # 4 second time limit
    for i in range(0, len(PROBLEMS)):
        print("*************************************")
        print("GAME {}".format(i+1))

        s0 = PROBLEMS[i]  # Problems get harder as i gets bigger
        se = SearchEngine('depth_first', 'full')
        se.init_search(s0, goal_fn=sokoban_goal_state, heur_fn=heur_alternate)
        # se.init_search(s0, goal_fn=sokoban_goal_state, heur_fn=heur_euclidean_distance)
        final = se.search(timebound)

        if final:
            #final.print_path()
            solved += 1
        else:
            unsolved.append(i)

    print("\n*************************************")
    print("Of 10 initial games, {} were solved in less than {} seconds by this solver.".format(solved, timebound))
    print("Games that remain unsolved in the set are Games: {}".format(unsolved))
    print("The benchmark implementation solved 14 out of the 40 practice problems given 4 seconds.")
    print("*************************************\n")
    ##############################################################


if test_manhattan:
    ##############################################################
    # TEST MANHATTAN DISTANCE
    print('Testing Manhattan Distance')

    #Correct Manhattan distances for the initial states of the provided problem set
    correct_man_dist = [4, 4, 2, 8, 11, 11, 14, 14, 27, 9, ]

    solved = 0
    unsolved = []
#iteration through Games 1-6
    for i in range(0, 6):
        print("GAME {}".format(i+1))
#save problem(games) set to s0.
        s0 = PROBLEMS[i]

        man_dist = heur_manhattan_distance(s0)
        print('calculated man_dist:', str(man_dist))
        #To see state
        #print(s0.state_string())
#conditinoal statement to increase 'solved' by 1
        if man_dist == correct_man_dist[i]:
            solved += 1
        else:
            unsolved.append(i)    

    print("*************************************")  
    print("In the problem set provided, you calculated the correct Manhattan distance for {} states out of 6.".format(solved))
    print("States that were incorrect: {}".format(unsolved))      
    print("*************************************\n") 
    ##############################################################


if test_anytime_gbfs:

  len_benchmark = [23, 35, 27, 20, 41, 41, -99, -99, -99, -99]

  ##############################################################
  # TEST ANYTIME GBFS
  print('Testing Anytime GBFS')

  solved = 0
  unsolved = []
  benchmark = 0
  timebound = 60
  for i in range(0, 6):
    print("*************************************")  
    print("GAME {}".format(i+1))
#save PROBLEMS[i] to s0
    s0 = PROBLEMS[i] #Problems get harder as i gets bigger
    weight = 10
    final = anytime_gbfs(s0, heur_fn=heur_displaced, timebound=timebound)
#conditional statemenet comparing benchmark to final.gval
    if final:
      #final.print_path()
      if final.gval <= len_benchmark[i] or len_benchmark[i] == -99:
        benchmark += 1
      solved += 1 
    else:
      unsolved.append(i)  

  print("\n*************************************")  
  print("Of 6 initial problems, {} were solved in less than {} seconds by this solver.".format(solved, timebound))
  print("Of the {} problems that were solved, the cost of {} matched or outperformed the benchmark.".format(solved, benchmark))  
  print("Problems that remain unsolved in the set are Problems: {}".format(unsolved))  
  print("The benchmark implementation solved 6 out of the 10 practice problems given 8 seconds.")
  print("*************************************\n") 
  ##############################################################

if test_anytime_weighted_astar:

  len_benchmark = [23, 35, 27, 20, 41, 41, -99, -99, -99, -99]

  ##############################################################
  # TEST ANYTIME WEIGHTED A STAR
  print('Testing Anytime Weighted A Star')

  solved = 0
  unsolved = []
  benchmark = 0
  timebound =  15 #second time limit
  #iteration through problem(game) set 1-6
  for i in range(0, 6):
    print("*************************************")  
    print("GAME {}".format(i+1))
#save PROBLEMS[i] to s0 memory and other declarations
    s0 = PROBLEMS[i]
    weight = 10
    final = anytime_weighted_astar(s0, heur_fn=heur_displaced, weight=weight, timebound=timebound)
#conditional statement comparing final.gval to len_benchmark[i]
    if final:
      #final.print_path()
      if final.gval <= len_benchmark[i] or len_benchmark[i] == -99:
        benchmark += 1
      solved += 1 
    else:
      unsolved.append(i)  

  print("\n*************************************")  
  print("Of 6 initial problems, {} were solved in less than {} seconds by this solver.".format(solved, timebound))
  print("Of the {} problems that were solved, the cost of {} matched or outperformed the benchmark.".format(solved, benchmark))  
  print("Games that remain unsolved in the set are Problems: {}".format(unsolved))
  print("The benchmark implementation solved 6 out of the 10 practice games given 8 seconds.")
  print("*************************************\n") 
  ##############################################################

if test_non_trivial:

  ##############################################################
  # TEST ALTERNATE HEURISTIC
  print('Testing alternate heuristic with uniform-cost search')

  solved = 0; unsolved = []; benchmark = 0; timebound = 8 #8 second time limit
  for i in range(0, len(PROBLEMS)):
    print("*************************************")
    print("GAME {}".format(i+1))

#declarations referencing functions from search.py
    s0 = PROBLEMS[i] #Problems get harder as i gets bigger
    se = SearchEngine('custom', 'full')
    se.init_search(s0, goal_fn=sokoban_goal_state, heur_fn=heur_alternate)
    #se.init_search(s0, goal_fn=sokoban_goal_state, heur_fn=heur_euclidean_distance)
    final = se.search(timebound)

    if final:
      #final.print_path()
      solved += 1
    else:
      unsolved.append(i)

  print("\n*************************************")
  print("Of 6 initial problems, {} were solved in less than {} seconds by this solver.".format(solved, timebound))
  print("Problems that remain unsolved in the set are Problems: {}".format(unsolved))
  print("The benchmark implementation solved 14 out of the 40 practice problems given 4 seconds.")
  print("*************************************\n")
  ##############################################################

if test_fval_function:

  test_state = SokobanState("START", 6, None, None, None, None, None, None, None)

  correct_fvals = [6, 11, 16]

  ##############################################################
  # TEST fval_function
  print("*************************************") 
  print('Testing fval_function')

  solved = 0
  weights = [0., .5, 1.]
  for i in range(len(weights)):

    test_node = sNode(test_state, hval=10, fval_function=fval_function)

    fval = fval_function(test_node, weights[i])
    print ('Test', str(i), 'calculated fval:', str(fval), 'correct:', str(correct_fvals[i]))
    
    if fval == correct_fvals[i]:
      solved +=1  


  print("\n*************************************")  
  print("Your fval_function calculated the correct fval for {} out of {} tests.".format(solved, len(correct_fvals)))  
  print("*************************************\n") 
  ##############################################################


