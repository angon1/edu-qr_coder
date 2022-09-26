import pyqrcode
# import png
from pyzbar.pyzbar import decode
from PIL import Image


def qr_code_decode(*,qr_code_path:str):
    qr_code_decoded = decode(Image.open(qr_code_path))
    return qr_code_decoded[0].data.decode('ascii')


def generate_qr_code(*,link:str, filename:str) -> None:
    qr_code = pyqrcode.create(link)    
    qr_code.png(filename, scale=5)    


def main():
    link = "https://www.instagram.com/the.clever.programmer/"
    generate_qr_code(link=link, filename="qr_code.png")
    qr_code_decode(qr_code_path="qr_code.png")

if __name__ == "__main__":
    main()