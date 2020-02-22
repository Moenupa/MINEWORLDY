car_brands = open('car_brands.txt')
cars = car_brands.readlines()
for car in cars:
	car=car.strip('\n')
	if car == 'bmw':
		print(car.upper())
	elif car == 'gmc':
		print(car.upper())
	elif car == 'mclaren':
		print('McLaren')
	else:
		print(car.title())