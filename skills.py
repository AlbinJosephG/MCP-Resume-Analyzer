KNOWN_SKILLS = {
    "python",
    "machine learning",
    "deep learning",
    "nlp",
    "sql",
    "docker",
    "cloud",
    "tensorflow",
    "data analysis",
    "rest apis"
}

def extract_skills(text: str) -> set:
    text = text.lower()
    return {skill for skill in KNOWN_SKILLS if skill in text}
