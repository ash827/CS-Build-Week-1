# creating our board

from cell import Cell
from random import randint

class Board:
    def __init__(self , rows , columns):
        # this will take in specified cell sizes from the user to generate grid
        self._rows = rows
        self._columns = columns   
        self._grid = [[Cell() for column_cells in range(self._columns)] for row_cells in range(self._rows)]

        self._generate_board()

    def draw_board(self):
        # drawing the board
        # print('\n'*25)
        print('Now Printing...')
        for row in self._grid:
            for column in row:
                print (column.character(),end='')
            print()

    def _generate_board(self):
        # generating random board
        for row in self._grid:
            for column in row:
                chance_number = randint(0,2)
                if chance_number == 1:
                    column.set_alive()

    def update_board(self):
        """
        updates the board based on the check 
        of each cell pr. generation
        """
        # cells list for living cells to kill and cells to resurrect or keep alive
        comes_alive = []
        gets_killed = []

        for row in range(len(self._grid)):
            for column in range(len(self._grid[row])):
                # check neighbor square:
                check_neighbor = self.check_neighbor(row, column)
                
                living_neighbors_count = []

                for neighbor_cell in check_neighbor:
                    # check live status for neighbor_cell:
                    if neighbor_cell.is_alive():
                        living_neighbors_count.append(neighbor_cell)

                cell_object = self._grid[row][column]
                status_main_cell = cell_object.is_alive()

                # If the cell is alive, check the neighbor status.
                if status_main_cell == True:
                    if len(living_neighbors_count) < 2 or len(living_neighbors_count) > 3:
                        gets_killed.append(cell_object)

                    if len(living_neighbors_count) == 3 or len(living_neighbors_count) == 2:
                        comes_alive.append(cell_object)

                else:
                    if len(living_neighbors_count) == 3:
                        comes_alive.append(cell_object)

        # set cell statuses
        for cell_items in comes_alive:
            cell_items.set_alive()

        for cell_items in gets_killed:
            cell_items.set_dead()

    
    
    def check_neighbor(self, check_row , check_column):
        '''
        checks all the 8 neighbors for the cells and returns 
        the list of the valid neighbors so the update method 
        can set the new status
        '''        
        # how deep the search is:
        search_min = -1
        search_max = 2

        # empty list to append neighbors into.
        neighbor_list = []
        for row in range(search_min,search_max):
            for column in range(search_min,search_max):
                neighbor_row = check_row + row
                neighbor_column = check_column + column 
                
                valid_neighbor = True

                if (neighbor_row) == check_row and (neighbor_column) == check_column:
                    valid_neighbor = False

                if (neighbor_row) < 0 or (neighbor_row) >= self._rows:
                    valid_neighbor = False

                if (neighbor_column) < 0 or (neighbor_column) >= self._columns:
                    valid_neighbor = False

                if valid_neighbor:
                    neighbor_list.append(self._grid[neighbor_row][neighbor_column])
        return neighbor_list
