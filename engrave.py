import scratchattach as scratch3

import os

os.system('clear')

username = input('Input Username\n')

password = input('Input Password\n')

session = scratch3.login(username, password)

id = input('Input Id of project\n')

conn = session.connect_cloud(id)

logs = scratch3.get_cloud(id)

print('current variables in use\n')

print(logs)

print('\n')

temp = input('would you like to pull a value to txt? yes or no\n')
if temp == 'yes':
    temp = input('Input variable name\n')
    tvalue = scratch3.get_var(id, temp)
    with open('variable.txt', 'w') as f:
        f.write(tvalue)
    print('saved to variable.txt')
else:
    input_string = input('Enter all variable names to set separated by dashes\n')
    value = input('Input value of vars\n')
    var_list = input_string.split("-")
    loops = input('Flood infinitely? yes or no\n')
    if loops == 'yes':
        while True:
            for name in var_list:
                print("Flooding...")
                print(name)
                conn.set_var(name, value)
    else:
        for name in var_list:
            print("Flooding...")
            print(name)
            conn.set_var(name, value)
