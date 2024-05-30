import math

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_diameter(self) -> float:  # d = 2r
        return self.radius * 2

    def calculate_circumference(self) -> float:  # C = 2pi*r
        return self.radius * 2 * math.pi

    def calculate_area(self) -> float:  # A = pi*r^2
        return math.pi * self.radius * self.radius

    def grow(self):
        self.radius *= 2

    def get_radius(self) -> float:
        return self.radius

    def __str__(self) -> str:
        return f'Radius: {self.radius}; Diameter: {self.calculate_diameter()}; Circumference: {self.calculate_circumference()}; Area: {self.calculate_area()}'

def validate_radius(input_value: str) -> float:
    try:
        radius = float(input_value)
        if radius > 0:
            return radius
        else:
            print("The radius must be a positive number.")
            return None
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None

while True:
    radius_input = input('Welcome to the circle tester! Please enter the radius of the circle: ')
    radius = validate_radius(radius_input)
    if radius is not None:
        break

circle = Circle(radius)

while True:
    print(f'\n{circle}')

    grow_input = input('Do you want the circle to grow? (yes/no): ').strip().lower()
    if grow_input == 'yes':
        circle.grow()
    elif grow_input == 'no':
        print(f'Goodbye! The final radius is {circle.get_radius()}.')
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


