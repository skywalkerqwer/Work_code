import qrcode

# 生成二维码
text = 'Hello world'
img = qrcode.make(text)
img.save('QR-code.png')
