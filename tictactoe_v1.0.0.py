import random

# Board layout
layout = [
	[' ', '|', ' ', '|', ' '],
	['-', '+', '-', '+', '-'],
	[' ', '|', ' ', '|', ' '],
	['-', '+', '-', '+', '-'],
	[' ', '|', ' ', '|', ' ']
]

# Winning combinations
win = [
	[1, 2, 3], [4, 5, 6], [7, 8, 9],
	[1, 4, 7], [2, 5, 8], [3, 6, 9],
	[1, 5, 9], [3, 5, 7]
]

choice_list = []
playerchoice_list = []
computerchoice_list = []

def print_board():
	for row in layout:
		print(' '.join(row))
	print()

def place_move(choice, symbol, choice_list_ref):
	"""Place a move on the board based on choice (1–9)."""
	# Convert choice (1–9) into row/col in layout
	row_index = (choice - 1) // 3 * 2   # 0, 2, 4
	col_index = ((choice - 1) % 3) * 2  # 0, 2, 4
	layout[row_index][col_index] = symbol
	choice_list.append(choice)
	choice_list_ref.append(choice)

def check_winner():
	for combo in win:
		if all(v in playerchoice_list for v in combo):
			print("Player wins!")
			return True
		if all(v in computerchoice_list for v in combo):
			print("Computer wins!")
			return True
	return False

# Game loop
print_board()
while len(choice_list) < 9:
	# Player move
	try:
		playerchoice = int(input("Enter your move (1-9): "))
	except ValueError:
		print("Invalid input. Please enter a number between 1 and 9.")
		continue

	if playerchoice not in range(1, 10):
		print("Invalid choice. Pick between 1 and 9.")
		continue
	if playerchoice in choice_list:
		print("ERROR: Spot already taken.")
		continue

	place_move(playerchoice, 'X', playerchoice_list)
	print_board()

	if check_winner():
		break

	if len(choice_list) == 9:
		print("It's a draw!")
		break

	# Computer move
	while True:
		computerchoice = random.randint(1, 9)
		if computerchoice not in choice_list:
			place_move(computerchoice, 'O', computerchoice_list)
			print("Computer chose:", computerchoice)
			print_board()
			break

	if check_winner():
		break

