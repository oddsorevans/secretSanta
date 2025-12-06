# Secret Santa Web Application

A modern, stylish web application for organizing Secret Santa gift exchanges with beautiful HTML email cards.

## ✨ Features

- **Participant Management**: Add participants manually or import from CSV
- **Flexible Exclusion Rules**:
  - Set one-way or mutual exclusions
  - Visual indicators for exclusion types (→ for one-way, ⇄ for mutual)
  - Auto-mutual toggle for convenience
- **5 Beautiful Christmas Card Styles**:
  - 🎄 Classic Christmas (red & green traditional)
  - ✨ Elegant Gold (sophisticated gold & white)
  - ❄️ Winter Wonderland (cool blues & snowflakes)
  - 🎁 Festive Fun (bright & playful)
  - 🕯️ Rustic Charm (warm & cozy wood tones)
- **Custom Email Templates**: Create personalized messages with dynamic variables
- **Live Card Preview**: See exactly how your styled email card will look
- **Debug Mode**: Test pairings and preview all cards before sending
- **Secret Pairings**: Pairings are generated and sent without revealing them to the organizer
- **Modern UI**: Built with Vue 3 and Tailwind CSS for a beautiful, responsive experience

## Project Structure

```
secret-santa-webapp/
├── frontend/          # Vue 3 + Vite frontend
│   ├── src/
│   │   ├── components/
│   │   ├── App.vue
│   │   └── main.js
│   └── package.json
├── backend/           # Flask API backend
│   ├── app.py
│   └── requirements.txt
└── README.md
```

## Setup Instructions

### Prerequisites

- Node.js (v18 or higher)
- Python 3.8 or higher
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd secret-santa-webapp/backend
   ```

2. Create a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask server:
   ```bash
   python app.py
   ```

   The backend will start on `http://localhost:5001`

   **Note for macOS users:** Port 5001 is used to avoid conflicts with macOS AirPlay Receiver which uses port 5000

### Frontend Setup

1. Open a new terminal and navigate to the frontend directory:
   ```bash
   cd secret-santa-webapp/frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

   The frontend will start on `http://localhost:5173`

4. Open your browser and go to `http://localhost:5173`

## Usage Guide

### Step 1: Add Participants

- **Manual Entry**: Fill in name, email, and interests for each participant
- **CSV Import**: Upload a CSV file with columns: Email, Name, Interests

Example CSV format:
```csv
Email,Name,Interests
john@example.com,John,"Coffee, books, hiking"
jane@example.com,Jane,"Art, cooking, travel"
```

### Step 2: Set Exclusions

- **Auto-Mutual Toggle**: Enable/disable automatic reciprocal exclusions
  - When ON: Excluding A→B automatically excludes B→A
  - When OFF: Create one-way exclusions (A can't buy for B, but B can buy for A)
- **Visual Indicators**:
  - Red button with → : One-way exclusion
  - Red button with ⇄ and ring: Mutual exclusion
- Common uses: couples, roommates, family members

### Step 3: Choose Card Style & Customize Message

1. **Select Card Style**: Choose from 5 beautiful Christmas-themed designs
   - Each style has unique fonts, colors, and layouts
   - Preview your selection in real-time

2. **Configure SMTP**:
   - Server: `smtp.gmail.com` (for Gmail)
   - Port: `587`
   - Email: Your email address
   - Password: App-specific password (see Gmail setup below)

3. **Edit Message Content**:
   - Write your personalized message
   - Use variables: `{giver_name}`, `{recipient_name}`, `{recipient_interests}`
   - Your message is automatically inserted into the styled card
   - Click "Show Full Preview" to see the complete HTML card

### Step 4: Send Emails

- Review your configuration summary
- **Debug Mode** (NEW! 🔍):
  - View all pairings before sending
  - Preview each styled email card
  - Download individual cards as HTML files
  - Perfect for testing without sending actual emails
- **Send Emails**: Generates secret pairings and sends beautiful HTML cards to all participants
- **Important**: Once sent (not in debug mode), pairings are NOT shown to you!

## Gmail Setup

To use Gmail for sending emails:

1. Enable 2-Step Verification on your Google Account
2. Go to: [Google Account](https://myaccount.google.com/) → Security → 2-Step Verification
3. Scroll down to "App passwords"
4. Generate a new app password for "Mail"
5. Use this 16-character password in the SMTP configuration

## Features in Detail

### Dynamic Email Variables

- `{giver_name}`: Name of the person receiving the email
- `{recipient_name}`: Name of their Secret Santa recipient
- `{recipient_interests}`: Interests of the recipient

### Pairing Algorithm

- Based on the original Python implementation
- Ensures everyone gives and receives exactly once
- Respects all exclusion rules
- Automatically retries if exclusions create impossible scenarios

### Security

- SMTP credentials are never stored
- Pairings are generated server-side and not returned to the organizer
- All data is processed in-memory and not saved

## Building for Production

### Frontend

```bash
cd frontend
npm run build
```

Built files will be in `frontend/dist/`

### Backend

For production deployment, consider using:
- Gunicorn or uWSGI for serving the Flask app
- Environment variables for configuration
- HTTPS for secure communication

## Troubleshooting

### Emails Not Sending

- Check SMTP credentials are correct
- For Gmail, ensure you're using an App Password, not your regular password
- Verify your email provider allows SMTP access
- Check firewall settings allow connections on port 587

### CSV Import Issues

- Ensure CSV has headers: Email, Name, Interests
- Check for proper formatting and encoding (UTF-8)
- Verify no missing fields

### Pairing Algorithm Fails

- Review exclusion rules - they may make valid pairings impossible
- Ensure you have at least 3 participants
- Try reducing the number of exclusions

## Development

The application uses:
- **Frontend**: Vue 3 (Composition API), Vite, Tailwind CSS
- **Backend**: Flask, Flask-CORS
- **Communication**: REST API with JSON

To modify the pairing algorithm, edit `backend/app.py::create_secret_santa_list()`

## License

This project is provided as-is for personal use.

## Credits

Based on the original Secret Santa pairing script by Evan Jackson.
