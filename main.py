class Car:
    def __init__(self, make, model_name, top_speed, color):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color
       # Variables
       self._current_speed = 0
    def __str__(self):
        return f'{self.color} {self.make} {self.model_name}'
    def __repr__(self):
        return f"Car(make={self.make} model={self.model_name}, top_speed={self.top_speed}, color={self.color})"
    def __eq__(self, other):
        return (
        self.make == other.make and
        self.model_name == other.model_name and
        self.top_speed == other.top_speed and
        self.color == other.color
        )
    @property
    def current_speed(self):
        return self._current_speed
    @current_speed.setter
    def current_speed(self, value):
        if value <= self.top_speed:
            self._current_speed = value
        else:
            raise ValueError(f"Value {value} exceeds top speed of {self.top_speed}")
    def accelerate(self, step=10):
        self.current_speed += step
    def decelerate(self, step=10):
        self.current_speed -= step
class Truck(Car):
   def __init__(self, max_load, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.max_load = max_load





truck = Truck(make="Mercedes", model_name="Actros", color="Black", top_speed=90, max_load=1200)
print(truck)

truck.accelerate(24)
print(truck.current_speed)

truck = Truck(make="Mercedes", model_name="Sprinter", color="Black", top_speed=90, max_load=1200)
car = Car(make="Ford", model_name="Mustang", top_speed=250, color="red")
print(isinstance(truck,Car))





"""
car = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
print(car)
car = Car(make="Ford", model_name="Mustang", top_speed=250, color="red")
print(car.current_speed)
car.current_speed = 200
print(car.current_speed)

car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
print(car_one == car_two)
"""