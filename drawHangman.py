def hangman_parts(trial):
	if trial == 0:
		print("""\t  _________
\t  |
\t  |""")
	if trial == 1:
		print("\t  O")
	if trial == 2:
		print("\t \|/")
	if trial == 3:
		print("\t  |")
	if trial == 4:
		print("\t / \\")

def hangman(trials):
	for i in range(0,trials):
		hangman_parts(i)
