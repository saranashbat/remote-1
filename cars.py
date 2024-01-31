import random

cars = ["Audi", "Toyota", "Kia", "Nissan", "Tesla"]

randomNum = random.randint(0, len(cars)-1)

print(cars[randomNum])

def modelYear():
	year = random.randint(2000, 2024)
	return year

print(modelYear())
