# Ask the user to enter the radius of the circle
radius = float(input("What is the radius of the circle? "))

# Calculate the diameter of the circle
diameter = 2 * radius

# Calculate the circumference of the circle
circumference = 2 * 3.14 * radius

# Calculate the area of the circle
area = 3.14 * radius ** 2

# Print the final message to the user
print("A circle with a radius of " + str(radius) + " units will have a diameter of " + str(diameter) + " units, a circumference of " + str(circumference) + " units, and an area of " + str(area) + " square units.")
