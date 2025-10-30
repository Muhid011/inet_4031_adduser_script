#!/usr/bin/python3

# INET4031 – Interactive Dry Run Script
# Author: Hamza Muhidin
# Date Created: Oct/25/2025
# Last Modified: Oc/27/20225

# os – runs Linux system commands
# re – checks for comment lines using regular expressions
# sys – reads input file line by line from standard input
import os
import re
import sys

# Prompt user to choose dry-run mode
dry_run = input("Run in dry-run mode? (Y/N): ").strip().upper() == "Y"

def main():
    for line in sys.stdin:
        # Skip lines that start with '#' (comments)
        match = re.match("^#", line)

        # Split line into fields using ':' delimiter
        fields = line.strip().split(':')

        # Skip line if it's a comment or doesn't have exactly 5 fields
        if match or len(fields) != 5:
            if dry_run:
                print("[Dry Run] Skipping line due to comment or incorrect format.")
            continue

        # Extract user details
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])  # Format: First Last,,,

        # Split group field into list of groups
        groups = fields[4].split(',')

        # Notify account creation
        print(f"==> Creating account for {username}...")
        cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
        if dry_run:
            print(f"[Dry Run] Would run: {cmd}")
        else:
            os.system(cmd)

        # Notify password setup
        print(f"==> Setting the password for {username}...")
        cmd = f"/bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"
        if dry_run:
            print(f"[Dry Run] Would run: {cmd}")
        else:
            os.system(cmd)

        # Assign user to groups if applicable
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
