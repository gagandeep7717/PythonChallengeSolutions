# http://www.pythonchallenge.com/pc/def/oxygen.html

import requests
from io import BytesIO
from PIL import Image

img_file = Image.open(BytesIO(requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png').content))
# img_file = Image.open('oxygen.png')

img = img_file.load()
#img.show()


[xs, ys] = img_file.size

print [xs, ys]


row = []

for x in range(0, xs):
		row.append(img_file.getpixel((x, ys / 2)))


grayscale = []

ord = []
for tuple in row:
	if tuple[0] == tuple[1] == tuple[2]:
		grayscale.append(tuple)
grayscale.pop(-1)

print len(grayscale)
str = ''
for i in range(0, len(grayscale)-1):
		str += chr(grayscale[i][0])



print str

ords = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for i in ords:
	print(chr(i)),
