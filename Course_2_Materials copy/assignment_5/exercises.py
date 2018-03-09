import math

#def to_fahrenheit(degrees_celsius):
#    return degrees_celsius


#def to_celsius(degrees_fahrenheit):
#    return degrees_fahrenheit


def to_fahrenheit(degrees_celcius):
	output = degrees_celcius * (9 / 5) + 32
	return output 


def to_celcius(degrees_fahrenheit):
	output = (degrees_fahrenheit - 32) * (5 / 9)
	return output

print(to_fahrenheit(0))
print(to_fahrenheit(50))
print(to_fahrenheit(100))
print(to_fahrenheit(150))
print(to_celcius(32))


#height = 1/2 a * t^2

def vertical_height(time_elapsed):
        return ((1/2) * (9.8) * time_elapsed * time_elapsed)

print(vertical_height(3)) 
print(vertical_height(10))


#fall_time = root(2h/a) 

def get_fall_time(height):
        return math.sqrt((2 * height) / (9.8))

print(get_fall_time(20))


#range= v(x) * t
#delta_x = Htower - Htarget
#delta_y = Dtarget - Dtower

def is_vulnerable(tower_height, tower_x, tower_y, target_x, target_y):
        muzzle_velocity = 300
        time_in_air = math.sqrt((2 * tower_height) / (9.8))
	
	tower_range = muzzle_velocity * time_in_air
        delta_x = tower_x - tower_y
        delta_y = target_y - target_x

        separation = math.sqrt(delta_x * delta_y)
        if separation < tower_range:
                print("The target is closer than the tower range, decrease range")
                return False
        else:
                print("The target is further than the tower range, increase range")
                return False

print(is_vulnerable(100, 20, 3, 3, 10))
print(is_vulnerable(10, 100, 10, 0, 130050))
print(is_vulnerable(1,1,1,1001,300))



