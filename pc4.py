#http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345

import urllib2
import math

url = []
url.append("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")

def linkedlist():
		tempurl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={x}"
		
		for i in range(1,399):
			request= urllib2.Request(url[-1])
			response = urllib2.urlopen(request)
			for line in response:
				line = line.decode('utf-8')
				nothing = line.split(' ')[-1]
				#print("nothing: ",nothing)
				newurl = tempurl.replace("{x}", nothing)
				#print("NEW URL - ", newurl)
				url.append(newurl)

				try:
					int(nothing)
				except:
					print(url[-1])
					break



linkedlist()
