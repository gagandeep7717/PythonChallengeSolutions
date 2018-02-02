#http://www.pythonchallenge.com/pc/def/map.html

pc2Hint = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

listHint = list(pc2Hint)

newList = []
for x in listHint:
	if 122 > ord(x) < 97:
		newList.append(x)
	else:
		asciiChar = ord(x) + 2
		if asciiChar > 122:
			asciiChar =  asciiChar - 122 - 1 + 97

		newList.append(chr(asciiChar))

print(''.join(newList))

print("# USING str.maketrans()")
intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = str.maketrans(intab, outtab)

print(pc2Hint.translate(trantab))