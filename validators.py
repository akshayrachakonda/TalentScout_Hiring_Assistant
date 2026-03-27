import re

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validate_phone(phone):
    return re.match(r"^\+?\d{10,15}$", phone)

def validate_tech_stack(tech_list):
    return all(len(tech) > 1 and any(c.isalpha() for c in tech) for tech in tech_list)