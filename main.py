import batlib
import time

#Heart of the Game

def main():
        global turn,message,debug,map,shipcol,shiprow
	while turn > 0: #Loop until turns are gone
		batlib.clear(100)
		print "BATTLE SHIP"
		batlib.clear(2)
		if debug == True:
			print 'Coordinates are %s row and %s colum' % (shiprow,shipcol)


		print message#explains what happened
		for row in map: #This prints out the map on each line instead of all together
			print " ".join(row)
		batlib.clear(3)#3 lines of whitespace

		guessrow = input("Row     ")
		guesscol = input("Colum   ")

		#If they guess correctly
		if guessrow == shiprow and guesscol == shipcol:
			batlib.updatestats(True,batlib.gettotal(),batlib.getwin())
			print "Well done soldier! Direct hit."
			batlib.printstats()
			if batlib.again() == True:
				start()
			else:
				print 'At ease, soldier.'
				break


		#If they guess out of range
		elif guessrow not in range(1,6) or guesscol not in range(1,6):
			message =  "Those coordinates could harm civilians!"
			batlib.clear(1)
			turn -= 3

		#If they already hit a certain spot
		elif map[guesscol][guessrow] == "x":
			message = "Sir, we already tried that spot."
			batlib.clear(1)
			turn -= 2


		#If they miss
		else:
			message = "Sir, the missile failed to hit anything."
			batlib.clear(1)
			map[guesscol][guessrow] = "x"
			turn -= 1


	#If they run out of turns
	else:
		batlib.updatestats(False,batlib.gettotal(),batlib.getwin())
		print('')
		print('')
		print('')
		print "Game Over"
		print "The enemy has sunk you"
		batlib.printstats()
		if batlib.again() == True:
			start()
		else:
			print 'rage quit omg'

###


#Defining Variables and such
def start():
        global turn,map,debug,shipcol,shiprow,message
        message = ""
        shiprow = batlib.random()
        shipcol = batlib.random()
        debug = False
        map = batlib.createmap()
        turn = 5
       # global turn,map,debug,shipcol,shiprow,message
        main()
start()
