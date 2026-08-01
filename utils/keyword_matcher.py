def match_keywords(resume_tokens, jd_tokens):
    """
    Compare resume and job description keywords.

    Returns:
        matching_keywords
        missing_keywords
    """

    resume_set = set(resume_tokens)
    jd_set = set(jd_tokens)

    matching_keywords = sorted(resume_set.intersection(jd_set))
    missing_keywords = sorted(jd_set.difference(resume_set))

    return matching_keywords, missing_keywords