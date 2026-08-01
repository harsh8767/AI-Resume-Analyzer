import streamlit as st
from utils.resume_parser import extract_resume_text

# -----------------------
# Page Configuration
# -----------------------
st.set_page_config(
    page_title="AI Resume & Job Match Analyzer",
    page_icon="📄",
    layout="wide"
)

# -----------------------
# Load CSS
# -----------------------
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------
# Sidebar
# -----------------------
with st.sidebar:
    st.title("📄 Resume Analyzer")
    st.divider()

    st.success("Version 0.1")

    st.write("Current Sprint")
    st.info("Professional UI")

# -----------------------
# Header
# -----------------------
st.markdown(
    """
    <h1 class="main-title">
    AI Resume & Job Match Analyzer
    </h1>

    <p class="sub-title">
    Analyze resumes against job descriptions using AI-powered insights.
    </p>
    """,
    unsafe_allow_html=True,
)

# -----------------------
# Upload Section
# -----------------------
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

if st.button("🔍 Analyze Resume", use_container_width=True):

    if resume is None:
        st.warning("Please upload a resume.")
    else:

        resume_text = extract_resume_text(resume)

        st.success("Resume parsed successfully!")

        st.text_area(
            "Extracted Resume Text",
            resume_text,
            height=300,
        )

st.divider()

# -----------------------
# Placeholder Results
# -----------------------
st.header("Analysis Results")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("ATS Score", "--")

with col2:
    st.metric("Match Score", "--")

with col3:
    st.metric("Missing Skills", "--")

st.info("Upload a resume and job description to begin analysis.")