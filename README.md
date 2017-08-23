# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Naked Twins method we can eliminate the options from peers if two of the peers contain only two values and both peers contain the exact same values. 
That means that these boxes are either of the two values and if one box takes one of the values, the other box will have to be equal to the other value. Since those boxes are confied to either of 
those two values, it means that the peers in row, column, sq, and diagonal that the two boxes are located in cannot be any of those two values.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: **Diagonal boxes added to peers**

By using the given values in the puzzle, we are able to obtian more information about the puzzle by reducing the options [of the unsolved] boxes [peers] accosicated with this box, that is, 
a value can only appear once in any sq, row, column and diagonal. We can use the Eliminate function to remove from its peers, the solved value as an option for that unit.
After, we can use the Only Choice method to reduce the options of the unsolved boxes further. The Only_choice() function looks for a unsolved box and checks the rows, columns, squares and diagonals [if 
it is a box in the diagonal] and if a value that only appears once, we can assign that value to the box. We now that the value cannot be anywhere else within its peers and therefore it must be at this box. 
Now, using the Naked Twins method we can eliminate the options from peers if two of the peers contain only two values and both peers contain the exact same values. 
That means that these boxes are either of the two values and if one box takes one of the values, the other box will have to be equal to the other value. Since those boxes are confied to either of 
those two values, it means that the peers in row, column, sq, and diagonal that the two boxes are located in cannot be any of those two values. 
    By reducing the possibilities of the unknown boxes as much as possible, we narrow the options for the Search() function. The search function finds the box of the smallest possibilities and tries the 
possibilities for that box. It then tries to work out the puzzle with the first value, calling the previous functions to reduce the puzzle further and calling itself again and again for the options that are 
not solved after the reducing functions (eliminate, only_choice and Naked Twins) we can call search again and again until it is solved or until we try all the values and the puzzle is unsolveable.


### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
