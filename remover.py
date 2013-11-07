
import math
import Image

img = Image.open("ee126.png")
img = img.convert("RGBA")
print img.getcolors()
datas = img.getdata()
red = (255, 0, 0)
threshold = 250

def distance(first, second):
	ret = 0
	for index in range(len(first)):
		ret += pow(first[index] - second[index], 2)
	if first != (255, 255, 255):
		#print str(math.sqrt(ret)) + "  " + str(first)
		pass
	return math.sqrt(ret)

def isRed(rgb):
	return distance(rgb, red) < threshold


newData = []
for item in datas:
	if isRed(item[:3]):
		newData.append((255, 255, 255, 255))
	else:
		newData.append(item)

img.putdata(newData)
img.save("ee126-converted.png", "PNG")

if __name__ == "__main__":
	pass
	# do stuff
