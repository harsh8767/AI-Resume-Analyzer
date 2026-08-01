def generate_suggestions(
    ats_score,
    missing_keywords,
    resume_sections
):
    """
    Generate resume improvement suggestions.
    """

    suggestions = []

    # ATS Score
    if ats_score < 60:
        suggestions.append(
            "Increase ATS compatibility by including more job-specific keywords."
        )

    # Missing Skills
    if len(missing_keywords) > 0:
        top_missing = ", ".join(missing_keywords[:8])

        suggestions.append(
            f"Consider adding these important skills: {top_missing}."
        )

    # Resume Sections
    for section, present in resume_sections.items():

        if not present:
            suggestions.append(
                f"Add a '{section.replace('_', ' ').title()}' section."
            )

    # Strong Resume
    if ats_score >= 85:
        suggestions.append(
            "Excellent resume! Continue quantifying achievements and keeping skills updated."
        )

    return suggestions