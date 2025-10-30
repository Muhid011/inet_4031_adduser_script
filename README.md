# INET4031 – Add Users Script

## Program Description

This program adds users and assigning them to groups on an Ubuntu system. Normally, a system administrator would have to manually run commands like "adduser", "passwd", and "usermod" for each person. That takes time and can lead to mistakes.

Instead, this script reads user information from a file and runs those commands for you. It’s really useful when setting up servers for teams like developers, especially when you need to add many accounts

## Program User Operation

This script reads each line from the input file and uses that data to create users, set their passwords, and add them to groups. You can run the script in two diffrent ways:
- **Dry run**: Shows what commands would run, but doesn’t make changes
- **Real run**: Actually creates users and updates the system


### Input File Format

Each line in the input file should look like this:

username:password:last_name:first_name:group1,group2

- **Username** – The login name
- **Password** – The account password
- **Last Name** – The user’s last name
- **First Name** – The user’s first name
- **Groups** – A list of groups (use `-` if none)
- Lines starting with `#` are skipped
- Lines with fewer than 5 fields are ignored
- If the group field is `-`, the user won’t be added to any groups

### Command Execution

Before running the script, make sure it is executable by using this command:
chmod +x create-users.py

Then run it like this:
./create-users.py < create-users.input

To actually create users, use this command:
sudo ./create-users.py < create-users.input

### Dry Run

When the script starts, it asks:
Run in dry-run mode? (Y/N):

- Type "Y" to test the script. It will print the commands but won’t run them.
- Type "N" to run the commands and create users for real.

Dry run mode helps you check your input file before making changes to the system.
