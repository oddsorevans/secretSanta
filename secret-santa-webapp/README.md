# Secret Santa — Web App

A Vue 3 + Flask web app for organizing a Secret Santa exchange. Add participants, set exclusion rules, pick a card style, preview the rendered email, and send. Pairings are generated server-side and **never returned to the organizer**, so the host stays surprised too.

## Features

- **Participant management** — add by hand or paste a CSV
- **Exclusion rules** — one-way (`A→B`) or auto-mutual (`A⇄B`); useful for couples and roommates
- **5 HTML card styles** — Classic Christmas, Elegant Gold, Winter Wonderland, Festive Fun, Rustic Charm
- **Custom message templates** — variables: `{giver_name}`, `{recipient_name}`, `{recipient_interests}`, `{recipient_address}`
- **Debug mode** — generate pairings and view rendered cards without sending email; download cards as HTML
- **Email debug mode** — send all generated emails to your own address instead of recipients (sanity check)

## Requirements

- Python 3.8+
- Node.js 18+
- A Gmail account with an [App Password](https://myaccount.google.com/apppasswords) (or any SMTP server)

## Quick start

From the `secret-santa-webapp/` directory:

```bash
./start.sh
```

The script creates the Python venv, installs dependencies, and starts both servers. Open <http://localhost:5173>.

### Manual setup

**Backend** (terminal 1):
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
Backend runs on <http://localhost:5001>. Port 5001 is used because macOS uses 5000 for AirPlay Receiver.

**Frontend** (terminal 2):
```bash
cd frontend
npm install
npm run dev
```
Frontend runs on <http://localhost:5173> and proxies `/api/*` to the backend.

## Usage

1. **Participants** — add at least 3 people manually, or upload a CSV with columns `Email,Name,Interests` (and optionally `Address`).
2. **Exclusions** — click pairs of names to block them. The auto-mutual toggle decides whether `A→B` also blocks `B→A`.
3. **Email template** — pick a card style, write your message, and choose between **Send Real Emails** (requires SMTP creds) or **Debug Mode** (preview only).
4. **Send** — review the summary and send. In real-send mode, pairings are not shown to you.

### CSV format

```csv
Email,Name,Interests
alice@example.com,Alice,"Books, hiking, coffee"
bob@example.com,Bob,"Board games, cooking, vinyl records"
```

## Project layout

```
secret-santa-webapp/
├── backend/
│   ├── app.py              # Flask API (/api/send, /api/health)
│   ├── card_templates.py   # HTML card generators (Python, used at send time)
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.vue
│   │   ├── cardTemplates.js  # HTML card generators (JS, used for preview)
│   │   ├── components/       # Per-step Vue components
│   │   └── main.js
│   ├── vite.config.js
│   └── package.json
└── start.sh
```

## Production build

```bash
cd frontend && npm run build      # outputs to frontend/dist/
```

For the backend in production, use a real WSGI server (e.g. Gunicorn) behind HTTPS instead of `flask run`. SMTP credentials are accepted from the form and never persisted on the server.

## Troubleshooting

- **Backend won't start on port 5000** — that's macOS AirPlay Receiver. The app already uses 5001; if you want 5000 back, disable AirPlay Receiver in System Settings → General → AirDrop & Handoff.
- **Gmail rejects the password** — make sure 2-Step Verification is on and you're using a 16-character App Password, not your account password.
- **Pairing fails** — too many exclusions can make a valid arrangement impossible. The algorithm will retry, but with very tight constraints it can spin; loosen the rules.
- **403 / CORS errors** — confirm the backend is running (`curl http://localhost:5001/api/health` should return `{"status":"ok"}`).

## Stack

- **Frontend**: Vue 3 (Composition API), Vite, Tailwind CSS, axios
- **Backend**: Flask, Flask-CORS, smtplib (stdlib)
- **API**: REST + JSON
