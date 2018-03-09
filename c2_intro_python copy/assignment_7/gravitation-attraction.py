#!/usr/local/bin/python3

import math

# F ( in Newtons ) = G * m1 * m2 / d2 where
#
#  G = universal gravitation constant = 6.673 x 10**-11 Nm2/kg*
#

def gravitation_attraction( m1, m2, d ):
    G = 6.673e-11
    return G * m1 * m2 / d**2

#Sample Problem #1

#Determine the force of gravitational attraction between the earth (m = 5.98 x 1024 kg) and a 70-kg physics student if the student is standing at sea level, a distance of 6.38 x 106 m from earth's center.

mass_earth = 5.98e24
mass_student = 70
distance = 6.38e6

print( "Force due to gravity:", gravitation_attraction( mass_earth, mass_student, distance ) )
