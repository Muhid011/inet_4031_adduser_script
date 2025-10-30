#!/usr/bin/python3

# INET4031 – Interactive Dry Run Script
# Author: Hamza Muhidin
# Date Created: 10/25/2025
# Last Modified: 10/27/2025

# os – runs system commands
# re – checks for comment lines
# sys – reads input from a file
import os
import re
import sys

# Ask user if they want to do a dry run
dry_run = input("Run in dry-run mode? (Y/N): ").strip().upper() == "Y"

def main():
    for line in sys.stdin:
        # Skip lines that start with '#' (comments)
        match = re.match("^#", line)

        # Split the line by ':' into parts
        fields = line.strip().split(':')

        # Skip if it's a comment or missing fields
        if match or len(fields) != 5:
            if dry_run:
                print("[Dry Run] Skipping line due to comment or incorrect format.")
            continue

        # Get user info
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])  # Full name format

        # Get group list
        groups = fields[4].split(',')

        # Show message for creating user
        print(f"==> Creating account for {username}...")
        cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
        if dry_run:
            print(f"[Dry Run] Would run: {cmd}")
        else:
            os.system(cmd)

        # Show message for setting password
        print(f"==> Setting the password for {username}...")
        cmd = f"/bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"
        if dry_run:
            print(f"[Dry Run] Would run: {cmd}")
        else:
            os.system(cmd)

        # Add user to groups
        for group in groups:
            if group != '-':
                print(f"==> Assigning {username} to the {group} group...")
                cmd = f"/usr/sbin/adduser {username} {group}"
                if dry_run:
                    print(f"[Dry Run] Would run: {cmd}")
                else:
                    os.system(cmd)

if __name__ == '__main__':
    main()
