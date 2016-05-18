#!/usr/bin/env python2
"""
Given an integer N followed by N email address, print a list
containing only valid email addresses in lexicographical order.

Rules for valid emails:
    1. Must have the format:  username@website.ext
    2. username can only contain letters, digits, dashes and underscores
        ""
    3. website name can only have letters and digits
    4. maximum length of extension is 3
"""
from sys import stdin, stdout
import re
r = stdin.readline

def is_valid_email( string ):
    valid_pattern = "^[a-zA-Z0-9-_]{1,}@[a-zA-Z0-9]{,}\.[a-z]{,3}$"
    validQ = bool( re.search( valid_pattern, string  ))
    assert type(validQ) is bool
    return validQ

def main():
    valid_emails = []

    num_cases = int( r().strip() )
    for email in range( num_cases ):
        email = r().strip()
        email_is_valid = is_valid_email( email )
        if email_is_valid:
            valid_emails.append( email )


    valid_emails.sort()
    stdout.write( str(valid_emails) )



if __name__ == '__main__':
    main()
