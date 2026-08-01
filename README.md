# 📄 AI Resume Analyzer

![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub last commit](https://img.shields.io/github/last-commit/harsh8767/AI-Resume-Analyzer)
![GitHub repo size](https://img.shields.io/github/repo-size/harsh8767/AI-Resume-Analyzer)

An AI-powered Resume Analysis application that evaluates resumes against job descriptions using **Natural Language Processing (NLP)**, **Machine Learning**, and **Google Gemini AI**. The application provides ATS compatibility scores, keyword matching, semantic similarity analysis, AI-generated feedback, resume grading, and downloadable PDF reports through an interactive Streamlit interface.

---

# 🚀 Live Demo

🌐 **Try the application here**

**https://ai-resume-analyzer-05rf.onrender.com/**

No installation required—simply upload your resume, paste a job description, and receive an instant analysis.

---

# 📌 Overview

Recruiters spend only a few seconds reviewing each resume, and many organizations rely on Applicant Tracking Systems (ATS) to filter applications before they reach a recruiter.

AI Resume Analyzer helps job seekers optimize their resumes by comparing them with a target Job Description (JD). The system identifies missing keywords, calculates semantic similarity, evaluates ATS compatibility, assigns a resume grade, generates AI-powered feedback, and creates a professional PDF report.

The project combines traditional NLP techniques with modern Large Language Models to simulate a real-world resume screening process.

---

# ⭐ Project Highlights

- 🤖 AI-powered Resume Review using Google Gemini
- 📊 ATS Compatibility Score
- 🔍 Keyword Matching Analysis
- 📈 TF-IDF & Cosine Similarity Matching
- 📝 Resume Section Detection
- ⭐ Resume Grading (A–F)
- 💡 Personalized Resume Suggestions
- 📄 Professional PDF Report Generation
- 🎨 Interactive Streamlit Dashboard
- ☁️ Deployed on Render

---

# 📸 Application Preview

## Home Page

![Home](images/home_page.png)

## ATS Score Analysis

![ATS Score](images/ats_score_analysis.png)

## Resume Rating Dashboard

![Dashboard](images/resume_rating_dashboard.png)

## AI Resume Review

![AI Review](images/ai_resume_review.png)

## PDF Report

![PDF Report](images/pdf_report_download.png)

---

# ✨ Features

- 📄 Upload Resume (PDF)
- 💼 Paste Job Description
- 🤖 AI Resume Review
- 📊 ATS Compatibility Score
- 🔍 Keyword Match Analysis
- 📈 Resume-JD Similarity Score
- 📝 Resume Section Detection
- ⭐ Resume Quality Grading
- 💡 Improvement Suggestions
- 📥 Download Professional PDF Report
- ⚡ Fast Resume Processing
- 🎨 Interactive Dashboard

---

# 🧠 Resume Analysis Workflow

```text
                Resume (PDF)
                      │
                      ▼
              Text Extraction (PyMuPDF)
                      │
                      ▼
              Text Cleaning & Processing
                      │
                      ▼
        Resume + Job Description Comparison
                      │
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
Keyword Match   Semantic Similarity   Section Analysis
      │               │                │
      └───────────────┼────────────────┘
                      ▼
              ATS Score Calculation
                      │
                      ▼
             Resume Grade Assignment
                      │
                      ▼
           AI-powered Resume Feedback
                      │
                      ▼
          Professional PDF Report
```

---

# 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| 🐍 Language | Python |
| 🎨 Framework | Streamlit |
| 🧠 Natural Language Processing | NLTK |
| 🤖 Machine Learning | Scikit-learn |
| 📊 Similarity Measurement | TF-IDF & Cosine Similarity |
| 📈 Data Processing | Pandas, NumPy |
| 📄 PDF Processing | PyMuPDF |
| 📉 Visualization | Matplotlib |
| ✨ AI Integration | Google Gemini API (`google-genai`) |
| 📑 Report Generation | ReportLab |
| ☁️ Deployment | Render |
---

# 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── runtime.txt
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
│
├── assets/
│   └── styles.css
│
├── images/
│   ├── home_page.png
│   ├── ats_score_analysis.png
│   ├── resume_rating_dashboard.png
│   ├── ai_resume_review.png
│   └── pdf_report_download.png
│
├── reports/
│   └── .gitkeep
│
├── sample_data/
│   ├── resumes/
│   │   ├── data_analyst_resume.pdf
│   │   ├── data_scientist_resume.pdf
│   │   ├── frontend_developer_resume.pdf
│   │   ├── python_developer_resume.pdf
│   │   └── software_engineer_resume.pdf
│   │
│   └── job_descriptions/
│
└── utils/
    ├── ai_review.py
    ├── ats_score.py
    ├── charts.py
    ├── keyword_matcher.py
    ├── pdf_report.py
    ├── resume_grade.py
    ├── section_checker.py
    ├── similarity.py
    ├── suggestions.py
    └── text_processor.py
```

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/harsh8767/AI-Resume-Analyzer.git
```

## 2. Navigate into the Project

```bash
cd AI-Resume-Analyzer
```

## 3. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Configure Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_google_gemini_api_key
```

Obtain your API key from Google AI Studio.

---

## 6. Run the Application

```bash
streamlit run app.py
```

Open your browser and visit

```
http://localhost:8501
```

---

# 📊 Evaluation Metrics

The application evaluates resumes using multiple criteria:

- ATS Compatibility Score
- Resume-JD Similarity Score
- Keyword Match Percentage
- Resume Completeness
- Resume Structure
- Missing Keywords
- Resume Grade (A–F)
- AI-generated Resume Feedback

---

# 📋 Sample Files

The repository includes sample resumes and job descriptions for testing.

```text
sample_data/
├── resumes/
└── job_descriptions/
```

These files allow users to explore the application's functionality without creating their own inputs.

---

# ⚠️ Known Limitations

- Supports PDF resumes only.
- AI feedback depends on the response quality of the language model.
- ATS score is heuristic-based and may differ from commercial ATS software.
- Keyword matching cannot fully replicate recruiter decision-making.

---

# 🚀 Future Improvements

- DOCX Resume Support
- Resume History
- User Authentication
- Multiple Resume Comparison
- Resume Templates
- Cover Letter Generator
- Job Recommendation System
- Resume Version Tracking
- Interview Question Generator
- Dark Mode

---

# 🙏 Acknowledgements

This project makes use of the following open-source technologies:

- Streamlit
- Google Gemini API
- NLTK
- Scikit-learn
- PyMuPDF
- ReportLab
- Pandas
- NumPy
- Matplotlib
- Open Source Python Community

---

# 👨‍💻 Developer

## Harsh Chavan

Computer Engineering Student

Passionate about Artificial Intelligence, Machine Learning, Data Science, and Python Development.

**GitHub**

https://github.com/harsh8767

**LinkedIn**

https://www.linkedin.com/in/harsh-chavan-1646a2257/

---

# 📜 License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more information.