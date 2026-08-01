import os

from dotenv import load_dotenv
from google import genai

# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL_NAME = "gemini-3.5-flash-lite"


def generate_ai_review(
    resume_text,
    job_description,
    ats_score,
    missing_keywords,
):
    """
    Generates a professional AI recruiter review
    using Google's Gemini model.
    """

    missing = ", ".join(missing_keywords)

    if not missing:
        missing = "None"

    prompt = f"""
You are a Senior Technical Recruiter with over 15 years of experience hiring candidates for Software Engineering, Data Science, AI, Data Analytics and Product roles.

Your job is to review the candidate's resume exactly like a real recruiter.

The review should be practical, concise and ATS-focused.

Candidate ATS Score:
{ats_score}%

Important Missing Skills:
{missing}

=========================
RESUME
=========================
{resume_text}

=========================
JOB DESCRIPTION
=========================
{job_description}

Instructions:

• Evaluate both ATS compatibility and recruiter appeal.
• Focus on whether this resume is likely to get shortlisted.
• Mention only important missing skills.
• Avoid generic advice.
• Keep the review realistic.
• Do NOT exaggerate strengths.
• Do NOT repeat the ATS score.
• Keep the entire response under 350 words.

Return the report EXACTLY in the following format.

# 📌 Overall Assessment

Write 2-3 concise sentences.

# 💪 Strengths

- Bullet 1
- Bullet 2
- Bullet 3

# ⚠ Weaknesses

- Bullet 1
- Bullet 2
- Bullet 3

# ❌ Critical Missing Skills

Mention only important missing skills that would improve interview chances.

# 💡 Improvement Suggestions

Provide exactly FIVE practical improvements.

# 🎯 Interview Readiness

Score: XX/100

Explain in one concise paragraph why this score was given.

# 🏁 Recruiter Verdict

Choose ONLY ONE:

🟢 Strongly Recommend

🟢 Recommend

🟡 Consider

🔴 Not Recommended

End the report immediately after the verdict.
"""

    try:

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )

        if hasattr(response, "text") and response.text:
            return response.text.strip()

        return (
            "## ❌ AI Review Unavailable\n\n"
            "The AI model returned an empty response."
        )

    except Exception as e:

        return f"""
## ❌ AI Review Unavailable

Gemini could not generate the recruiter review.

**Reason**

{str(e)}

Please verify:

• Your Gemini API key is valid.

• Internet connection is available.

• The selected model is accessible.

Then try again.
"""