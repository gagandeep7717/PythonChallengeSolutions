#http://www.pythonchallenge.com/pc/def/channel.html

'''
f = open("channel/readme.txt", "r")
for line in f:
	print(line)
f.close()
'''

import zipfile
infoList = {}
chainList = []

def print_info(archive_name):
	zf = zipfile.ZipFile(archive_name)
	for info in zf.infolist():
		infoList[info.filename] = info.comment
	#print(infoList)
	#for list in infoList:
	#	print(list) 

print_info('channel.zip')

def chain(filename):
	fileuri = "channel/{x}.txt"
	openURI = fileuri.replace('{x}', filename)
	#print(openURI)
	f = open(openURI, "r")
	filetext = f.readlines()[0]
	f.close()
	#print(filetext)
	text = filetext.split(' ')
	nothing = text[-1]
	chainList.append(nothing)
	#print(nothing)
	try:
		chain(nothing)
	except:
		#print(chainList)
		return 1

chainList.append('90052')
chain("90052")

def collectComments():
	comment = ""
	for file in chainList:
		try:
			filename = file+".txt"
			comment = comment + infoList[filename]
		except:
			print("End of List")
	print(comment)

collectComments()

