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
    
   
