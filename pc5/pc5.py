#http://www.pythonchallenge.com/pc/def/peak.html

import pickle

str = ''

unpickledText = pickle.load(open("banner.p", "r"))

f = open("pc5answer.txt", "w")
#print(unpickledText)
for tuple in unpickledText:
	#print("tuple: ", tuple)
	str = ''
	for tuple2 in tuple:
		for i in range(1, tuple2[1]+1):
			str = str + tuple2[0]
	print(str)
	f.write(str + "\n")

f.close()

print(len("                                                                                                           "))