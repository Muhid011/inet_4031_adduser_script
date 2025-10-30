#!/usr/bin/python3

# INET4031
# Muhid011
# Date Created: 10/25/2025
# Date Last Modified: 10/27/2025

# Import modules:
# os – runs system commands
# re – checks for comment lines
# sys – reads input from a file
import os
import re
import sys

def main():
    for line in sys.stdin:
        # Skip lines that start with '#' (comments)
        match = re.match("^#", line)

        # Split the line by ':' into parts
        fields = line.strip().split(':')

        # Skip if it's a comment or missing fields
        if match or len(fields) != 5:
            continue

        # Get user info
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])  # Full name format

        # Get group list
        groups = fields[4].split(',')

        # Show message for creating user
        print("==> Creating account for %s..." % (username))

        # Command to create user
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # Run this line to create user
        # os.system(cmd)

        # Show message for setting password
        print("==> Setting the password for %s..." % (username))

        # Command to set password
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # Run this line to set password
        # os.system(cmd)

        # Add user to groups
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                # Run this line to add user to group
                # os.system(cmd)

if __name__ == '__main__':
    main()
