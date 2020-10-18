from board import Board

class Player:
    def __init__(self,name:str,piece:str) -> None:
        piece=piece.upper()
        if not (piece=='O' or piece=='X'):
            raise Exception("piece should be either 'X' or 'O'")
        self.name = name
        self.piece = piece

    def place(self,b:Board,x:int,y:int) -> None:
        b.place(x,y,self.piece)
        print(f"{self.name} >> placed an {self.piece} on {x},{y}")
        b.print_board()
