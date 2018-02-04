# http://www.pythonchallenge.com/pc/def/equality.html

import re

# Solution Using REGEX
def pc3Regex():
	result = ""
	equalityText = open("pc3.txt").read()
	for m in re.finditer(r"[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]", equalityText):
		temp = m.group()	
		result = result + temp[int(len(temp)/2)]
	print("REGEX Solution - ", result)
		
pc3Regex()

# Traditional Solution
def equality():
	result = ''
	equalityText = open("pc3.txt").read()
	
	for i in range(0, len(equalityText)):
		if not isCaps(equalityText[i]):
			if i+1 < len(equalityText) and isCaps(equalityText[i+1]):
				if isCaps(equalityText[i+2]):
					if isCaps(equalityText[i+3]):
						if not isCaps(equalityText[i+4]):
							if isCaps(equalityText[i+5]):
								if isCaps(equalityText[i+6]):
									if isCaps(equalityText[i+7]):
										if not isCaps(equalityText[i+8]):
											#print(equalityText[i] + equalityText[i+1] + equalityText[i+2] + equalityText[i+3] + equalityText[i+4] + equalityText[i+5] + equalityText[i+6] + equalityText[i+7] + equalityText[i+8] )
											result = result + equalityText[i+4]
	print("Condition Tree (Simple Approach) - ", result)


def isCaps(x):
	caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	if x in caps:
		return True
	else:
		return False

equality()


#http://www.pythonchallenge.com/pc/def/linkedlist.php
  