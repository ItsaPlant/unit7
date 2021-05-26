class Car:
    def __init__(self, make, model_name, top_speed, colour):
        self.make = make
        self.model_name = model_name
        self.top_speed = top_speed
        self.color = colour

        #var

        self._current_speed = 0

    
    def current_speed(self):
        return self._current_speed

    def accelerate(self, step=10):
        self._current_speed += step
    
    def decelerate(self, step=10):
        self._current_speed -= step

    def __str__(self):
        return f"{self.color} {self.make} {self.model_name}"

mustang = Car(make="Ford", model_name="Mustang", top_speed=250, colour="red")

print(mustang)
print(mustang.make)


class Truck(Car):
    def __init__(self, max_load, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_load = max_load

truck = Truck(make="Mercedes", model_name="Actros", colour="black", top_speed=90, max_load=1200)
print(truck)

truck.accelerate(30)



speed = truck.current_speed
print(speed)

print(isinstance(mustang, Truck))
print(isinstance(truck, Car))

print(issubclass(Car, Truck))
print(issubclass(Truck, Car))
