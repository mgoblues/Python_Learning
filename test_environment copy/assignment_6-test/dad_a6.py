#!/usr/local/bin/python3

import sys
import pdb
import random
import math

def get_random_direction():
    direction = ""
    probability = random.random()

    if probability < 0.25:
        direction = "north"
    elif probability < 0.5:
        direction = "west"
    elif probability < 0.75:
        direction = "south"
    else:
        direction = "east"

    return direction


#for i in range(0,20):
#    print( get_random_direction() )

def get_direction_displacement(dir_key):
    displacements = {
        'west': (-1, 0),
        'east': (1, 0),
        'north': (0, 1),
        'south': (0, -1)
        }

    # access the dictionary
    # UPDATE HERE: how do you use the key to access a dictionary?
    # replace None with the answer
    return displacements[dir_key]

def take_walk(steps):
    current_location = [0, 0]
    for step_index in range(steps):
        direction = get_random_direction()

        displacement = get_direction_displacement(direction)

        # extract the numerical values from the tuple
        delta_x = displacement[0]
        delta_y = displacement[1]

        # UPDATE current_location HERE
        current_location[0] += delta_x
        current_location[1] += delta_y

    return current_location

def take_all_walks(steps, runs):
    endpoints = []
    total_d = 0
    for run_index in range(runs):
        end_location = take_walk(steps)
        endpoints.append(end_location)
        dx = end_location[0]
        dy = end_location[1]
        total_d += math.sqrt(dx*dx + dy*dy)

#    print( "AFD: ", total_d/runs )         # This works but is currently turned off
    return endpoints

def average_final_distance(endpoints):
    total_distance = 0
    for coords in endpoints:
        dx = coords[0]
        dy = coords[1]

        # use the Pythagorean theorem to get distance like last session
        distance = math.sqrt(dx*dx + dy*dy)

        total_distance += distance

    return total_distance / len(endpoints)

# at end of __main__ code add these lines to see if it worked
# mind the indentation, should be 4 spaces in front
    average_displacement = average_final_distance(end_locations)
    print(average_displacement)

#pdb.set_trace()

if __name__ == "__main__":
    steps = 10
    if len(sys.argv) > 1:
        steps = int(sys.argv[1])

    runs = 1
    if len(sys.argv) > 2:
        runs = int(sys.argv[2])

    current_location = take_walk(steps)        
    print("Done with walk of", steps, "steps, printing end location: ")
    print(current_location)

    end_locations = take_all_walks( steps, runs )
    print(end_locations)

    print("Average final distance: ",average_final_distance(end_locations))
