import random
r = random.randint(1,100)
while True:
	num = input('guess the nummber:')
	num = int(num)
	if num == r:
		print('u so fking clever')
		break
	elif num > r:
		print('the nummber is too big')
	elif num < r:
		print('the nummber is too small')
