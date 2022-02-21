import qrcode 

with open('dfw.txt') as f:
    data = f.read()

img = qrcode.make(data)
img.save('QR_code.png')   