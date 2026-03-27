import google.generativeai as genai
from config import MODEL_NAME

model = genai.GenerativeModel(MODEL_NAME)

def call_llm(prompt: str) -> str:
    """Handles Gemini API calls safely."""
    try:
        response = model.generate_content(prompt)

        if response and response.text:
            return response.text
        else:
            return "⚠️ Empty response from AI."

    except Exception as e:
        return f"❌ Gemini Error: {str(e)}"