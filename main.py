import csv
import random
from pprint import pprint
from datetime import datetime
from connect import sendEmails


def create_secret_santa_list(names, excluded_pairings={}):
    random.seed(datetime.now().timestamp())
    secret_santa_list = []
    remaining_names = names.copy()

    for giver in names:
        possible_recipients = [name for name in remaining_names if name != giver and name not in excluded_pairings.get(giver, [])]
        
        if not possible_recipients:
            # If there are no valid recipients, start over
            return create_secret_santa_list(names, excluded_pairings)

        recipient = random.choice(possible_recipients)
        secret_santa_list.append((giver, recipient))
        remaining_names.remove(recipient)

    return secret_santa_list

def process_csv(csv_file_path):
    data_dict = {}
    names = []

    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            name = row['Name'].strip()
            email = row['Email'].strip()
            interests = row['Interests'].strip()
            address = row['Address'].strip()

            names.append(name)

            # Create the inner dictionary
            inner_dict = {'email': email, 'interests': interests, 'address': address}

            # Add to the main dictionary
            data_dict[name] = inner_dict

    return names, data_dict

#dictionary of illegal matchups
illegal = {
    "Dylan":["Rachel"],
    "Rachel":["Dylan"],
    "Chris":["Sarah", "Evan"],
    "Sarah":["Chris"],
    "Evan":["Chris"],
    "Ron":["Sydney"],
    "Sydney":["Ron"],
    "Keaton":["Ally"], 
    "Ally":["Keaton"]
}

#fill dictionary with name email pair from csv file. csv file is formatted as Name,Email
emails = {}
pairs = {}
#create 2 lists so that I can make pairs
names = []
complete = False

names, emails = process_csv('emails.csv')

pairs = create_secret_santa_list(names, illegal)

sendEmails(pairs, emails)

