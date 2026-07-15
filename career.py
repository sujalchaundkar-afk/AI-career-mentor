def get_career(skills, interest):

    skills = skills.lower()
    interest = interest.lower()

    if "python" in skills or "artificial intelligence" in interest or "ai" in interest:
        return "AI / Machine Learning Engineer"

    elif "html" in skills or "css" in skills or "javascript" in skills:
        return "Frontend Web Developer"

    elif "java" in skills:
        return "Java Developer"

    elif "sql" in skills:
        return "Database Administrator"

    elif "c" in skills or "c++" in skills:
        return "Software Developer"

    elif "data" in interest:
        return "Data Analyst"

    elif "cyber" in interest:
        return "Cyber Security Analyst"

    elif "cloud" in interest:
        return "Cloud Engineer"

    else:
        return "Sorry, I could not find a matching career. Try adding more skills."
