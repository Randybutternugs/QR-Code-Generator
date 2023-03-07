import qrcode
from colorama import Fore, Style
import os

#resize the terminal window
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=16, cols=50))

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


os.system('cls')
print(Style.RESET_ALL + Fore.GREEN + "\nEnter the text to be encoded in the QR code: " + Style.RESET_ALL + Fore.RED, end='')
input_text = input()
print(Style.RESET_ALL)

qr.add_data(input_text)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="red")

img.show()