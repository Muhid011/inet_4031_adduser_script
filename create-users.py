#!/usr/bin/python3

# INET4031
# Muhid011
# Date Created: Oct 25
# Date Last Modified: Oct 27

# Import required modules:
# os – allows execution of system-level commands
# re – used for regular expression matching
# sys – provides access to system input/output
import os
import re
import sys

def main():
    for line in sys.stdin:
        # Skip lines that start with '#' (used for comments in input file)
        match = re.match("^#", line)

        # Split the line into fields using ':' as the delimiter
        fields = line.strip().split(':')

        # Skip the line if it's a comment or doesn't contain exactly 5 fields
        if match or len(fields) != 5:
            continue

        # Extract user details from the fields
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])  # Format: Full Name, Room Number, etc.

        # Split group field into a list of groups
        groups = fields[4].split(',')

        # Notify that account creation is starting
        print("==> Creating account for %s..." % (username))

        # Build the command to create the user with no password and GECOS info
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # Uncomment the line below to actually create the user
        # os.system(cmd)

        # Notify that password is being set
        print("==> Setting the password for %s..." % (username))

        # Build the command to set the user's password using echo and passwd
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # Uncomment the line below to actually set the password
        # os.system(cmd)

        # Assign user to specified groups (if not '-')
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                # Uncomment the line below to actually add the user to the group
                # os.system(cmd)

if __name__ == '__main__':
    main()
