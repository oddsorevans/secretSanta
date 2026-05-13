import argparse
import csv
import json
import random
from datetime import datetime
from pathlib import Path

from connect import send_emails


def create_secret_santa_list(names, excluded_pairings=None):
    if excluded_pairings is None:
        excluded_pairings = {}

    random.seed(datetime.now().timestamp())
    secret_santa_list = []
    remaining_names = names.copy()

    for giver in names:
        possible_recipients = [
            name for name in remaining_names
            if name != giver and name not in excluded_pairings.get(giver, [])
        ]

        if not possible_recipients:
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
            names.append(name)
            data_dict[name] = {
                'email': row['Email'].strip(),
                'interests': row['Interests'].strip(),
                'address': row['Address'].strip(),
            }

    return names, data_dict


def load_exclusions(path):
    if not path or not Path(path).exists():
        return {}
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def parse_args():
    parser = argparse.ArgumentParser(description='Generate Secret Santa pairings and send emails.')
    parser.add_argument('--participants', default='data/participants.csv',
                        help='Path to participants CSV (columns: Name, Email, Interests, Address)')
    parser.add_argument('--exclusions', default='data/exclusions.json',
                        help='JSON mapping of giver -> list of names they cannot draw')
    parser.add_argument('--dry-run', action='store_true',
                        help='Print pairings to stdout instead of sending emails')
    return parser.parse_args()


def main():
    args = parse_args()

    names, participants = process_csv(args.participants)
    exclusions = load_exclusions(args.exclusions)
    pairs = create_secret_santa_list(names, exclusions)

    if args.dry_run:
        for giver, recipient in pairs:
            print(f'{giver} -> {recipient}')
        return

    send_emails(pairs, participants)


if __name__ == '__main__':
    main()
