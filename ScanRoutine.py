from time import sleep
from ChessPiece import *
from NFC_Functions import *

NumChessPiece = 32
PieceList = []
record = open("piece_record.txt", "w+")
record.write("T P C           uid                    x y\r\n" )

for total in range(0, NumChessPiece):
    print(total)
    #determine color
    if total >= 16:
        color = 1
    else:
        color = 0

    # designate piece type
    if total >= 16:
        piece = piece_types(total-16)
    else:
        piece = piece_types(total)

    #get uid
    uid = None
    while uid is None or find_uid(uid,PieceList):
        uid = scan_nfc()

    #create new ChessPiece Object
    PieceList.append(ChessPiece(piece,color,uid,total,total))
    record.write(str(total) + " " 
                 + str(PieceList[total].piece) + " "
                 + str(PieceList[total].color) + " "
                 + str(PieceList[total].uid) + " "
                 + str(PieceList[total].x_pos) + " "
                 + str(PieceList[total].y_pos) + "\r\n")
    sleep(0.25)
    #move to new location - add stepper code

