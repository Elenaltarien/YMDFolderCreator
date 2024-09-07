# Automate numerical series folder creation.
# Rachel MM Fisher fisherr@labcorp.com
# Sources: 
# - Geeks for Geeks

# Import necessary modules
import os

# Get user input on how many files to create and where to create them.
num_folders = input('How many folders would you like to create? ')
parent_dir_prompt = input('Enter file path: ')

# Creates folders based on previous user input.
d = 1
while d <= int(num_folders):
    directory = str(d)
    parent_dir = parent_dir_prompt
    path = os.path.join(parent_dir, directory)
    os.makedirs(path)
    print("Directory '%s' created" % directory)
    d += 1
