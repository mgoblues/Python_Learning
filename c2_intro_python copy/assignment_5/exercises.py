import math

#
#=================================
#
def to_fahrenheit(degrees_celsius):
    x = degrees_celsius * 1.8 + 32
    return x

def to_celsius(degrees_fahrenheit):
    x = (degrees_fahrenheit - 32 ) / 1.8
    return x

print "32 degrees F = ", to_celsius(32)
print "98.6 degrees F = ", to_celsius(98.6)
print "100 degrees C = ", to_fahrenheit(100)


#
#=================================
#
def get_fall_time(height):
    # gravity isn't going to change, units in m/(s^2)
    acceleration_by_gravity = 9.8

    # replace with logic of above equation

    time_elapsed = math.sqrt((2 * height) / acceleration_by_gravity )
    return time_elapsed

print "Time to fall from 30m = ", get_fall_time(30), " s"

#
#=================================
#
def isVulnerable(tower_height, tower_x, tower_y, target_x, target_y):
    muzzle_velocity = 300

    # update this line to calculate time_in_air using get_fall_time() function
    time_in_air = get_fall_time( tower_height )

    tower_range = time_in_air * muzzle_velocity

    delta_x = tower_x - target_x  # difference between tower_x and target_x
    delta_y = tower_y - target_y  # difference between tower_y and target_y

    separation = math.sqrt( delta_x**2 + delta_y**2)  # the x and y deltas form a triangle, find the hypotenuse
    if separation < tower_range:
        print("The target is closer than the tower range, time to move")
        return True
    else:
        print("The target is further than the tower range, take a nap")
        return False

# def isVulnerable(tower_height, tower_x, tower_y, target_x, target_y):
print "Tower test #1, Vulnerable? ", isVulnerable( 50, 0, 0, 200, 0 )
print "Tower test #1, Vulnerable? ", isVulnerable( 50, 0, 0, 400, 0 )
print "Tower test #1, Vulnerable? ", isVulnerable( 50, 0, 0, 1000, 0 )
