class ChessPiece(object):
    # 0 - Pawn, 1 - Rook, 2 - Bishop, 3 - Knight, 4 - Queen, 5 - King
    # 0 - white, 1 - black
   def __init__(self,piece, color, uid, x_pos, y_pos):
       self.piece = piece
       self.uid = uid
       self.x_pos = x_pos
       self.y_pos = y_pos
       self.color = color

#Loopable piece designations
#first 8 entries are pawns
#second 8 are other pieces
def piece_types(loop):
    pieces = {
        0:0,
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:1,
        9:2,
        10:3,
        11:4,
        12:5,
        13:3,
        14:2,
        15:1

    }
    return pieces[loop]
