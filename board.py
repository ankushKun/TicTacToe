class Board:
    def __init__(self) -> None:
        self.board=[['','',''], # X ---->
                    ['','',''], # Y |
                    ['','','']] #   V
        self.turns=0

    def newgame(self) -> None:
        __init__(self)

    def print_board(self) -> None:
        for y in range(3):
            for x in range(3):
                print('-' if self.board[y][x] == '' else self.board[y][x],end="")
            print()

    def is_empty(self,x:int,y:int) -> bool:
        return self.board[y][x]==''

    def place(self,x:int,y:int,p:str) -> None:
        if self.is_empty(x,y):
            self.board[y][x]=p
            self.turns+=1

    def winner(self) -> str:
        # CHECK HORIZONTAL
        winner = '-'
        if self.turns>=9:
            return "Game Over"
        for y in range(3):
            if self.board[y][0]==self.board[y][1]==self.board[y][2]!='':
                winner = self.board[y][1]
        # CHECK VERTICAL
        for x in range(3):
            if self.board[0][x]==self.board[1][x]==self.board[2][x]!='':
                winner = self.board[1][x]
        # CHECK DIAGONAL
        if self.board[0][0]==self.board[1][1]==self.board[2][2]!='' or self.board[0][2]==self.board[1][1]==self.board[2][0]!='':
                winner = self.board[1][1]
        return winner
