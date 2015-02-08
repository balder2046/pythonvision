from PIL import Image
from pylab import *
pil_image = Image.open("8.jpg")
im = array(pil_image)
imshow(im)
print "click 3 points"
x = ginput(3)
print "you click", x
show()



