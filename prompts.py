from llm import call_llm

def generate_questions(tech_stack, experience):
    prompt = f"""
    You are a senior technical interviewer.

    Generate 3-5 interview questions for EACH technology.

    Candidate Experience: {experience} years
    
    Tech Stack: {tech_stack}

    Rules:
    - Separate questions by technology
    - Keep questions concise
    - Mix conceptual + practical

    Output format:

    Technology: Python
    1. Question
    2. Question

    Technology: React
    1. Question
    """

    return call_llm(prompt)