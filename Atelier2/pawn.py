
class Pawn:
    pawn_dic = (
        "",
        "King",
        "Queen",
        "Bishop",
        "Knight",
        "Rook",
        "Pawn"  
    )

    color_dic = (
        "",
        "White",
        "Black"
    )

    def __init__(self, name = int, color = int, coordinate_x = int, coordinate_y = int):
        self.color = self.color_dic[color]
        self.name = self.pawn_dic[name]
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y

    
    

    