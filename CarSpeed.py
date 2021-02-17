import CarClass as c

Car = c.Car(2018, "Chevy")

Car.get_speed()

for i in range(5):
    Car.accelerate()
    Car.get_speed()

for i in range(5):
    Car.brake()
    Car.get_speed()