import drawHangman
import time
from time import sleep
import random


#These are the key words:
keys = ["nepal" ,"facebook","skype","bhaktapur", "about", "education", "handsome", "country"]
heart = 5
trys = ""
cans = []
wans = ""
number = "1234567890-=+/.,"
score = 0
trial =1 
man = ""



question = random.choice(keys)
#question = "aabbccde"
q_len = len(question)

arr = []
arr.append('-'*len(question))
print("\n")
print(arr)

#print("_ "*q_len)
#Display the question:
for i in arr:
	for h in i:
		cans.append(h)

#Put some initial guess;
ran1 = random.randint(1,3)
for i in range(0,ran1):
	ran = random.randint(0,q_len-1)
	cans[ran] = question[ran]



print("Our question have {} words".format(q_len))

print("Our Word:" ,' '.join(cans))

while True:
	print("\nNewConsole")
	print('*'*40)
	if len(trys) ==  len(question):
		print("You won! Word: {} Your score: {}".format(question, score))
		print("Please press 'Enter' to quit..")
		break
	if heart == 0:
		print("\n You loose...")
		sleep(0.9)
		print("Your Score is {}".format(score))
		sleep(0.9)
		print("The word you could not answer is: {}".format(question))
		sleep(0.9)
		print("please press 'Enter' to quit..")
		break
	

	x = input("\n Please enter a letter: ")
	sleep(0.9)
	if 1 <len(x):
		print("\n You can enter only 1 letter")
		continue
	if x in number:
		print("\n Its not even a letter")
		continue
	if x in trys:
		print("\n You used this letter")
		continue
	if x in question:
		for i in range(0,len(question)):
			if x  == question[i]:
				#index = question.index(x)
				cans[i] = x
				score += 25
				trys += x
				#continue

			



	
		print("In line {} .", ' '.join(cans))
	else:
		wans += x
		heart -= 1
		print("\n This letter {} is not in our world! {} heart left".format(x, heart))
		sleep(0.7)
		drawHangman.hangman(trial)
		trial += 1

	print('*'*20)

					

try:
	input()
except SyntaxError:
	pass


#print(question)
