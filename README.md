# 💼 CareerCopilot-AI

An AI-powered career assistant that helps candidates optimize their resumes for specific job roles by analyzing skill alignment, identifying ATS keyword gaps, recommending profile improvements, generating personalized cover letters, and creating targeted career development plans using Google Gemini.

---

## 🚀 Overview

CareerCopilot-AI helps job seekers increase their chances of getting shortlisted by comparing their resume against a target job description and providing actionable recommendations.

The platform leverages Google's Gemini AI to perform intelligent resume analysis, ATS optimization, recruiter-style assessments, interview preparation, and personalized learning roadmap generation.

---

## ✨ Features

### 📊 Comprehensive Profile Suite
Runs a deep keyword and skill gap analysis against the target role and automatically generates a professional 3-paragraph cover letter tailored to the position.

### 📝 ATS Optimization & Rewriter
Re-engineers existing experience descriptions, project summaries, and profile sections to maximize ATS compatibility using targeted keywords and impactful action verbs.

### 🛣️ 30-Day Skill Gap Roadmap
Identifies missing skills and generates a detailed week-by-week learning roadmap with actionable project milestones to help candidates bridge knowledge gaps.

### 🔍 Simulated Recruiter Assessment
Provides a recruiter-style evaluation highlighting strengths, concerns, and a final hiring recommendation:

- HIRE
- MAYBE
- REJECT

### 🎯 Targeted Interview Preparation
Creates an interview preparation package containing:

- Technical interview questions with model answers
- System design and architecture questions
- Behavioral interview questions using the STAR framework

### 📄 PDF Resume Upload Support
Upload resumes directly in PDF format and automatically extract content using PyPDF for analysis.

---

## 🏗️ System Workflow

```text
Resume Input (PDF / Manual Entry)
              │
              ▼
Target Job Description
              │
              ▼
Google Gemini Analysis Engine
              │
              ├── ATS Optimization
              ├── Skill Gap Detection
              ├── Resume Rewriting
              ├── Recruiter Assessment
              ├── Interview Preparation
              └── Learning Roadmap Generation
              │
              ▼
Personalized Career Development Report
```

---

## 🛠️ Technology Stack

| Component | Technology |
|------------|------------|
| Frontend | Streamlit |
| Backend | Python |
| AI Model | Google Gemini 2.5 Flash |
| API Integration | Google GenAI SDK |
| PDF Processing | PyPDF |

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Shrutimendhe76/CareerCopilot-AI.git
cd CareerCopilot-AI
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

If you are not using a requirements file:

```bash
pip install streamlit google-genai pypdf
```

### 3. Run the Application

```bash
streamlit run app.py
```

---

## 🔑 API Setup

Generate a Gemini API key from:

https://aistudio.google.com/app/apikey

Enter the API key in the sidebar before launching any analysis pipeline.

---

## 📖 How to Use

1. Enter your Gemini API Key.
2. Upload your resume PDF or paste profile information manually.
3. Paste the target job description or internship criteria.
4. Select your preferred analysis mode from the **Co-Pilot Engine Mode** menu.
5. Click **Launch Engine**.
6. Review the AI-generated insights, recommendations, and reports.

---

## 🎯 Example Use Cases

- Internship Applications
- Campus Placements
- Entry-Level Job Applications
- Career Switching
- Resume Optimization
- ATS Preparation
- Interview Preparation
- Skill Development Planning

---

## 🔮 Future Enhancements

- Dynamic ATS score extraction from structured JSON responses
- Downloadable PDF reports
- LinkedIn profile optimization
- Multi-role resume version generation
- Company-specific interview preparation
- Application tracking dashboard
- Voice-based interview simulation

---

## 👩‍💻 Team

Developed as part of a hackathon project focused on applying Generative AI to solve real-world career preparation and professional development challenges.

---

## 🌟 Project Vision

Our goal is to simplify career preparation by helping candidates build stronger resumes, prepare for interviews, identify skill gaps, and align themselves more effectively with modern hiring requirements through AI-driven insights and personalized recommendations.
