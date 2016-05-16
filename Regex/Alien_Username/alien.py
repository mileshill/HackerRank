#!/usr/bin/env python2
"""
-Validation of alien usernames-
Build a regex pattern to match the listed conditions.
1.It must begin with an underscore or dot
        "^[_.]"
2.Followed by ONE or MORE occurrences of positive digits:
        "[0-9]{1,}"
3.Letters (upper or lower case) ZERO or more:
        "[a-zA-Z]*"
4.End with an optional underscore:
        "[_]{0,1}$"
"""
# imports
from sys import stdin, stdout
import re
r = stdin.readline

def validate( uname ):
    """ Returns boolean value for username verification """
    assert type(uname) is str

    regex_pattern = "^[_.][0-9]{1,}[a-zA-Z]*[_]{0,1}$"
    is_valid = bool(re.search( regex_pattern, uname ))

    assert type( is_valid ) is bool
    return is_valid

def main():
    num_lines = int( r() ) # number of test cases

    for line in range( num_lines ):
        is_valid = validate( r().strip() )

        if is_valid:
            stdout.write("VALID\n")
        else:
            stdout.write("INVALID\n")

if __name__ == '__main__':
    main()

