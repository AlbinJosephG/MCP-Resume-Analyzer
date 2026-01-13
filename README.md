# MCP-Resume-Analyzer
A simple AI-powered resume analyzer that matches resumes against job descriptions and suggests skill improvements. This project uses MCP logic for analysis and provides a FastAPI web interface for easy interaction.

## Project Structure

```bash
mcp-resume-analyzer/
├── server.py # Core MCP resume analysis logic
├── web.py # FastAPI backend
├── skills.py # Skill extraction utilities
├── templates/
│ └── index.html # Frontend HTML template
├── static/
│ └── style.css # Frontend styles
├── .venv/ # Python virtual environment
└── README.md
 ```

## Features

- **Resume Parsing** – Reads PDF resumes.
- **Job Matching** – Compares resume content against job descriptions.
- **Skill Suggestions** – Highlights missing or recommended skills.
- **Web Interface** – Upload resumes and job descriptions in a browser.
- **Separation of Logic** – MCP backend logic separated from frontend.

## 🛠 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/mcp-resume-analyzer.git
cd mcp-resume-analyzer
 ```
2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate    # Linux / macOS
.venv\Scripts\activate
 ```
3.Install dependencies:

```bash
pip install fastapi uvicorn PyPDF2 jinja2
 ```
## 📂 Usage

1. Prepare your resume PDF.

2. Create a job description text file (plain text).

3. Upload both via the web interface.

4. View the output:

- Resume-job match score

- Skills missing or recommended

## 📜 License

This project is MIT Licensed

## Screenshots
<img width="1206" height="888" alt="image" src="https://github.com/user-attachments/assets/cb0ddf58-26b5-4462-9f8a-c753900050aa" />


