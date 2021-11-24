from pawn import Pawn

class Game:
    pawns = []
    
    def __init__(self):
        self.positioning()

    def positioning(self):
        pawns = []
        for i in range(1 ,9):
            for j in range(1, 9):
                n = 0
                c = 0
                if i < 3:
                    c = 1
                elif i > 6:
                    c = 2
                if i == 1 or i == 8:
                    if j == 1 or j == 8:
                        n = 5 # Rook
                    elif j == 2 or j == 7:
                        n = 4 # Knight
                    elif j == 3 or j == 6:
                        n = 3 #Bishop
                    elif j == 4:
                        n = 1 #King
                    elif j == 5:
                        n = 2 #Queen
                if i == 2 or i == 7:
                    n = 6 # pawn
                #case vide
                if i > 2 and i < 7:
                    n = 0 
                    c = 0

                self.pawns.append(Pawn(n, c, i, j))

        