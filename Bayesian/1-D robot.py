import matplotlib.pyplot as plt
%matplotlib inline

import numpy as np

def initialize_robot(grid_size):
    
    grid = []
    
    for i in range(grid_size):
        grid.append(1./grid_size)
   
    return grid
    
    
    
    ##Test##
    # Result should be a list with 9 elements all having value 1/9
assert initialize_robot(9) == [1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9]

# Result should be a list with 4 elements all having value 1/4
assert initialize_robot(4) == [1/4, 1/4, 1/4, 1/4]

print('Hooray! You just initialized a discrete probability distribution')



import matplotlib.pyplot as plt
%matplotlib inline

import numpy as np

def output_map(grid):
    x_labels = range(len(grid))
    plt.bar(x_labels, grid)
    plt.xlabel('Grid Space')
    plt.ylabel('Probability')
    plt.title('Probability of the Robot Being at Each Space on the Grid')
    plt.show()
    
    
 #Test
  output_map([.2, .2, .2, .2, .2])
    
    
    
 def update_probabilities(grid, updates):
    for i in range(len(updates)):
        grid[updates[i][0]] = updates[i][1]
        
    return grid


#Test
assert update_probabilities([0.2, 0.2, 0.2, 0.2, 0.2], [[0, .4], [1, 0.15], [2, 0.15], [3, 0.15], [4, 0.15]]) == [0.4, 0.15, 0.15, 0.15, 0.15]
assert update_probabilities([0.2, 0.2, 0.2, 0.2, 0.2], [[1, 0.15], [0, .4], [4, 0.15], [2, 0.15], [3, 0.15]]) == [0.4, 0.15, 0.15, 0.15, 0.15]
assert update_probabilities([0.2, 0.2, 0.2, 0.2, 0.2], [[0, .25], [4, 0.15]]) == [0.25, 0.2, 0.2, 0.2, 0.15]

print('Everything looks good!')
   
