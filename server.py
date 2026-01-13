from mcp.server.fastmcp import FastMCP
from skills import extract_skills
import pdfplumber

mcp = FastMCP("Resume Analyzer MCP (PDF)")

@mcp.tool()
def read_resume_pdf(path: str = "resume.pdf") -> str:
    """Read text from resume PDF"""
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

@mcp.tool()
def score_job_match(resume_text: str, job_text: str) -> dict:
    """Score resume vs job description"""
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    matched = resume_skills & job_skills
    missing = job_skills - resume_skills

    score = int((len(matched) / max(len(job_skills), 1)) * 100)

    return {
        "match_score_percent": score,
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing)
    }

@mcp.tool()
def suggest_skills(resume_text: str, job_text: str) -> list:
    """Suggest skills to add"""
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)
    return sorted(job_skills - resume_skills)

if __name__ == "__main__":
    print("✅ MCP Resume Analyzer Server running...")
    mcp.run()
