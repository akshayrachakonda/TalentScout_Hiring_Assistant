# 🤖 TalentScout AI Hiring Assistant

An intelligent AI-powered chatbot designed to streamline the initial candidate screening process for a fictional recruitment agency, **TalentScout**.

This chatbot collects candidate details and generates **personalized technical interview questions** based on the candidate’s declared tech stack using **Google Gemini API**.

---

## 🚀 Features

### ✅ Candidate Information Collection
- Full Name
- Email Address (validated)
- Phone Number (validated)
- Years of Experience
- Desired Role
- Current Location
- Tech Stack

---

### 🧠 AI-Powered Question Generation
- Generates **3–5 questions per technology**
- Adapts based on **candidate experience**
- Covers:
  - Conceptual questions
  - Practical scenarios
  - Real-world use cases

---

### 🔄 Context-Aware Conversation
- Maintains conversation flow using session state
- Step-by-step guided interaction

---

### ⚠️ Error Handling & Fallback
- Handles invalid inputs (email, phone)
- Graceful fallback if AI fails

---

### 🔐 Data Privacy & Security
- No data is stored permanently
- Uses `.env` for API key protection
- Session-based data handling (GDPR-friendly)

---

## 🏗️ Project Structure

talentscout/
│
├── app.py # Main Streamlit app (UI + flow)
├── config.py # API configuration
├── llm.py # Gemini API handler
├── prompts.py # Prompt engineering logic
├── validators.py # Input validation
├── state.py # Session state management
├── requirements.txt # Dependencies
├── .gitignore # Ignore sensitive files
└── README.md # Documentation


---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd talentscout
```
2️⃣  Create Virtual Environment (Recommended)
```
python -m venv venv
venv\Scripts\activate   # Windows
```
3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
4️⃣ Setup Environment Variables

Create a .env file in the root directory:
```
GEMINI_API_KEY=your_api_key_here
```
▶️ Running the Application
```
streamlit run app.py
```
