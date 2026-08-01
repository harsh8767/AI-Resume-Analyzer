import re


def calculate_ats_score(
    resume_text,
    matched_keywords,
    jd_keywords,
    similarity_score
):
    """
    Calculates ATS score using multiple factors.
    Returns:
        ats_score,
        keyword_score,
        section_score,
        length_score,
        contact_score
    """

    # -----------------------------
    # Keyword Score (40%)
    # -----------------------------
    if len(jd_keywords) > 0:
        keyword_ratio = len(matched_keywords) / len(jd_keywords)
    else:
        keyword_ratio = 0

    keyword_score = keyword_ratio * 40

    # -----------------------------
    # Similarity Score (30%)
    # -----------------------------
    similarity_component = (similarity_score / 100) * 30

    # -----------------------------
    # Resume Sections (15%)
    # -----------------------------
    sections = [
        "education",
        "experience",
        "skills",
        "projects",
        "certifications",
        "summary"
    ]

    found = 0

    text = resume_text.lower()

    for section in sections:
        if section in text:
            found += 1

    section_score = (found / len(sections)) * 15

    # -----------------------------
    # Resume Length (10%)
    # -----------------------------
    words = len(resume_text.split())

    if 300 <= words <= 900:
        length_score = 10
    elif 200 <= words < 300:
        length_score = 8
    else:
        length_score = 5

    # -----------------------------
    # Contact Details (5%)
    # -----------------------------
    email = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        resume_text
    )

    phone = re.search(
        r"\+?\d[\d\s-]{8,}",
        resume_text
    )

    contact_score = 0

    if email:
        contact_score += 2.5

    if phone:
        contact_score += 2.5

    ats_score = (
        keyword_score
        + similarity_component
        + section_score
        + length_score
        + contact_score
    )

    ats_score = round(min(100, ats_score), 2)

    return (
        ats_score,
        round(keyword_score, 2),
        round(section_score, 2),
        round(length_score, 2),
        round(contact_score, 2),
    )