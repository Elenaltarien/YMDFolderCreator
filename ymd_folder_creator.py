# Automate numerical series folder creation.
# Rachel MM Fisher elenaltarien@gmail.com
# Sources: 
# - Geeks for Geeks

# Import necessary modules
import os


# Dictionary of months folders and how many days are in the month. Doesn't account for Leap Year.
months = {'01January': 31, '02February': 28, '03March': 31, '04April': 30, '05May': 31, '06June': 30, '07July': 31, '08August': 31, '09September': 30, '10October': 31, '11November': 30, '12December': 31}

# Get user input on folder structure. 
file_path = input('Enter file path: ')
year = input('What year would you like to create folders for? ')
parent_dir = os.path.join(file_path, year)

folder_structure = input('Choose an option: 1. Monthly Folders   2. Monthly and Daily Folders ')

if (folder_structure == '1'):
    for k, v in months.items():
        months_dir = k
        months_parent_dir = parent_dir
        path = os.path.join(months_parent_dir,months_dir)
        os.makedirs(path)
        print("Directory '%s' created" % months_dir)
elif (folder_structure == '2'):
    for k, v in months.items():
        months_dir = k
        daily_dir = v
        d = 1
        while d <= daily_dir:
            directory = str(d)
            months_parent_dir = parent_dir
            month_path = os.path.join(months_parent_dir, months_dir)
            path = os.path.join(month_path, directory)
            os.makedirs(path)
            print("Directory '%s' created" % directory)
            d += 1
        # months_parent_dir = parent_dir_prompt
        # path = os.path.join(months_parent_dir,months_dir)
        # os.makedirs(path)
        # print("Directory '%s' created" % months_dir)
else: 
    print('That is an invalid option.')