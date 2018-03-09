import math

#def to_fahrenheit(degrees_celsius):
#    return degrees_celsius


#def to_celsius(degrees_fahrenheit):
#    return degrees_fahrenheit

def to_fahrenheit(degrees_celcius):
        '''Take temp in celcius and return in F'''
        new_f = degrees_celcius * (9 / 5) + 32
        return new_f 


def to_celcius(degrees_fahrenheit):
        '''Take temp in fahrenheit and return in C'''
        new_c = (degrees_fahrenheit - 32) * (5 / 9)
        return new_c

print((str(to_fahrenheit(0)) + " degrees F"))
print(to_fahrenheit(50))
print(to_fahrenheit(100))
print(to_fahrenheit(150))
print(to_celcius(32))

#Part 2: Physics problem
#need to solve:
#	y component of tower and target
#	x component of tower and target
#constants: 
#	gravity(acceleration) (9.8 m/s^2)
#equations:
#	range = V(ix) * time in air
#	time in air = root((2 * height)/acceleration)) 	
	

def vertical_height(time_elapsed):
	'''solve for height based on time elapsed using formula h = (1/2)at^2. a=acceleration= 9.8 m/s^2)'''
	height_of_tower = ((1/2) * (9.8) * time_elapsed**2 )
	return height_of_tower

print(vertical_height(3))
print(vertical_height(10))


def get_fall_time(height):
        '''Get fall time (elapsed) based on height when dropped'''
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



