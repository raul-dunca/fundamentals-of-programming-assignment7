import random
from copy import deepcopy


"""
            This class  follows the next strategy:
            If there are more the 9 empty squares the Computer just moves to a random square,
            otherwise: first it "moves" in every free square and checks if the board is full if so it makes that move,
            otherwise it undo's it. After that, if there isnt a move that can close the game it will try and make a move
            after which will remain an even number of free squares, if there doesnt exist such a move it will move random
"""
class ComputerPlayerRandom():
    def move(self, field):
        stack = []
        stack.append(deepcopy(field._data))       #we store the state of the field befoare moving

        if len(field.empty_squares()) > 9:
            square = random.choice(field.empty_squares())
            # Convert (1,1) to A1
            return chr(square[1] + 65) + str(square[0])         #if there are more the 9 free squares move randomly
        elif len(field.empty_squares()) > 0:
            k = int(0)
            i = field.empty_squares()
            while k < len(i):
                p = i[k]
                field.move(chr(p[1] + 65) + str(p[0]), 'O')   #make the moves in order
                stack.append(deepcopy(field._data))          #remember the state after the move
                if field.is_full():
                                                 #if after the move the field is full we undo the move and give the field the initial values and return the move
                    field.undo(stack)           # in order to make it in the ui
                    field._data.clear()
                    field._data=(deepcopy(stack[-1]))

                    return chr(p[1] + 65) + str(p[0])
                field.undo(stack)          # if after the move the field is not full we just undo the move
                field._data.clear()
                field._data = (deepcopy(stack[-1]))

                k += 1

            k = int(0)
            i = field.empty_squares()
            while k < len(i):
                p = i[k]
                field.move(chr(p[1] + 65) + str(p[0]), 'O')      #make the moves in order
                stack.append(deepcopy(field._data))              #remember the state after the move
                j = field.empty_squares()
                if len(j) % 2 == 0:                             #check if after the move we have an even number of empty squares
                    field.undo(stack)
                    field._data.clear()                         #if sowe undo the move and give the field the initial values and return the move
                    field._data = (deepcopy(stack[-1]))
                    return chr(p[1] + 65) + str(p[0])           # in order to make it in the ui
                field.undo(stack)
                field._data.clear()                              # if after the move the field is not full we just undo the move and continue
                field._data = (deepcopy(stack[-1]))
                k += 1
            square = random.choice(field.empty_squares())       #if this type of move is not possible just move random
            return chr(square[1] + 65) + str(square[0])







        """
            This class  follows the next strategy:
            If the board is odd and Computer makes the first move, then the first move will be in the center of the board.
            In order to win, next the Computer will only mirror the player's moves.
        """
class ComputerPlayer():

    def __init__(self, w, h):
        self._width = w
        self._height = h
        self._ok = 0

    def move(self, move):
        if (self._ok == 0):
            self._ok += 1
            w = (self._width // 2)
            h = (self._height // 2)
            return chr(w + 65) + str(h)
        else:
            col = ord(move[0]) - 65
            row = int(move[1:])
            return chr(self._width - 1 - col + 65) + str(self._height - 1 - row)
