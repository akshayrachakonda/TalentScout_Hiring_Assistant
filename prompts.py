from llm import call_llm
from llm import cached_llm_call

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

    return cached_llm_call(prompt)

def fallback_response():
    return """
     I'm sorry, I didn't understand that.

    Please provide valid input.

    Example:
    - Name: John Doe
    - Tech Stack: Python, React, MongoDB
    """