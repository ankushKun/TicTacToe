from board import Board
from player import Player
from time import sleep

def start_game() -> None:
    board = Board()

    board.newgame()

    current = 'X'
    while(True):
        if current=='X':
            name = board.p1.name
            piece=board.p1.piece
        else:
            name = board.p2.name
            piece=board.p2.piece

        board.print_board()
        coor = input(f"{name} >> Where do you want to put your piece({piece})? [x,y] ")
        try:
            x,y=coor.split(',')
            x,y=int(x),int(y)
        except Exception as e:
            print("Improper Input")
            sleep(1)
            continue
        if x>2 or x<0 or y>2 or y<0:
            print("\nYou can put your piece there -_-\n")
            sleep(1)
        else:
            if board.is_empty(x,y):
                board.p1.place(board,x,y) if current=='X' else board.p2.place(board,x,y)
                current = 'O' if current=='X' else 'O'
                if board.winner()=="X":
                    print(f">>> {board.p1.name} has won")
                    break
                elif board.winner()=="O":
                    print(f">>> {board.p2.name} has won")
                    break
            else:
                print("\nYou can put your piece there -_-\n")
                sleep(1)


start_game()
