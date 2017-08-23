"""
Kaemon Zachary Derrick
Project 1. Solving Diagonal Sudoku
January 31st 2017

This project implements the Eliminate Strategy, Only Choice Strategy,
Naked Twins Strategy and Recursive Search to solve a Diagonal Sudoku Puzzle.


Note: Some code reused from the course.

"""
#Cross declared above variables because some variables use this function
def cross(A, B):
    return [s+t for s in A for t in B]


#################Variable Declaration#########################

assignments = []
rows = 'ABCDEFGHI'
cols = '123456789'
boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') 
    for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

#For Right -> Left peers
y = 8

#Create Diagonal Peers Left -> Right, Right -> Left
diagonalLR = [0,0,0,0,0,0,0,0,0]
diagonalRL = [0,0,0,0,0,0,0,0,0]
for x in range(0,9):
    diagonalLR[x] = row_units[x][x]
    diagonalRL[x] = row_units[x][y-x]

#For each box that appers in the Diagonal, add its Diagonal Counterparts
# to its list of peers
for y in range(0,9):
        for x in range(0,9):
            if (diagonalLR[y] != diagonalLR[x]):
                peers[diagonalLR[y]].add(diagonalLR[x])
            if (diagonalRL[y] != diagonalRL[x]):
                peers[diagonalRL[y]].add(diagonalRL[x])

#################Function Declaration#########################

def assign_value(values, box, value):
    """
    ***Function taken exactly from: Udacity Solving a Sudoku with AI ***

    Assigns a value to a given box. If it updates the board record it.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
        box: a key in the dictionary
        value: new value to be assigned to key

    Returns:
        the values dictionary 
    """   
    
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
        
    return values

def naked_twins(values):
    """Eliminates values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """     
    #For each of the rows, columns, squares                         
    for x in range(0,9):
        #Use Naked Twins Technique on the rows 
        for unit in row_units[x]:
            if (len(values[unit]) == 2):                                           
                for compare in row_units[x]:
                    if (values[compare] == values[unit] and compare != unit): 
                        for c in values[unit]:
                            for update in row_units[x]:
                                if (update != unit and update != compare):
                                    tempString = values[update]
                                    tempString = tempString.replace(c, "")
                                    assign_value(values, update, tempString)
                                          
        #Use Naked Twins Technique on the Columns 
        for unit in column_units[x]:
            if (len(values[unit]) == 2):                                           
                for compare in column_units[x]:
                    if (values[compare] == values[unit] and compare != unit): 
                        for c in values[unit]:
                            for update in column_units[x]:
                                if (update != unit and update != compare):
                                    tempString = values[update]
                                    tempString = tempString.replace(c, "")
                                    assign_value(values, update, tempString)
                                          
        #Use Naked Twins Technique on the Squares
        for unit in square_units[x]:
            if (len(values[unit]) == 2):                                           
                for compare in square_units[x]:
                    if (values[compare] == values[unit] and compare != unit): 
                        for c in values[unit]:
                            for update in square_units[x]:
                                if (update != unit and update != compare):
                                    tempString = values[update]
                                    tempString = tempString.replace(c, "")
                                    assign_value(values, update, tempString)
                                          
    #Use Naked Twins Technique on the Left-Right Diagonal
    for unit in diagonalLR:
        if (len(values[unit]) == 2):                                           
            for compare in diagonalLR:
                if (values[compare] == values[unit] and compare != unit): 
                    for c in values[unit]:
                        for update in diagonalLR:
                            if (update != unit and update != compare):
                                tempString = values[update]
                                tempString = tempString.replace(c, "")
                                assign_value(values, update, tempString)
                                      
    #Use Naked Twins Technique on the Right-Left Diagonal
    for unit in diagonalRL:
        if (len(values[unit]) == 2):                                           
            for compare in diagonalRL:
                if (values[compare] == values[unit] and compare != unit): 
                    for c in values[unit]:
                        for update in diagonalRL:
                            if (update != unit and update != compare):
                                tempString = values[update]
                                tempString = tempString.replace(c, "")
                                assign_value(values, update, tempString)
                                      
    return values

def grid_values(grid):
    """
    Converts string into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. 
                    If a box has no value, then the value will be '123456789'.
    """
    values = []
    options = '123456789'
    for char in grid:
        if char == '.':
            values.append(options)
        else:
            values.append(char)
    assert len(values) == 81
    return dict(zip(boxes, values))

def display(values):
    """
    ***Function taken exactly from: Udacity Solving a Sudoku with AI ***
    
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """    

    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):
    #Check every box, if the box has a final value (Length == 1),
    #remove that value from its undetermined peers (Length > 1).
    for unit in units:
        if (len(values[unit]) == 1):
            for peer in peers[unit]:
                tempString = values[peer]
                tempString = tempString.replace(values[unit],"")
                assign_value(values, peer, tempString)

    return values

def only_choice(values): 
    """
    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """

    #For each Sq. use only choice technique
    count = 0
    for x in range(0,9):
        for y in range (0,9):
            count = 0
            if (len(values[square_units[x][y]]) > 1):
                tempString = values[square_units[x][y]]
                for k in range (0, len(tempString)):
                    for z in range (0,9):
                        comparingString = values[square_units[x][z]]
                        if (tempString[k] in comparingString):
                            count = count + 1
                    if (count == 1):
                        assign_value(values, square_units[x][y], tempString[k])
                        count = 0
                        break
                    count = 0
                    
    #For each column use only choice technique
    for x in range(0,9):
        for y in range (0,9):
            count = 0
            if (len(values[column_units[x][y]]) > 1):
                tempString = values[column_units[x][y]]
                for k in range (0, len(tempString)):
                    for z in range (0,9):
                        comparingString = values[column_units[x][z]]
                        if (tempString[k] in comparingString):
                            count = count + 1
                    if (count == 1):
                        assign_value(values, column_units[x][y], tempString[k])
                        count = 0
                        break
                    count = 0
    
    #For each row use only choice technique
    for x in range(0,9):
        for y in range (0,9):
            count = 0
            if (len(values[row_units[x][y]]) > 1):
                tempString = values[row_units[x][y]]
                for k in range (0, len(tempString)):
                    for z in range (0,9):
                        comparingString = values[row_units[x][z]]
                        if (tempString[k] in comparingString):
                            count = count + 1
                    if (count == 1):
                        assign_value(values, row_units[x][y], tempString[k])
                        count = 0
                        break
                    count = 0
                    
    #For Left -> Right Daigonal
    for y in range (0,9):
        count = 0
        if (len(values[diagonalLR[y]]) > 1):
            tempString = values[diagonalLR[y]]
            for k in range (0, len(tempString)):
                for z in range (0,9):
                    comparingString = values[diagonalLR[y]]
                    if (tempString[k] in comparingString):
                        count = count + 1
                if (count == 1):
                    assign_value(values, diagonalLR[y], tempString[k])
                    count = 0
                    break
                count = 0
                
    #For Right -> Left Daigonal
    for y in range (0,9):
        count = 0
        if (len(values[diagonalRL[y]]) > 1):
            tempString = values[diagonalRL[y]]
            for k in range (0, len(tempString)):
                for z in range (0,9):
                    comparingString = values[diagonalRL[y]]
                    if (tempString[k] in comparingString):
                        count = count + 1
                if (count == 1):
                    assign_value(values, diagonalRL[y], tempString[k])
                    count = 0
                    break
                count = 0
    return values

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        #Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() 
        if len(values[box]) == 1])
        
        #Eliminate Strategy
        values = eliminate(values)
        
        #Only Choice Strategy
        values = only_choice(values)
        
        #Naked Twins Strategy
        values = naked_twins(values)
        
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() 
        if len(values[box]) == 1])
        
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        
        # Return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


def search(values):
    #After we guess a value, eliminate more possibilities 
    values = reduce_puzzle(values)
    
    #If values is false, then atleast one box contains 0 possibilities. (Wrong)
    #This means that we must go back up the DFS tree and choose another value
    #for the box.
    if values is False:
        return False ## Failed earlier
    
    #If all boxes contain only one number, we know that the Sudoku puzzle is 
    #solved and we can return the solved puzzle.
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
        
    # Choose a square with least possibilities. By doing so we reduce the 
    #number of possibilites for the puzzle.
    length = 9
    index = ""
    options = ""
    for unit in units:
        if (len(values[unit]) < length and len(values[unit]) > 1):
            index = unit
            length = len(values[unit])
            options = values[unit]
            
    #Recursion to solve each one of the resulting sudokus
    #For each of the possibilities of the square, try and solve the puzzle.
    for c in options:
        new_sudoku = values.copy()
        new_sudoku[index] = c
        attempt = search(new_sudoku)
        
        #If the puzzle is returned we know that a result has been found.
        #We will then pass up the reurned puzzle through the 
        #DFS tree until the top when we finally return the solved puzzle. 
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...
            9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. 
        False if no solution exists.
        
    """
    #Take the string and turn it into a Dictionary 
    puzzle = grid_values(grid)
    
    #Solve as many boxes we can with the values we have
    puzzle = reduce_puzzle(puzzle)
    
    #Use DFS to solve the remaining boxes in the puzzle
    puzzle = search(puzzle)
    
    return puzzle

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))
    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
