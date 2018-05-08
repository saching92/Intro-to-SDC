def initial_grid(rows, columns):

    # TODO: initialize an empty list in a variable called grid
    grid = []
    
    # TODO: initialize an empty row in a variable called row
    row = []

    # TODO: calculate the initial probability
    probability = 1./(rows*columns)
    
    for i in range(rows):
        for j in range(columns):
            row.append(probability)
        grid.append(row)
        row=[]
        
        
        
    
    # TODO: write a nested for loop that appends values to the grid variable
    # HINT: You first need to fill in a row with values and then append the row to the grid.
    #        Then you'll need to set the row variable to an empty list.
    #        The logic of all this can be tough to think through. 
    #        If you get stuck, see the demonstrations in the previous part of the lesson
        
    return grid
    
    def probability(grid, row, column):
    
    
    # TODO: return the probability that the robot as at the space representing by the row and column values.
    
    return grid[row][column]
    
    ####Test
    
    assert probability([[.25, .1], 
                    [.45, .2]], 
                   1, 1) == 0.2

assert probability([[.05, .1, .1],
                    [.04, .3, .02],
                    [.01, .02, .02],
                    [.005, .012, .06],
                    [.09, .07, .103]], 3, 2) == 0.06

assert probability([[.05, .1, .1],
                    [.04, .3, .02],
                    [.01, .023, .017],
                    [.005, .012, .06],
                    [.09, .07, .103]], 2, 2) == .017

print('You passed all the assertion tests.')
