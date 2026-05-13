# Secret Santa — CLI

A small Python script that reads participants from a CSV, generates Secret Santa pairings (respecting exclusion rules), and emails each person their assignment via Gmail SMTP.

## Requirements

- Python 3.8+
- A Gmail account with an [App Password](https://myaccount.google.com/apppasswords)

No third-party dependencies — everything used is in the standard library.

## Setup

1. **Set your credentials.** Copy the example file and fill in your own:
   ```bash
   cp credentials.py.example credentials.py
   ```
   Edit `credentials.py` to set `FROM` (your Gmail address) and `appPassword` (the 16-character app password). `credentials.py` is gitignored.

   Alternatively, export environment variables instead of creating the file:
   ```bash
   export SECRET_SANTA_EMAIL="you@gmail.com"
   export SECRET_SANTA_APP_PASSWORD="xxxxxxxxxxxxxxxx"
   ```

2. **Add your participants.** Create `data/participants.csv` with these columns:
   ```csv
   Name,Email,Interests,Address
   Alice,alice@example.com,"Books, hiking","123 Main St"
   Bob,bob@example.com,"Board games","456 Oak Ave"
   ```
   See [`data/participants.example.csv`](data/participants.example.csv) for a full example. Files matching `data/*.csv` are gitignored (the `.example.csv` file is the exception).

3. **(Optional) Add exclusion rules.** Create `data/exclusions.json` mapping each name to people they cannot draw:
   ```json
   {
     "Alice": ["Bob"],
     "Bob": ["Alice"]
   }
   ```
   Useful for couples or roommates. See [`data/exclusions.example.json`](data/exclusions.example.json).

## Usage

Dry-run (prints pairings to the terminal, sends nothing):
```bash
python main.py --dry-run
```

Send for real:
```bash
python main.py
```

Custom file paths:
```bash
python main.py --participants data/my_list.csv --exclusions data/my_exclusions.json
```

## How pairings work

The algorithm walks the participant list in order; for each giver it picks a random recipient that isn't themselves and isn't in their exclusion list. If it paints itself into a corner (no valid recipient remains), it restarts from scratch. With reasonable exclusion lists this terminates quickly.

## Files

- `main.py` — CLI entry point and pairing algorithm
- `connect.py` — SMTP send logic
- `credentials.py.example` — template for SMTP credentials
- `data/participants.example.csv` — example participant list
- `data/exclusions.example.json` — example exclusion rules
