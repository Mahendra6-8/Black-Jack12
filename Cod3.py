
		# Push
		elif dealer_hand.calc_val == player_hand.calc_val():
			result = 'Tied up, push!' + restart_phrase
			playing = False

		# Dealer beats player
		else:
			result = 'Dealer Wins! ' + restart_phrase
			chip_pool -= bet
			playing = False

	game_step()

# Function to print results and ask user for next step

def game_step():
	'''Function to print game step/status on output'''

	# Display Player Hand
	print ""
	print ('Player Hand is: '),player_hand.draw(hidden = False)

	print ''
	print 'Player hand total is: ' +str(player_hand.calc_val())

	# Display Dealer Hand
	print ''
	print('Dealer Hand is: '), dealer_hand.draw(hidden = True)

	# If game round is over
	if playing == False:
		print " --- for a total of " + str(dealer_hand.calc_val())
		print "Chip Total: " +str(chip_pool)

	# Otherwise, don't know the second card yet
	else:
		print " with another card hidden upside down"

	# Print result of hit or stand
	print ''
	print result

	player_input()


# Function to exit the game

def game_exit():
	print 'Thanks for playing!'
	exit()

# Function to read user input

def player_input():
	'''Read user input, lower case it jsuts to be safe'''

	plin = raw_input().lower()

	if plin == 'h':
		hit()
	elif plin == 's':
		stand()
	elif plin == 'd':
		deal_cards()
	elif plin == 'q':
		game_exit()
	else:
		print "Invalid Input. Enter h, s, d, or q: "
		player_input()

# Intro to game

def intro():
	statement = '''Welcome to BlackJack! Get as close to 21 as you can without getting over! 
Dealer hits until she reaches 17. Aces count as 1 or 11. Card output goes a letter followed by a number of face notation. '''

	print statement
	print ''

# Playing the Game

'''The following code will initiate the game! 
(Note: Need to Run a 11 Cells)'''

# Create a Deck
deck = Deck()

# Shuffle it
deck.shuffle()

# Create player and dealer hands
print ''
player_hand = Hand()
print ''
deal_hand = Hand()

# Print the intro
intro()

# Deal out the cards and start the game!
deal_cards()
