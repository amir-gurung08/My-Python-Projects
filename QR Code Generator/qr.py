import qrcode
from PIL import Image

data = input("Enter text to Generate QR Code: ")
save = input("Enter the image name to save: ")
qr = qrcode.QRCode(version=3, box_size=8, border=4)
qr.add_data(data)
image = qr.make_image(fill= "black", back_color="Greenyellow")
filename = f"{save}.png"
image.save(filename)
Image.open(filename)

