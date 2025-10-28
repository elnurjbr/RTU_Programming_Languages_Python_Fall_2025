# TODO: import math
import math

def circle_area(radius):
    """Return the area of a circle given its radius."""
    # TODO: implement formula using math.pi
    return math.pi * radius ** 2

if __name__ == "__main__":
    # TODO: ask for user input, call circle_area(), and print formatted result
    r = float(input("Enter radius: "))
    result = circle_area(r)
    print(f"Area of the circle: {result:.2f}")
