import sys
from argparse import ArgumentParser
import math
import Image

class AnswerRemover():

	def __init__(self, infile, outfile, threshold):
		self.img = Image.open(infile).convert("RGBA")
		self.outfile = outfile
		self.threshold = threshold
		self.red = (255, 0, 0)
		self.data = self.img.getdata()

	def isRed(self, rgb):
		return self.distance(rgb, self.red) < self.threshold


	def distance(self, first, second):
		ret = 0
		for index in range(len(first)):
			ret += pow(first[index] - second[index], 2)
		if first != (255, 255, 255):
			#print str(math.sqrt(ret)) + "  " + str(first)
			pass
		return math.sqrt(ret)

	def processImage(self):
		print "Processing..."
		newData = []
		for item in self.data:
			if self.isRed(item[:3]):
				newData.append((255, 255, 255, 255))
			else:
				newData.append(item)
		self.img.putdata(newData)

	def saveImage(self):
		self.img.save(self.outfile, "PNG")

if __name__ == "__main__":
	parser = ArgumentParser(description="Removes all red from image")
	parser.add_argument('-i', '--infile', nargs='?', type=str, help='input file, in PNG format')
	parser.add_argument('-o', '--outfile', nargs='?', type=str, default='out.png', help='output file, in PNG format')

	args = parser.parse_args()
	answer_remover = AnswerRemover(args.infile, args.outfile, 250)
	answer_remover.processImage()
	answer_remover.saveImage()

