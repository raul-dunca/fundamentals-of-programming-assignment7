from texttable import Texttable



class Custom_exception(Exception):
    """
    Writing (Exception) tells Python that RepoExc... is an Exception
    """
    pass


class Field:
    def __init__(self, width, height):
        self._cols = width
        self._rows = height
        # 0 is default value
        self._data = [[0] * self._cols for i in range(self._rows)]
    def move(self, square, symbol):
        """
        Turn square into coordinates
        """
        col = ord(square[0]) - 65
        row = int(square[1:])

        self._move(row, col, symbol)

    def undo(self, stack):
        """
        a undo function needed at computer tactic

        """
        if (len(stack) > 1):
            stack.pop()
            return stack[-1]

    def _move(self, x, y, symbol):
        """
        Make a move on the board
        :param x: Row
        :param y: Column
        :param symbol: Player sign (X or O)
        """
        if not (0 <= x < self._rows and 0 <= y < self._cols):
            raise Custom_exception("Not a valid cell!")

        if self._data[x][y] != 0:
            raise Custom_exception("Cell already taken!")
        self._data[x][y]=symbol
        if (x==0 and y==0):                  #this is the up left corner
            self._data[x+1][y]="*"
            self._data[x + 1][y+1] = "*"
            self._data[x][y+1] = "*"
        elif (y==0 and x==self._rows-1):     #this is the down left corner
            self._data[x - 1][y] = "*"
            self._data[x - 1][y + 1] = "*"
            self._data[x][y + 1] = "*"
        elif (x==0 and y==self._cols-1):     #this is the up right corner
            self._data[x][y - 1] = "*"
            self._data[x + 1][y - 1] = "*"
            self._data[x + 1][y] = "*"
        elif  (y==self._cols-1 and x==self._rows-1):          #this is the down right corner
            self._data[x - 1][y] = "*"
            self._data[x - 1][y - 1] = "*"
            self._data[x][y - 1] = "*"
        elif x==0 and y!=0 and y!=self._cols-1:            #this is the case where the move is made on the first row but not in corners
            self._data[x][y-1]="*"
            self._data[x+1][y - 1] = "*"
            self._data[x+1][y] = "*"
            self._data[x+1][y+1] = "*"
            self._data[x][y+1] = "*"
        elif y==self._cols-1 and x!=self._rows-1 and x!=0:           #this is the case where the move is made on the last collum but not in corners
            self._data[x-1][y] = "*"
            self._data[x + 1][y - 1] = "*"
            self._data[x][y-1] = "*"
            self._data[x - 1][y - 1] = "*"
            self._data[x+1][y] = "*"
        elif y==0 and x!=0 and x!=self._rows-1:                     #this is the case where the move is made on the first collum but not in corners
            self._data[x + 1][y] = "*"
            self._data[x + 1][y +1] = "*"
            self._data[x][y+1] = "*"
            self._data[x -1][y+1] = "*"
            self._data[x - 1][y] = "*"
        elif x==self._rows-1 and y!=self._cols-1 and y!=0:          #this is the case where the move is made on the last row but not in corners
            self._data[x][y-1] = "*"
            self._data[x - 1][y - 1] = "*"
            self._data[x-1][y] = "*"
            self._data[x - 1][y + 1] = "*"
            self._data[x][y+1] = "*"

        else:                                           #else(if it is a "center move") aka if all the nine squares need to be filled

            i=int(0)
            while i<=2:
                try:
                    if self._data[x-1][y-1+i] == 0:
                        self._data[x-1][y-1+i]="*"
                    i+=1
                except IndexError:
                    i+=1
            i = int(0)
            while i <= 2:
                try:
                    if self._data[x][y - 1 + i] == 0:
                        self._data[x][y - 1 + i] = "*"
                    i += 1
                except IndexError:
                    i+=1
            i = int(0)
            while i <= 2:
                try:
                    if self._data[x +1][y - 1 + i] == 0:
                        self._data[x +1][y - 1 + i] = "*"
                    i += 1
                except IndexError:
                    i+=1

    def empty_squares(self):
        """
        Return a list of all non-played squares
        """
        result = []
        for i in range(self._rows):
            for j in range(self._cols):
                if self._data[i][j] == 0:
                    result.append((i, j))
        return result

    def is_full(self):
        """
        Returns True if the field is full,otherwise False
        """
        k = int(0)
        for i in range(self._rows):
            for j in range(self._cols):
                if self._data[i][j] == 0:
                    k+=1
        if k==0:
            return True
        else:
            return False

    def __str__(self):
        """
        Here we just print field in a nice format !
        """

        col_width=[]
        for i in range(self._cols):
            if i<26:
                col_width.append(1)
        col_width.append(1)

        t = Texttable()
        t.set_cols_width(col_width)

        # Horizontal header
        header_row = ['/']
        for i in range(self._cols):
            if i<26:
                header_row.append(chr(65 + i))

        t.header(header_row)

        for i in range(self._rows):
            row = self._data[i]
            # Initialize vertical header
            display_row = [i]

            for j in range(self._cols):
                if j<26:
                    val = self._data[i][j]
                    if val == 0:
                        display_row.append(' ')
                    else:
                        display_row.append(val)

            t.add_row(display_row)

        return t.draw()
