#!/usr/bin/env python2
"""
Bot Saves Princess:
    Mario is located at the center of the grid. Princess Peach is located at one of the four corners. Peach is denoted by 'p' and Mario by 'm'. The goal is to make the proper moves to reach the princess

    Input:
            First line contains an ODD integer (3<=N<=99) denoting the size of the grid. The is followed by an NxN grid. 

    Output:
            Print out the steps required to reach the princess. Each move will have the format "MOVE\n"

    Valid Moves:
            LEFT, RIGHT, UP, DOWN
"""
from sys import stdin, stdout
r = stdin.readline

def find_princess_position( grid_size ):
    """ Read the array to find princess """
    assert type( grid_size ) is int
    for i in range( grid_size ):
        line = list(r().strip())
        if 'p' in line:
            j = line.index('p') 
            location = (j,i)
    return location 

def get_directions( x_peach, y_peach, x_mario, y_mario):
    """ Determine L/R U/D directions mario will travel """
    horizontal_dir =''
    vertical_dir = ''
    # horizontal direction
    if x_peach > x_mario:
        horizontal_dir = "RIGHT"
    else:
        horizontal_dir = "LEFT"
    # vertical direction
    if y_peach > y_mario:
        vertical_dir = "DOWN"
    else:
        vertical_dir = "UP"

    return (horizontal_dir, vertical_dir)

def generate_marios_path( grid_size, location_of_princess ):
    """ Generate the steps to move to the princess """
    grid_center = (grid_size -1)/2 + 1 
    distance_to_wall = grid_center -1
    xp, yp = location_of_princess
    x_dir, y_dir = get_directions( xp, yp, xm, ym )
    
    horizontal = [ x_dir for x in range(distance_to_wall)]
    vertical = [ y_dir for y in range(distance_to_wall) ]

    return horizontal + vertical


def main():
    grid_size = int( r().strip() )

    location_of_princess =  find_princess_position( grid_size )
    marios_path = generate_marios_path( grid_size, location_of_princess )
    
    assert type( marios_path ) is list
    for move in marios_path:
        stdout.write( move + '\n' )

if __name__ == '__main__':
    main()

