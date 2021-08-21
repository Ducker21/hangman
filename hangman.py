import random
def hangman(word):
	wrong = 0
	stages = [" ",
		  "__________	",
		  "|	 | 	",
		  "|	 |	",
		  "|	 0	",
		  "|	<|>	",
		  "|	< >	",
		  "|		"]
	rletters = list(word)
	board = ["_"] * len(word)
	win = False
	print("ハングマンへようこそ!")
	while wrong < len(stages) - 1:
		print("\n")
		msg = "1文字予想してね"
		char = input(msg)
		if char in rletters:
			cind = rletters.index(char)
			board[cind] = char
			rletters[cind] = '$'
		else:
			wrong += 1
		print(" ".join(board))
		e = wrong + 1
		print("\n".join(stages[0:e]))
		if "_" not in board:
			print("あなたの勝ち!")
			print(board)
			win = True
			break
	if not win:
		print("あなたの負け!")
		print("正解は{}".format(word))


animal = ["cat", "dog", "monkey", "fish"]
num = random.randint(0, len(animal)-1)
hangman(animal[num])

