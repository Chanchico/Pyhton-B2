
from game import Game

def main():
    j = 0
    game = Game()
    for i in game.pawns:
        
        j+= 1
        print( str(j) +" " + i.name + i.color + str(i.coordinate_x) + str(i.coordinate_y))

main()

