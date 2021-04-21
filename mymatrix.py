#!/usr/bin/env python3

# PIL Image module (create or load images) is explained here:
# http://effbot.org/imagingbook/image.htm
# PIL ImageDraw module (draw shapes to images) explained here:
# http://effbot.org/imagingbook/imagedraw.htm

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from time import sleep
from rgbmatrix import RGBMatrix, RGBMatrixOptions

class mymatrix(object):

	WHITE=(255,255,255)
	BLACK=(0,0,0)
	RED=(255,0,0)

	def __init__(self, rows=16, cols=32, chain_length=4, parallel=1, hardware_mapping='adafruit-hat-pwm'):
		self.options                    = RGBMatrixOptions()
		self.options.rows               = rows
		self.options.cols               = cols
		self.options.chain_length       = chain_length
		self.options.parallel           = parallel
		self.options.hardware_mapping   = hardware_mapping
		self.matrix                     = RGBMatrix(options = self.options)

	def clear(self):
		self.matrix.Clear()

	def settext(self, text, color=WHITE, w=0, h=0):
		# XXX: go back and figure out where we can set the font size
		textsize  = ImageDraw.Draw(Image.new("RGB", (1,1))).textsize(text)
		self.textimage = Image.new("RGB", textsize)
		self.draw = ImageDraw.Draw(self.textimage)
		self.draw.text( (w,h), text, color)

	def posttext(self,w=0,h=0):
		self.clear()
		self.matrix.SetImage(self.textimage, w, h)

	def scrolltext(self,zigzag=False):
		W,H = self.textimage.size
		print(W,H)
		h=0
		d=1
		for n in range(self.options.chain_length * self.options.cols, -W, -1):  # Start off top-left, zigzag to the left
			w=n
			self.matrix.Clear()
			self.posttext(w,h)
			yield w
			if zigzag: 
				#print(h)
				h+=d
			if h+H >= self.options.rows or h <= 0: 
				d = 0-d

if __name__ == "__main__":
	mm = mymatrix()
	mm.settext("Hello, world!")
	mm.posttext()
	sleep(3)
	mm.settext("Goodbye, world!")
	mm.posttext()
	sleep(3)
	mm.settext("swoop!")
	for w in mm.scrolltext():
		print(w)
		sleep(0.05)
