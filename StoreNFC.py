from time import sleep
import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.spi import PN532_SPI
import ChessPiece

#Create SPI Connection
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs_pin = DigitalInOut(board.D5)


pn532 = PN532_SPI(spi, cs_pin, debug=False)

#Configure nfc read for MiFare
pn532.SAM_configuration()

NumChessPiece = 31



PiecePosition = ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1",
                 "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
                 "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",
                 "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"]

uidList = []

PieceUID = {}



# while len(PieceUID) <= NumChessPiece:
#     print(str(len(PieceUID))+ " " + str(uid) + " " + str(uidList))
#     uid = pn532.read_passive_target(timeout=0.5)
#     if uid is not None:
#         redundant = False
#         for i in range(0, len(uidList)):
#             if uid == uidList[i]:
#                 redundant = True
#         if not redundant:
#             PieceUID[PiecePosition[PieceCounter]] = uid
#             uidList.append(uid)
#             PieceCounter = PieceCounter + 1
#             sleep(1)
#
# print(PieceUID)

PieceCounter =0
while len(PieceUID) <= NumChessPiece:
    uid = pn532.read_passive_target(timeout=0.5)
    if uid is not None and uid not in uidList:
        PieceUID[PiecePosition[PieceCounter]] = uid
        uidList.append(uid)
        PieceCounter = PieceCounter + 1
    print(str(len(PieceUID)) + " " + str(uid) + " " + str(uidList))

print(PieceUID)



