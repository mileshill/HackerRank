#!/usr/bin/evn python2
"""
Provided with N lines of possible IP address. Detect if
1. IPv4
2. IPv6
3. Neither

IPv4: A.B.C.D where, ABCD are integers in the range [0,255]

IPv6: 8 groups of 16 bit each. Each group is written as 4 hexadecimal degits and separated by colors.
Consecutive sections of zeros are not expanded.
    "...:0:... => ...:0000:..."
    "...:5:... => ...:0005:..."
"""
# imports
from sys import stdin, stdout
import re
r = stdin.readline

def is_IPv4( string ):
    """ Test for IPv4 address"""
    ipv4_pattern = "^[0-9]|1[0-9]{,2}|2[0-5]{,2}[:]*"
    ipv4 = bool( re.search( ipv4_pattern, string  ))
    assert type(ipv4) is bool
    return ipv4

def is_IPv6( string):
    """ Test for IPv6 address"""
    return False

def main():
    num_cases = int( r().strip() )

    for case in range( num_cases ):
        case = r().strip()
        if is_IPv4( case  ):
            stdout.write("IPv4\n")

        elif is_IPv6( case ):
            stdout.write("IPv6\n")

        else:
            stdout.write("Neither\n")


if __name__ == '__main__':
    main()

