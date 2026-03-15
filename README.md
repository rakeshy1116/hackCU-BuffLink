# BuffLink (HackCU)

## BuffLink: Your CU Boulder Event Companion!

Discover CU Boulder events effortlessly! Set preferences, get personalized event alerts & calendar invites. Stay connected!

<img width="998" alt="Architecture" src="https://github.com/rakeshy1116/hackCU-BuffLink/assets/33839890/61368dcf-7a38-4dc4-9aac-f77d0cdda084">

## Video Demo

https://youtu.be/DUDM809RSwY

## Screenshots

https://drive.google.com/drive/folders/1VCwXvL1xMObncciUkBdARr_etGcyC77w?usp=drive_link

---

## About Project

A browser extension tailored for CU Boulder students. Set your event preferences once, and BuffLink will curate personalized events from the CU Boulder calendar, sending email notifications with calendar invites so you never miss out.

**Tech Stack:**
- **Frontend:** Chrome Extension (Manifest V3), Vanilla JS, Bootstrap 5
- **Backend:** Python 3, Flask, BeautifulSoup4
- **AI/ML:** Facebook BART Large MNLI (75% confidence threshold for event relevancy)
- **Database:** AWS DynamoDB
- **Email:** Gmail SMTP with iCalendar (`.ics`) attachments

---

## Getting Started

### Prerequisites

- Python 3.9+
- AWS account with DynamoDB tables (`User`, `NewEvents`) in your chosen region
- A Gmail account with an [App Password](https://support.google.com/accounts/answer/185833) enabled
- Google Chrome (for the browser extension)

### 1. Clone the repository

```bash
git clone https://github.com/rakeshy1116/hackCU-BuffLink.git
cd hackCU-BuffLink
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Copy the example env file and fill in your values:

```bash
cp .env.example .env
```

Edit `.env`:

```env
AWS_REGION=us-east-2
SENDER_EMAIL=your-email@gmail.com
SMTP_PASSWORD=your-gmail-app-password

# Optional: restrict to your Chrome extension's origin
# e.g. ALLOWED_ORIGINS=chrome-extension://abcdefghijklmnopqrstuvwxyz123456
ALLOWED_ORIGINS=*

FLASK_DEBUG=false
FLASK_PORT=5007
```

> **Never commit `.env` to version control.** It is listed in `.gitignore`.

### 4. Load environment variables and start the backend

```bash
# Using python-dotenv (loaded automatically if you use the load_dotenv call)
# Or export manually:
export $(grep -v '^#' .env | xargs)
python post_request.py
```

### 5. Load the browser extension

1. Open Chrome and navigate to `chrome://extensions/`
2. Enable **Developer mode** (top right)
3. Click **Load unpacked** and select the `frontend/` directory
4. The BuffLink icon will appear in your toolbar

---

## AWS DynamoDB Setup

Create two tables in DynamoDB:

| Table | Partition Key |
|-------|---------------|
| `User` | `emailId` (String) |
| `NewEvents` | `hash_id` (String) |

**NewEvents attributes:** `title`, `description`, `startDate`, `endDate`, `eventStatus`, `url`, `image`

**User attributes:** `userName`, `previousMails` (List), `extensionPrompts` (List)

---

## How It Works

```
Browser Extension (Frontend)
    ↓ POST: name, email, interests
Flask API (post_request.py :5007)
    ├→ Validate & store user prefs → DynamoDB (User table)
    ├→ Fetch all events → DynamoDB (NewEvents table)
    └→ BART NLI (75% threshold) → match events to interests
        ↓
    email_handler.py  (deduplication via previousMails)
        ↓
    send_email.py  (Gmail SMTP)
        ↓
    User Inbox: HTML email + .ics calendar invite
```

A separate scraper (`parse_calendar.py` → `parse_event.py`) populates the `NewEvents` table by parsing the [CU Boulder calendar](https://calendar.colorado.edu/calendar).

---

## Project Structure

```
hackCU-BuffLink/
├── .env.example          # Environment variable template
├── .gitignore
├── requirements.txt
├── post_request.py       # Flask API entry point
├── parse_calendar.py     # CU Boulder calendar scraper
├── parse_event.py        # Individual event parser
├── email_handler.py      # Email orchestration & deduplication
├── build_email.py        # HTML email + iCalendar builder
├── send_email.py         # Gmail SMTP sender
├── user_dynamo.py        # User DynamoDB operations
├── fetch_user_data.py    # User query helpers
├── fetch_event_data.py   # Event query helpers
├── events_tableget.py    # Event table scanner
├── aws_dynamo.py         # Generic DynamoDB uploader
├── dynamo_db_format.py   # Python → DynamoDB type converter
├── lm.py                 # Alternative DistilBart implementation
└── frontend/
    ├── manifest.json     # Chrome extension manifest (V3)
    ├── index.html        # Extension popup UI
    ├── script.js         # Extension logic
    ├── style.css         # Styling
    └── background.js     # Service worker
```

---

## Inspiration

Tired of missing out on exciting campus events? We felt the same! That's why we built BuffLink — a zero-cost, personalized event companion that delivers curated updates directly to your inbox.

## Challenges

Understanding user intent accurately was the main challenge. For example, "hike" could mean an outdoor activity or a salary negotiation talk. Balancing these interpretations required careful NLI prompt engineering.

## Accomplishments

- Built from scratch during HackCU — our first browser extension!
- Integrated NLP (BART), web scraping, AWS DynamoDB, and email delivery in a single weekend.
- Zero-cost architecture using AWS free tier + Gmail SMTP.

## What We Learned

Teamwork, proper coordination, and new technologies (Chrome Extensions, Transformers, DynamoDB). This hackathon pushed our limits and showed us we could build more than we thought.

## What's Next for BuffLink

- On-campus job board integration (filter postings by student interest)
- Deadline reminders for international students (OPT/CPT dates, etc.)
- Unsubscribe / preference management interface
- Scheduled scraping to keep the events table fresh automatically
