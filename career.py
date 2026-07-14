def get_career(skills, interest):

    skills = skills.lower()
    interest = interest.lower()

    if "python" in skills or "ai" in interest:
        return "AI / Machine Learning Engineer"

    elif "html" in skills or "css" in skills:
        return "Frontend Web Developer"

    elif "java" in skills:
        return "Java Developer"

    elif "sql" in skills:
        return "Database Administrator"

    elif "c" in skills or "c++" in skills:
        return "Software Developer"

    else:
        return "Keep learning new skills and explore different career options."
