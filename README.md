Doc2Slides, which automates the conversion of uploaded documents into downloadable PowerPoint presentations:

⸻

📄 Doc2Slides

Doc2Slides is an automated system that allows users to upload PDFs or JPEGs via a form and receive a downloadable PowerPoint presentation with each page or image rendered as a slide.

⸻

✨ Features

📤 Accepts PDF and JPEG uploads via Tally.so or Typeform

🔁 Fully automated using Zapier + GitHub Actions

🖼️ Converts each page/image into a PowerPoint slide

📝 Adds optional titles or captions to slides

📥 Sends download link via SMS or email

🌐 Publishes .pptx files to GitHub Pages or cloud storage

🔐 Secure credential handling with GitHub Secrets

⸻

🧾 How It Works

User Uploads File

Via a Tally.so or Typeform form with fields for:

File (PDF or JPEG)

Title or description

Contact info (email or phone)

Zapier

Downloads the uploaded file

Sends metadata and file URL to GitHub Actions via REST API

GitHub Actions

Downloads the file

Runs generate_slides.py to create a PowerPoint

Saves the .pptx to docs/output/

Sends a download link via ClickSend or email

⸻

📁 Project Structure

.

├── .github/

│   └── workflows/

│       └── generate_slides.yml       # GitHub Action workflow

├── docs/

│   └── output/                       # Published PowerPoint files

├── uploads/                          # Temporary file storage

├── generate_slides.py                # Converts files to PowerPoint

├── requirements.txt                  # Python dependencies

└── README.md

⸻

🔧 Setup Instructions

1. Create GitHub Repository

Create a new repository named doc2slides.

2. Add GitHub Secrets

Go to Repo → Settings → Secrets → Actions and add:

Secret NameDescription

CLICKSEND_USERNAMEYour ClickSend email login

CLICKSEND_API_KEYYour ClickSend API key

EMAIL_API_KEY(Optional) Email service API key

3. Define GitHub Action

File: .github/workflows/generate_slides.yml

on:

  workflow_dispatch:

    inputs:

      file_url:

        required: true

      title:

        required: true

      recipient:

        required: true

4. Zapier Setup

Trigger: New form submission

Action 1: Download file

Action 2: POST to GitHub API

POST https://api.github.com/repos/your-username/doc2slides/actions/workflows/generate_slides.yml/dispatches

Headers:

{

  "Authorization": "Bearer YOUR_GITHUB_PAT",

  "Accept": "application/vnd.github.v3+json"

}

Body:

{

  "ref": "main",

  "inputs": {

    "file_url": "https://example.com/uploaded.pdf",

    "title": "Team Orientation Slides",

    "recipient": "+1234567890"

  }

}

⸻

🧪 Local Testing

# Set environment variables

export CLICKSEND_USERNAME="your_email@example.com"

export CLICKSEND_API_KEY="your_api_key"



# Run script manually

python generate_slides.py --file "uploads/sample.pdf" --title "My Slides" --recipient "+1234567890"

⸻

✅ Requirements

python-pptx

PyMuPDF

Pillow

clicksend-client

requests

⸻

🛠️ Future Improvements

Add support for DOCX and PNG

Generate ICS calendar invites for presentations

Web dashboard to manage uploaded files and downloads

Google Drive or Dropbox integration

⸻

📘 License

MIT License

⸻

Would you like me to generate this file for you now?

