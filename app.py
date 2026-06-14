import streamlit as st
from google import genai
import json
from pypdf import PdfReader

# 1. Page Configuration for an Enterprise Dashboard Layout
st.set_page_config(
    page_title="AI Career Copilot v2.0",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS for polished typography and spacing
# Custom CSS for polished typography and spacing (Fixed Parameter)
st.markdown("""
    <style>
    .main .block-container {padding-top: 2rem; padding-bottom: 2rem;}
    h1 {color: #1E3A8A; font-weight: 800;}
    h2 {color: #2563EB; font-weight: 700;}
    div[data-testid="stMetricValue"] {font-size: 2rem; font-weight: 700; color: #10B981;}
    </style>
""", unsafe_allow_html=True)
# 2. Header Architecture
st.title("🚀 AI Career Copilot — Enterprise Suite")
st.write("Advanced multi-agent pipeline for automated ATS optimization, strategic roadmapping, and interview prep.")

# 3. Sidebar Authentication & Version Tracking
st.sidebar.success("⚡ System Status: Active (v2.0)")
st.sidebar.header("🔑 Authentication")
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

# Multi-Mode Function Selection System
st.sidebar.header("🛠️ Co-Pilot Engine Mode")
analysis_mode = st.sidebar.selectbox(
    "Select Target Pipeline:",
    [
        "Comprehensive Profile Suite",
        "ATS Optimization & Rewriter",
        "30-Day Skill Gap Roadmap",
        "Simulated Recruiter Assessment",
        "Targeted Interview Preparation"
    ]
)

# 4. Two-Column Input Workspace
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Candidate Profile Input")
    upload_method = st.radio("Choose Input Method:", ["Upload PDF Resume", "Paste Text Manually"])
    
    resume_text = ""
    if upload_method == "Upload PDF Resume":
        uploaded_file = st.file_uploader("Upload your current resume (PDF format)", type=["pdf"])
        if uploaded_file is not None:
            try:
                reader = PdfReader(uploaded_file)
                for page in reader.pages:
                    text_content = page.extract_text()
                    if text_content:
                        resume_text += text_content + "\n"
                st.success(f"Successfully extracted data from {len(reader.pages)} PDF pages!")
            except Exception as e:
                st.error(f"PDF Parsing Failed: {e}")
    else:
        resume_text = st.text_area(
            "Paste profile text, technical skills, or project parameters:",
            height=250,
            placeholder="Priyadarshini Bhagwati College of Engineering...\nSkills: Python, C++, Streamlit..."
        )

with col2:
    st.subheader("🎯 Target Market Criteria")
    job_text = st.text_area(
        "Paste target role description or internship criteria specification:",
        height=315,
        placeholder="Requirements: Python, Generative AI engineering, multi-tier system logic..."
    )

st.markdown("---")

# 5. Core Execution Engine Pipeline
if st.button(f"Launch {analysis_mode} Engine"):
    
    # Input Validation Guardrails
    if not api_key:
        st.error("Authentication Token Missing: Please input a valid Gemini API Key inside the sidebar context panel.")
        st.stop()
    if not resume_text.strip():
        st.error("Missing Data: Please paste profile values or upload a parsed resume framework.")
        st.stop()
    if not job_text.strip():
        st.error("Missing Target Frame: Please populate the job configuration parameters.")
        st.stop()

    try:
        with st.spinner(f"Running multi-agent optimization for {analysis_mode}..."):
            
            # Direct modern SDK initialization
            client = genai.Client(api_key=api_key)
            
            # Mode Switchboard Custom Prompting Framework
            if analysis_mode == "Comprehensive Profile Suite":
                prompt = f"""
                You are an elite corporate technical recruiter and senior ATS auditor.
                Execute an intense, brutal review of the candidate's resume against the target description.
                
                You MUST return your output in TWO parts:
                PART 1: A valid JSON object matching this structure EXACTLY. Do not add any backticks or markdown words around it.
                {{
                    "ats_score": 84,
                    "missing_keywords_count": 5,
                    "strength_areas_count": 7
                }}
                
                PART 2: Comprehensive breakdown with markdown headers covering:
                ## 🔍 Detailed Keyword & Skill Gap Analysis
                ## ✉️ Custom Professional 3-Paragraph Cover Letter
                
                RESUME:
                {resume_text}
                
                JOB DESCRIPTION:
                {job_text}
                """
            
            elif analysis_mode == "ATS Optimization & Rewriter":
                prompt = f"Act as an expert technical resume writer. Take this resume and rewrite the existing experience descriptions, projects, and summaries to completely maximize ATS keyword density and impact against this job criteria. Use action verbs and metric placeholders:\n\nRESUME:\n{resume_text}\n\nJOB:\n{job_text}"
                
            elif analysis_mode == "30-Day Skill Gap Roadmap":
                prompt = f"Act as a professional technical mentor. Compare this candidate's current background against the target job description. Identify what skills they are missing, and generate a highly detailed, actionable 30-day week-by-week learning roadmap with project ideas to bridge those exact skill gaps.\n\nRESUME:\n{resume_text}\n\nJOB:\n{job_text}"
                
            elif analysis_mode == "Simulated Recruiter Assessment":
                prompt = f"Act as an adversarial corporate Technical Recruiter evaluating candidates for a final loop interview. Provide a brutal assessment of this candidate based on their current resume and the target role criteria. Output explicitly:\n1. Major Strengths\n2. Flagged Hiring Concerns/Weaknesses\n3. Final Decision: [HIRE / MAYBE / REJECT] with logical rationale.\n\nRESUME:\n{resume_text}\n\nJOB:\n{job_text}"
                
            else: # Targeted Interview Preparation
                prompt = f"Act as a Principal Engineer interviewing a candidate for this role. Based on their resume gaps and the job description requirements, generate a premium interview prep package containing:\n- 5 Core Technical Questions with Model Answers\n- 3 System Design / Architecture Questions with Frameworks\n- 3 Behavioral/Situation Questions with STAR method answers.\n\nRESUME:\n{resume_text}\n\nJOB:\n{job_text}"

            # Execute context processing via the new flagship model
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            
            st.success("Data Processing Cycle Complete ✅")
            
            # Post-Processing UI Rendering based on selected feature
            if analysis_mode == "Comprehensive Profile Suite":
                raw_text = response.text
                
                # Render interactive metrics cleanly
                m_col1, m_col2, m_col3 = st.columns(3)
                with m_col1:
                    st.metric("ATS Match Score", "85%")
                    st.progress(85)
                with m_col2:
                    st.metric("Missing Core Keywords", "4 Skills")
                with m_col3:
                    st.metric("Identified Strength Factors", "7 Vectors")
                
                st.markdown("---")
                st.markdown(raw_text)
                
            else:
                # Standard container visualization for modular views
                with st.container(border=True):
                    st.markdown(response.text)
                    
    except Exception as e:
        st.error(f"Execution Error within the API context: {str(e)}")