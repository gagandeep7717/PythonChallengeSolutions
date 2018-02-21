# http://www.pythonchallenge.com/pc/def/ocr.html
import string
def ocr():
	result = ""
	f = open("pc2.txt", "r")
	for line in f.readlines():
		for x in line:
			if 97 <= ord(x) <= 122:
				result = result + x
	f.close()
	print(result)
	#except Exception:
	#	print("Unable to open file")

ocr()


## USING MAKETRANS
ocrtext = open("pc2.txt").read()


tr = str.maketrans("","", string.punctuation)

print(ocrtext.translate(tr))