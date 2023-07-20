import qrcode

qr = qrcode.make('https://www.google.com')

qr.save('qrcode.png')
