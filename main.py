from board import Board
from player import Player

b = Board()
p1 = Player(name='P1',piece='X')
p2 = Player(name='P2',piece='O')

p1.place(b,0,2)
