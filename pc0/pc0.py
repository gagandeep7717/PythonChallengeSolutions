#http://www.pythonchallenge.com/pc/def/0.html

def powerof(n, i):
	ans	= 1
	for x in range(1,i+1):
		ans = ans * n
	return ans

print("For Loop: ", powerof(2,38))



#recursive approach

def recPower(n, i):
	if i == 0:
		return 1
	else:
		return n * recPower(n, i-1)

print("Recursion: ",recPower(2,38))



# replace 0 with 137438953472