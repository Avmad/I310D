def compute_volume_of_sphere(radius):
	pi = 3.14 # value of pi
	volume = (4 / 3) * pi * radius * radius * radius # formula for volume of sphere
	return volume # return the volume of the sphere

radius1 = 30 # example radius1
volume1 = compute_volume_of_sphere(radius1) # calculate volume of sphere with radius1
print(f"The volume of sphere with radius {radius1} is: {volume1}") # example output for radius1

radius2 = 40 # example radius2
volume2 = compute_volume_of_sphere(radius2) # calculate volume of sphere with radius2
print(f"The volume of sphere with radius {radius2} is: {volume2}") # example output for radius2