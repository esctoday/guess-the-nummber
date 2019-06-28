import random
start = input('start nummber:')
start = int(start)
end = input('end nummber：')
end = int(end)
r = random.randint(start,end)
count = 0
while True:
	count += 1  # count = count + 1
	num = input('guess the nummber:')
	num = int(num)
	if num == r:
		print('u so fking clever')
		print('this is the', count, 'time u guess.')
		break
	elif num > r:
		print('the nummber is too big')
	elif num < r:
		print('the nummber is too small')
	print('this is the', count, 'time u guess.')
