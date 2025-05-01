import os

def get_credentials(filepath):
    with open(filepath,"r") as file:
        return [line.strip() for line in file if line.strip()]

def get_next_account_index(last_used_file, total_accounts):
    #gets the index of the next account to use

    if not os.path.exists(last_used_file):
        return 0 #starts with first account if no list exists
    with open(last_used_file,"r") as file:
        last_index = int(file.readline().strip())
    return (last_index + 1) % total_accounts #cycle through accounts

def update_last_used_index(last_used_file, index):
    #updates last used account index in the file
    with open(last_used_file,"w") as file:
        file.write(str(index))
        