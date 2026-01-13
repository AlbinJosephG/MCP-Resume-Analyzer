from fastapi import FastAPI, UploadFile, Form, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
import pdfplumber

from skills import extract_skills

app = FastAPI()

# ✅ Mount static directory for CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


def read_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/analyze", response_class=HTMLResponse)
async def analyze(
    request: Request,
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    resume_text = read_pdf(resume.file)

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched = resume_skills & job_skills
    missing = job_skills - resume_skills

    score = int((len(matched) / max(len(job_skills), 1)) * 100)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "score": score,
            "matched": sorted(matched),
            "missing": sorted(missing),
        }
    )
