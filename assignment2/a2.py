# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.

    def __init__(self, symbol, row, col):
        """ (Rat, str, int, int) -> NoneType

        Initialize the rat's four instance variables.
        >>> rat = Rat('P', 1, 4)
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        """ (Rat, int, int) -> NoneType

        Set the rat's row and col instance variables to the given row and column.
        """
        self.row = row
        self.col = col

    def eat_sprout(self):
        """ (Rat) -> NoneType

         Add one to the rat's instance variable num_sprouts_eaten.
        """
        self.num_sprouts_eaten += 1

    def __str__(self):
        """ (Rat) -> str

        Return a string representation of the rat.
        """
        return '%s at (%s, %s) ate %s sprouts.' % (self.symbol,
                                                   self.row,
                                                   self.col,
                                                   self.num_sprouts_eaten)


class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self, maze, rat_1, rat_2):
        """ (Maze, list of list of str, Rat, Rat) -> NoneType

        Initialize maze.
        """ 
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = 0
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if self.maze[row][col] == SPROUT:
                    self.num_sprouts_left += 1 

    def is_wall(self, row, col):
        """ (Maze, int, int) -> bool

        Return True if and only if there is a wall at the given row
        and column of the maze.
        """

        return self.maze[row][col] == WALL

    def get_character(self, row, col):
        """ (Maze, int, int) -> str

        Return the character in the maze at the given row and column. 
        If there is a rat at that location,
        then its character should be returned rather than HALL.
        """

        if (row, col) == (self.rat_1.row, self.rat_1.col):
            return self.rat_1.symbol
        elif (row, col) == (self.rat_2.row, self.rat_2.col):
            return self.rat_2.symbol

        return self.maze[row][col]

    def move(self, rat, ver_dire, hor_dire):
        """ (Maze, Rat, int, int) -> bool

        Return True if and only if there wasn't a wall in the way
        """
        new_row = rat.row
        new_col = rat.col
        

        # vertical direction change
        if ver_dire == UP:
            new_row += UP
        elif ver_dire == DOWN:
            new_row += DOWN
        elif ver_dire == NO_CHANGE:
            new_row += NO_CHANGE

        # horizontal direction change
        if hor_dire == LEFT:
            new_col += LEFT
        elif hor_dire == RIGHT:
            new_col += RIGHT
        elif hor_dire == NO_CHANGE:
            new_col += NO_CHANGE

        if self.is_wall(new_row, new_col):
            return False

        check_char = self.get_character(new_row, new_col)
        if check_char == SPROUT:
            self.maze[new_row][new_col] = HALL
            self.num_sprouts_left -= 1
            rat.eat_sprout()
            rat.set_location(new_row, new_col)
        elif check_char == HALL:
            rat.set_location(new_row, new_col)

        return True

    def __str__(self):
        """ (Maze) -> str

        Return a string representation of the maze.
        """

        rat_1_location = (self.rat_1.row, self.rat_1.col)
        rat_2_location = (self.rat_2.row, self.rat_2.col)

        string = ""

        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if (row, col) == rat_1_location:
                    string += self.rat_1.symbol
                elif (row, col) == rat_2_location:
                    string += self.rat_2.symbol
                else:
                    string += self.maze[row][col]
            string += '\n'
        string += self.rat_1.__str__()
        string += '\n'
        string += self.rat_2.__str__()

        return string
