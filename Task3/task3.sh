#!/bin/bash

# Define the output file path
output_file="/c/Users/50004393/PycharmProjects/CW_2/Task3/print_commands.txt"

# Task 1: Find Print-Related Commands and Output to a Local File
compgen -c | grep -i print > "$output_file"

# Task 2: Append the Current Date and Time to the File
date >> "$output_file"

# Task 3: Close All Notepad Files
taskkill /F /IM notepad.exe

# Task 4: Append the Last 20 Errors from the Event Log to the File
wevtutil qe system /c:20 /f:text /q:"*[System[(Level=2)]]" >> "$output_file"

# Task 5: Append a List of All Available WMI Classes to the File
wmic /namespace:\\root\cimv2 path __namespace get name /value >> "$output_file"
