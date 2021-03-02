import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.spi import PN532_SPI

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs_pin = DigitalInOut(board.D5)


pn532 = PN532_SPI(spi, cs_pin, debug=False)

#Configure nfc read for MiFare
pn532.SAM_configuration()

def scan_nfc():
    temp_uid = None
    while temp_uid is None:
        temp_uid = pn532.read_passive_target(timeout=0.5)
    return temp_uid

def find_uid(uid,piece_list):
    if piece_list is None:
        return False
    for i in range(0,len(piece_list)):
        if piece_list[i].uid == uid:
            return piece_list[i]
    return False