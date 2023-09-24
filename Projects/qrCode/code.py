import qrcode as qr

img = qr.make("https://www.geeksforgeeks.org/generate-qr-code-using-qrcode-in-python/")
img.save("test.png")