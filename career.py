def get_career(skills, interest):

    skills = skills.lower()
    interest = interest.lower()

    if "python" in skills or "artificial intelligence" in interest or "ai" in interest:
        return "AI / Machine Learning Engineer"

    elif "data science" in interest or "data" in interest:
        return "Data Scientist"

    elif "html" in skills or "css" in skills or "javascript" in skills:
        return "Frontend Web Developer"

    elif "react" in skills:
        return "Frontend Developer"

    elif "java" in skills:
        return "Java Developer"

    elif "sql" in skills:
        return "Database Administrator"

    elif "c++" in skills or "c" in skills:
        return "Software Developer"

    elif "cyber" in interest:
        return "Cyber Security Analyst"

    elif "cloud" in interest:
        return "Cloud Engineer"

    elif "android" in interest:
        return "Android App Developer"

    elif "web" in interest:
        return "Full Stack Web Developer"

    elif "design" in interest:
        return "UI/UX Designer"

    elif "game" in interest:
        return "Game Developer"

    else:
        return "Software Engineer. Try learning Python, SQL, HTML and JavaScript to explore more career options."
