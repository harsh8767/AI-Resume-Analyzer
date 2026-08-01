def check_resume_sections(resume_text):
    """
    Checks whether important resume sections are present.
    """

    text = resume_text.lower()

    sections = {
        "Contact Information": True if "@" in text else False,

        "Professional Summary":
            any(keyword in text for keyword in [
                "summary",
                "profile",
                "objective",
                "about"
            ]),

        "Skills":
            "skills" in text,

        "Education":
            any(keyword in text for keyword in [
                "education",
                "bachelor",
                "master",
                "university",
                "college"
            ]),

        "Experience":
            any(keyword in text for keyword in [
                "experience",
                "intern",
                "employment",
                "work experience"
            ]),

        "Projects":
            "project" in text,

        "Certifications":
            any(keyword in text for keyword in [
                "certification",
                "certificate",
                "certifications"
            ]),

        "Achievements":
            any(keyword in text for keyword in [
                "achievement",
                "award",
                "honor",
                "accomplishment"
            ])
    }

    return sections