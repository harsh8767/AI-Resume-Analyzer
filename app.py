import re
import streamlit as st

from utils.resume_parser import extract_resume_text
from utils.text_processor import preprocess_text
from utils.similarity import semantic_similarity
from utils.ats_score import calculate_ats_score
from utils.section_checker import check_resume_sections
from utils.charts import plot_skill_match
from utils.resume_grade import get_resume_grade
from utils.suggestions import generate_suggestions
from utils.ai_review import generate_ai_review
from utils.pdf_report import create_pdf_report



# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Resume & Job Match Analyzer",
    page_icon="📄",
    layout="wide"
)

# --------------------------------------------------
# Load CSS
# --------------------------------------------------

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# --------------------------------------------------
# Session State
# --------------------------------------------------

default_values = {
    "analysis_done": False,
    "resume_text": "",
    "resume_tokens": [],
    "jd_tokens": [],
    "matched_keywords": [],
    "missing_keywords": [],
    "semantic_score": 0,
    "keyword_score": 0,
    "ats_score": 0,
    "resume_sections": {},
    "grade": "",
    "stars": "",
    "recommendation": "",
    "suggestions": [],
    "ai_review": ""
}

for key, value in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = value

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title("📄 Resume Analyzer")

    st.divider()

    st.success("Version 0.4")

    st.subheader("🚀 Features")

    st.markdown("""
✅ Resume Parsing

✅ Text Processing

✅ Keyword Matching

✅ Semantic Similarity

✅ ATS Score

✅ Resume Grade

✅ AI Resume Review

✅ Skill Visualization

⏳ PDF Report
""")

# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    """
<h1 class="main-title">
AI Resume & Job Match Analyzer
</h1>

<p class="sub-title">
Analyze resumes against job descriptions using AI-powered insights.
</p>
""",
    unsafe_allow_html=True
)

# --------------------------------------------------
# Upload Section
# --------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("📄 Upload Resume")

    resume = st.file_uploader(
        "Upload PDF Resume",
        type=["pdf"]
    )

with right:

    st.subheader("📋 Job Description")

    job_description = st.text_area(
        "",
        height=250,
        placeholder="Paste the complete Job Description here..."
    )

# --------------------------------------------------
# Analyze Button
# --------------------------------------------------

if st.button(
    "🔍 Analyze Resume",
    use_container_width=True
):

    if resume is None:
        st.error("Please upload a resume.")
        st.stop()

    if not job_description.strip():
        st.error("Please paste a Job Description.")
        st.stop()

    # ------------------------------------------
    # Resume Parsing
    # ------------------------------------------

    resume_text = extract_resume_text(resume)

    st.success("✅ Resume parsed successfully!")

    with st.expander("View Extracted Resume Text"):

        st.text_area(
            "",
            resume_text,
            height=300
        )

    # ------------------------------------------
    # Text Processing
    # ------------------------------------------

    resume_tokens = preprocess_text(resume_text)
    jd_tokens = preprocess_text(job_description)

    resume_keywords = set(resume_tokens)
    jd_keywords = set(jd_tokens)

    matched_keywords = sorted(
        resume_keywords.intersection(jd_keywords)
    )

    missing_keywords = sorted(
        jd_keywords.difference(resume_keywords)
    )

    # ------------------------------------------
    # Score Calculation
    # ------------------------------------------

    semantic_score = semantic_similarity(
        resume_text,
        job_description
    )

    ats_score, keyword_component, section_score, length_score, contact_score = calculate_ats_score(
        resume_text=resume_text,
        matched_keywords=matched_keywords,
        jd_keywords=jd_keywords,
        similarity_score=semantic_score
    )

    keyword_score = round(
        len(matched_keywords) /
        max(len(jd_keywords), 1) * 100,
        2
    )

    resume_sections = check_resume_sections(resume_text)

    grade, stars, recommendation = get_resume_grade(
        ats_score
    )

    suggestions = generate_suggestions(
        ats_score,
        missing_keywords,
        resume_sections
    )

    # ------------------------------------------
    # AI Review (Generated Only Once)
    # ------------------------------------------

    ai_review = generate_ai_review(
        resume_text=resume_text,
        job_description=job_description,
        ats_score=ats_score,
        missing_keywords=missing_keywords
    )

    # ------------------------------------------
    # Save Everything
    # ------------------------------------------

    st.session_state.analysis_done = True

    st.session_state.resume_text = resume_text
    st.session_state.resume_tokens = resume_tokens
    st.session_state.jd_tokens = jd_tokens

    st.session_state.matched_keywords = matched_keywords
    st.session_state.missing_keywords = missing_keywords

    st.session_state.semantic_score = semantic_score
    st.session_state.keyword_score = keyword_score
    st.session_state.ats_score = ats_score

    st.session_state.resume_sections = resume_sections

    st.session_state.grade = grade
    st.session_state.stars = stars
    st.session_state.recommendation = recommendation

    st.session_state.suggestions = suggestions
    st.session_state.ai_review = ai_review

# --------------------------------------------------
# Display Results
# --------------------------------------------------

if st.session_state.analysis_done:

    resume_tokens = st.session_state.resume_tokens
    jd_tokens = st.session_state.jd_tokens

    matched_keywords = st.session_state.matched_keywords
    missing_keywords = st.session_state.missing_keywords

    semantic_score = st.session_state.semantic_score
    keyword_score = st.session_state.keyword_score
    ats_score = st.session_state.ats_score

    resume_sections = st.session_state.resume_sections

    grade = st.session_state.grade
    stars = st.session_state.stars
    recommendation = st.session_state.recommendation

    suggestions = st.session_state.suggestions

    ai_review = st.session_state.ai_review

    # --------------------------------------------------
    # Generate PDF Report
    # --------------------------------------------------

    pdf_path = "reports/resume_analysis_report.pdf"

    create_pdf_report(
        filename=pdf_path,
        ats_score=ats_score,
        semantic_score=semantic_score,
        keyword_score=keyword_score,
        grade=grade,
        recommendation=recommendation,
        matched_keywords=matched_keywords,
        missing_keywords=missing_keywords,
        suggestions=suggestions,
        ai_review=ai_review
    )


        # --------------------------------------------------
    # Analysis Overview
    # --------------------------------------------------

    st.divider()

    st.subheader("📊 Analysis Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📄 Resume Keywords",
            len(set(resume_tokens))
        )

    with col2:
        st.metric(
            "✅ Matched Keywords",
            len(matched_keywords)
        )

    with col3:
        st.metric(
            "🎯 JD Keywords",
            len(set(jd_tokens))
        )

    with col4:
        st.metric(
            "❌ Missing Keywords",
            len(missing_keywords)
        )

    # --------------------------------------------------
    # Resume Match Analysis
    # --------------------------------------------------

    st.divider()

    st.header("📈 Resume Match Analysis")

    score1, score2, score3 = st.columns(3)

    with score1:

        st.metric(
            "🎯 ATS Score",
            f"{ats_score}%"
        )

        st.progress(ats_score / 100)

    with score2:

        st.metric(
            "🧠 Semantic Match",
            f"{semantic_score}%"
        )

        st.progress(semantic_score / 100)

    with score3:

        st.metric(
            "🔑 Keyword Match",
            f"{keyword_score}%"
        )

        st.progress(keyword_score / 100)

    # --------------------------------------------------
    # Resume Rating
    # --------------------------------------------------

    st.divider()

    st.subheader("⭐ Resume Rating")

    rating_col1, rating_col2 = st.columns([1, 2])

    with rating_col1:

        st.metric(
            "Resume Grade",
            grade
        )

        st.metric(
            "ATS Ready",
            f"{ats_score}%"
        )

    with rating_col2:

        st.markdown(f"## {stars}")

        st.write("### Recommendation")

        st.info(recommendation)

    # --------------------------------------------------
    # Quick Statistics
    # --------------------------------------------------

    st.divider()

    stat1, stat2, stat3 = st.columns(3)

    with stat1:

        st.metric(
            "Matched Skills",
            len(matched_keywords)
        )

    with stat2:

        st.metric(
            "Missing Skills",
            len(missing_keywords)
        )

    with stat3:

        coverage = round(
            len(matched_keywords) /
            max(len(jd_tokens), 1) * 100,
            1
        )

        st.metric(
            "Skill Coverage",
            f"{coverage}%"
        )

    # --------------------------------------------------
    # Keyword Comparison
    # --------------------------------------------------

    st.divider()

    left_col, right_col = st.columns(2)

    with left_col:

        st.subheader("✅ Matching Keywords")

        if matched_keywords:

            with st.expander(
                f"View {len(matched_keywords)} Matching Keywords"
            ):

                st.write(", ".join(matched_keywords))

        else:

            st.info("No matching keywords found.")

    with right_col:

        st.subheader("❌ Missing Keywords")

        if missing_keywords:

            with st.expander(
                f"View {len(missing_keywords)} Missing Keywords"
            ):

                st.write(", ".join(missing_keywords))

        else:

            st.success("Excellent! No missing keywords found.")

    # --------------------------------------------------
    # Skill Match Visualization
    # --------------------------------------------------

    st.divider()

    chart_col1, chart_col2 = st.columns([1, 2])

    with chart_col1:

        st.subheader("📊 Skill Match")

        fig = plot_skill_match(
            len(matched_keywords),
            len(missing_keywords)
        )

        st.pyplot(
            fig,
            clear_figure=True,
            use_container_width=False
        )

    with chart_col2:

        st.subheader("📈 Score Breakdown")

        st.write("### 🎯 ATS Score")

        st.progress(ats_score / 100)

        st.write(f"**{ats_score}%**")

        st.write("### 🧠 Semantic Match")

        st.progress(semantic_score / 100)

        st.write(f"**{semantic_score}%**")

        st.write("### 🔑 Keyword Match")

        st.progress(keyword_score / 100)

        st.write(f"**{keyword_score}%**")

    # --------------------------------------------------
    # Resume Sections
    # --------------------------------------------------

    st.divider()

    st.subheader("📑 Resume Sections")

    available = []
    missing = []

    for section, present in resume_sections.items():

        if present:
            available.append(
                section.replace("_", " ").title()
            )

        else:
            missing.append(
                section.replace("_", " ").title()
            )

    sec1, sec2 = st.columns(2)

    with sec1:

        st.success("Sections Found")

        for item in available:

            st.write(f"✅ {item}")

    with sec2:

        st.error("Missing Sections")

        if missing:

            for item in missing:

                st.write(f"❌ {item}")

        else:

            st.success("All important sections are present.")

    # --------------------------------------------------
    # Resume Improvement Suggestions
    # --------------------------------------------------

    st.divider()

    st.subheader("💡 Resume Improvement Suggestions")

    if suggestions:

        for suggestion in suggestions:

            st.info(suggestion)

    else:

        st.success(
            "🎉 Excellent! No major improvements are recommended."
        )

        # --------------------------------------------------
    # AI Resume Review
    # --------------------------------------------------

    st.divider()

    st.header("🤖 AI Resume Review")

    # Use the already generated review from Session State
    ai_review = st.session_state.ai_review

    with st.container(border=True):

        st.markdown(ai_review)

    # --------------------------------------------------
    # Interview Readiness
    # --------------------------------------------------

    match = re.search(r'(\d{1,3})/100', ai_review)

    if match:

        readiness = min(int(match.group(1)), 100)

        st.divider()

        st.subheader("🎯 Interview Readiness")

        col1, col2 = st.columns([1, 3])

        with col1:

            st.metric(
                "Score",
                f"{readiness}%"
            )

        with col2:

            st.progress(readiness / 100)

    # --------------------------------------------------
    # Recruiter Verdict
    # --------------------------------------------------

    st.divider()

    st.subheader("🏁 Recruiter Verdict")

    if "Strongly Recommend" in ai_review:

        st.success("🟢 Strongly Recommend")

    elif "Recommend" in ai_review and "Strongly" not in ai_review:

        st.success("🟢 Recommend")

    elif "Consider" in ai_review:

        st.warning("🟡 Consider")

    elif "Not Recommended" in ai_review:

        st.error("🔴 Not Recommended")

    else:

        st.info("Recruiter verdict not detected.")


    # --------------------------------------------------
    # Download PDF Report
    # --------------------------------------------------

    st.divider()

    st.subheader("📄 Download Analysis Report")

    with open(pdf_path, "rb") as pdf_file:

        st.download_button(
            label="📥 Download PDF Report",
            data=pdf_file,
            file_name="AI_Resume_Analysis_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    # --------------------------------------------------
    # Footer
    # --------------------------------------------------

st.divider()

st.caption(
    "🤖 AI Resume & Job Match Analyzer • Version 0.4"
)