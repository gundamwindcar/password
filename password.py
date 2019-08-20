password = 'a123456'
n = 3
while n > 0: 
	enter = input ('Please enter your password:')
	if enter == password:
		print('Login Successfully!')
		break
	else:
		while True: 
			n = n - 1
			if n > 1:
				print('Incorrect password! You have',n ,'chances')
			elif n == 1:
				print('Incorrect password! You have',n ,'chance')
			break
if n == 0:
	print('Unable to Login')
