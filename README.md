# Secret Santa

Two ways to draw and email Secret Santa pairings, with support for exclusion rules (couples, roommates, etc.) so people don't draw their partner.

## Pick one

| | [`python-cli/`](python-cli/) | [`secret-santa-webapp/`](secret-santa-webapp/) |
|---|---|---|
| **What it is** | A small Python script | A Vue + Flask web app |
| **Best for** | One-off use from a terminal | Friends/family who'd rather click than type commands |
| **Output** | Plain-text email | Styled HTML Christmas-card email (5 themes) |
| **Setup** | Python 3.8+, a Gmail app password | Python 3.8+, Node 18+, a Gmail app password |
| **Pairings hidden from organizer?** | No (it's your script) | Yes (generated server-side, never returned to UI) |

Both versions read participants from CSV, support exclusion rules, and send via SMTP. The webapp also has a debug mode that previews the rendered cards without sending anything.

## Repo layout

```
.
├── python-cli/             # Original CLI version
│   ├── main.py
│   ├── connect.py
│   ├── credentials.py.example
│   └── data/
│       ├── participants.example.csv
│       └── exclusions.example.json
└── secret-santa-webapp/    # Web app version
    ├── backend/            # Flask API
    └── frontend/           # Vue 3 + Vite + Tailwind
```

See each folder's `README.md` for setup and usage.

## Gmail app passwords

Both versions need a Gmail App Password (not your account password). Create one at <https://myaccount.google.com/apppasswords> after enabling 2-Step Verification.
