# ConeVolumeCalculator.py
# Your job is to write a function in ConeVolumeCalculator.py (call
# it **calculateConeVolume()** that calculates the volume of a cone
# factor based on the Volume Calculator
# Calculator.net (http://www.calculator.net/volume-calculator.html)

# Define Function below
# be sure to return an integer

from math import pi

def calculateConeVolume(baseRadius, height):
    area = (1/3) * pi * (baseRadius ** 2) * height
    area = round(area, 2)
    return area


if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    pass # remove or comment out this line if you wish to test the function



