import unittest
from game.field import Field,Custom_exception
from Computer.ComputerPlayer import ComputerPlayerRandom,ComputerPlayer
class FieldTest(unittest.TestCase):
    def setUp(self):
        self._field=Field(5,5)
    def test_move_corners(self):
        self._field.move("A0", "X")
        self.assertEqual(self._field._data,[["X","*",0,0,0],["*","*",0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
        self.assertRaises(Custom_exception, self._field.move, "A1", "X")
        self.assertRaises(Custom_exception, self._field.move, "A30", "X")
        self._field.move("E0", "O")
        self.assertEqual(self._field._data,[["X", "*", 0, "*", "O"], ["*", "*", 0, "*", "*"], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
        self._field.move("A4", "X")
        self.assertEqual(self._field._data,[["X", "*", 0, "*", "O"], ["*", "*", 0, "*", "*"], [0, 0, 0, 0, 0], ["*", "*", 0, 0, 0],["X", "*", 0, 0, 0]])
        self._field.move("E4", "O")
        self.assertEqual(self._field._data,[["X", "*", 0, "*", "O"], ["*", "*", 0, "*", "*"], [0, 0, 0, 0, 0], ["*", "*", 0, "*", "*"],["X", "*", 0, "*", "O"]])
    def test_move_edge_moves(self):
        f=Field(5,5)
        f.move("A2", "X")
        self.assertEqual(f._data,[[0,0,0,0,0],["*","*",0,0,0],["X","*",0,0,0],["*","*",0,0,0],[0,0,0,0,0]])
        f.move("C0","O")
        self.assertEqual(f._data, [[0,"*","O", "*", 0], ["*", "*", "*", "*", 0], ["X", "*", 0, 0, 0], ["*", "*", 0, 0, 0], [0, 0, 0, 0, 0]])
        f.move("E2", "O")
        self.assertEqual(f._data,[[0, "*", "O", "*", 0], ["*", "*", "*", "*", "*"], ["X", "*", 0, "*", "O"], ["*", "*", 0, "*", "*"],[0, 0, 0, 0, 0]])
        f.move("C4","X")
        self.assertEqual(f._data, [[0, "*", "O", "*", 0], ["*", "*", "*", "*", "*"], ["X", "*", 0, "*", "O"],["*", "*", "*", "*", "*"], [0, "*", "X", "*", 0]])
    def test_move_center(self):
        v=Field(3,3)
        v.move("B1","X")
        self.assertEqual(v._data, [["*", "*", "*",], ["*", "X", "*"], ["*", "*","*"]])
    def test_empty(self):
        self.assertEqual(self._field.empty_squares(),[(0, 0),(0, 1),(0, 2),(0, 3),(0, 4),(1, 0),(1, 1),(1, 2),(1, 3),(1, 4),(2, 0),(2, 1),(2, 2),(2, 3),(2, 4),(3, 0),(3, 1),(3, 2),(3, 3),(3, 4),(4, 0),(4, 1),(4, 2),(4, 3),(4, 4)])
    def test_full(self):
        r = Field(3, 3)
        self.assertEqual(r.is_full(),False)
        r.move("B1", "X")
        self.assertEqual(r.is_full(), True)
    def test_print(self):
        print(str(self._field))
    def tearDown(self):
        self._repo = None


class ComputerTest(unittest.TestCase):
    def setUp(self):
        self._field=Field(5,5)
        self._ai = ComputerPlayerRandom()
    def test_computer_move(self):
        self._field.move("C2","X")
        while not self._field.is_full():
            self._field.move(self._ai.move(self._field),"O")


    def tearDown(self):
        self._repo = None


class ComputerTestStrategy(unittest.TestCase):
    def setUp(self):
        self._field = Field(5, 5)
        self._ai = ComputerPlayer(5,5)

    def test_computer_move(self):
        self._field.move(self._ai.move(self._field),"O")
        self.assertEqual(self._field._data,[[0,0,0,0,0],[0,"*","*","*",0],[0,"*","O","*",0],[0,"*","*","*",0],[0,0,0,0,0]])
        self._field.move("A0","X")
        self._field.move(self._ai.move("A0"), "O")
        self.assertEqual(self._field._data,[["X", "*", 0, 0, 0], ["*", "*", "*", "*", 0], [0, "*", "O", "*", 0], [0, "*", "*", "*", "*"],[0, 0, 0, "*", "O"]])
    def tearDown(self):
        self._repo = None