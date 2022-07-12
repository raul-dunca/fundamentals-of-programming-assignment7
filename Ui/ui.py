
from game.field import Field,Custom_exception
from Computer.ComputerPlayer import ComputerPlayerRandom,ComputerPlayer
from copy import deepcopy

class UI:
    def __init__(self,w,h,ok):
        if w%2==1 and h%2==1 and ok==False:
            self._ai=ComputerPlayer(w,h)
            self._k=True
        else:
            self._ai = ComputerPlayerRandom()
            self._k=False
        self._field = Field(w, h)
        self._first=ok
        self._move=""
    def start(self):
        print("Welcome to Obstruction!")
        player_turn = self._first
        while not self._field.is_full():
            try:

                print(str(self._field))

                if player_turn:

                    move = input("Enter your move: ")
                    self._move=move
                    if (move[0]>='A' and move[0]<="Z") and (move[1:].isnumeric()):
                        self._field.move(move, 'X')
                    else:
                        raise Custom_exception("Invalid input!")
                else:
                    if(self._k):
                        ai_move = self._ai.move(self._move)

                        print("Computer moves at " + str(ai_move))
                        self._field.move(ai_move, 'O')

                    else:

                        ai_move = self._ai.move(self._field)
                        print("Computer moves at " + str(ai_move))
                        self._field.move(ai_move, 'O')

                player_turn = not player_turn
            except Custom_exception as ce:
                print(ce)
        if player_turn:
            print("You LOST!")
        else:
            print("You WON!")

