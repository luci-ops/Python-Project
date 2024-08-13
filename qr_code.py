# Import QRCode from pyqrcode 
import pyqrcode
import png
from pyqrcode import QRCode 

code = "I love you Priya Baby \n From Himanshu"


# Generate QR code 
url = pyqrcode.create(code) 

# Create and save the svg file naming "myqr.svg" 
url.svg("myqr.svg", scale = 15) 

# Create and save the png file naming "myqr.png" 
url.png('myqr.png', scale = 10) 
