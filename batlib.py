from random import randint

def random():
	return randint(1,5)

def createmap():
	row0 = ['0','1','2','3','4','5']
	row1 = ['1','O','O','O','O','O']
	row2 = ['2','O','O','O','O','O']
	row3 = ['3','O','O','O','O','O']
	row4 = ['4','O','O','O','O','O']
	row5 = ['5','O','O','O','O','O']
	map = [row0,row1,row2,row3,row4,row5]
	return map

def clear(space):
	for i in range(space):
		print('')

def again():
	answer = raw_input("Would you like to play again? y / n ")
	if answer.lower() == 'y' or answer.lower == 'yes':
		return True
	else:
		return False


##### FILE IN / OUT

def gettotal():
	stats = open("total.txt","r")
	total = stats.read()
	stats.close()
	return total
def getwin():
	stats = open("win.txt","r")
	win = stats.read()
	stats.close()
	return win

def updatestats(booln,total,win):
	#if the player wins set booln = True
	total = int(total)
	win = int(win)
	winfile = open("win.txt","w")
	totalfile = open("total.txt","w")
	if booln == True:
		winfile.write(str(win + 1))
		totalfile.write(str(total+1))
	else:
		totalfile.write(str(total+1))
		winfile.write(str(win))
	winfile.close()
	totalfile.close()

def printstats():
	totalfile = open("total.txt","r")
	winfile = open("win.txt","r")
	total = totalfile.read()
	win = winfile.read()
	loss = int(total)-int(win)
	winloss = float(win) / float(loss)
	print 'You have played a total of %s games with %s wins and %s losses' % (total,win,loss)
	print 'Your win : loss ratio is %s' % (winloss)
	totalfile.close()
	winfile.close()