import sys
from argparse import ArgumentParser
import math
from wand.image import Image as Img
import Image

class AnswerRemover():

	def __init__(self, infile, outfile, threshold):
		print infile
		with Img(filename=infile, resolution=1000000) as image:
			image.compression_quality = 100
			image.save(filename="temp.png")
		self.img = Image.open("temp.png").convert("RGBA")
		self.outfile = outfile
		self.threshold = threshold
		self.black = (0, 0, 0)
		self.data = self.img.getdata()

	def isBlack(self, rgb):
		return self.distance(rgb, self.black) < self.threshold


	def distance(self, first, second):
		ret = 0
		for index in range(len(first)):
			ret += pow(first[index] - second[index], 2)
		return math.sqrt(ret)

	def processImage(self):
		print "Processing..."

		newData = []
		for item in self.data:
			if not self.isBlack(item[:3]):
				newData.append((255, 255, 255, 255))
			else:
				newData.append(item)
		self.img.putdata(newData)

	def saveImage(self):
		self.img.save(self.outfile, "PNG")

if __name__ == "__main__":
	parser = ArgumentParser(description="Removes all red from image")
	parser.add_argument('-i', '--infile', nargs='?', type=str, help='input file, in PDF format')
	parser.add_argument('-o', '--outfile', nargs='?', type=str, default='out.png', help='output file, in PDF format')

	args = parser.parse_args()
	answer_remover = AnswerRemover(args.infile, args.outfile, 100)
	answer_remover.processImage()
	answer_remover.saveImage()

