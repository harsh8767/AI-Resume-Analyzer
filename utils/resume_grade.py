def get_resume_grade(score):
    """
    Returns resume grade, stars and recommendation
    based on ATS score.
    """

    if score >= 90:
        return "A+", "⭐⭐⭐⭐⭐", "Excellent Resume"

    elif score >= 80:
        return "A", "⭐⭐⭐⭐☆", "Very Strong Resume"

    elif score >= 70:
        return "B+", "⭐⭐⭐☆☆", "Good Resume"

    elif score >= 60:
        return "B", "⭐⭐⭐☆☆", "Above Average Resume"

    elif score >= 50:
        return "C+", "⭐⭐☆☆☆", "Needs Improvement"

    elif score >= 40:
        return "C", "⭐⭐☆☆☆", "Weak Resume"

    else:
        return "D", "⭐☆☆☆☆", "Poor Resume"