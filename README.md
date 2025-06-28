# 📄 Doc2Slides: Upload to PowerPoint via GitHub Pages

Doc2Slides lets users upload PDF or JPEG files through a web form hosted on GitHub Pages. Once uploaded, a GitHub Actions workflow is triggered to generate a downloadable PowerPoint presentation from the document.

---

## 🚀 Features

- 🖼️ Upload PDF or JPEG via GitHub Pages form
- 💾 File is saved to the GitHub repository using GitHub API
- ⚙️ GitHub Actions workflow is triggered to convert the file to a PowerPoint
- 📂 Generated `.pptx` is published to GitHub Pages for download

---

## 🌐 Live Demo
```
[https://clgi-technology.github.io/clgi-announcements/](https://clgi-technology.github.io/clgi-announcements/)

```

---

## 📁 Project Structure

```
text
.
├── docs/
│   └── output/                  # Generated PowerPoint presentations (deployed via GitHub Pages)
├── uploads/                    # Uploaded files saved via GitHub API
├── generate_slides.py         # Script to convert PDF/JPEG to PowerPoint
├── index.html                 # GitHub Pages form (uploads + triggers workflow)
├── .github/
│   └── workflows/
│       └── generate_slides.yml  # GitHub Actions workflow
├── requirements.txt           # Python dependencies
└── README.md

```

🛠️ Setup Instructions
1. Clone the Repo
```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

```
2. Enable GitHub Pages
In your GitHub repo:

Go to Settings → Pages

Source: docs/ folder on main branch

3. Add Personal Access Token (PAT)
Generate a GitHub PAT with repo and workflow scopes.
Store this token securely and use it in your index.html JavaScript.

Do NOT hardcode your token in public files! For production use, route through a backend or proxy.

4. Configure Workflow Trigger
The workflow in .github/workflows/generate_slides.yml listens for


```

on:
  repository_dispatch:
    types: [generate_slides]
Payload must include:

{
  "event_type": "generate_slides",
  "client_payload": {
    "file_url": "https://raw.githubusercontent.com/.../uploads/file.pdf",
    "title": "Presentation Title"
  }
}

```

🧾 How It Works
User uploads a file via index.html form

JavaScript encodes and uploads file to /uploads/ via GitHub API

It then calls the GitHub REST API to trigger a repository_dispatch event

GitHub Actions workflow runs:

Downloads the uploaded file

Converts it into a .pptx using generate_slides.py

Saves it to docs/output/

GitHub Pages automatically serves the updated docs/ directory

📦 Python Requirements
Install dependencies locally for testing:

```
bash
Copy
Edit
pip install -r requirements.txt
Required packages:

python-pptx

PyMuPDF

Pillow

requests

```

🧪 Local Test

```

python generate_slides.py uploads/sample.pdf "My Test Title"

```

📘 License
MIT License


---
