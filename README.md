# ⚡ Resume Analyzer  

A simple yet powerful **AI-powered Resume Analyzer** that compares a candidate’s resume with a given **Job Description (JD)** and provides a **match score (%)**.  
This project extracts text from resumes (`.pdf` and `.docx`), cleans the data, and applies **TF-IDF + Cosine Similarity** to evaluate how well a resume aligns with a job description.  

✨ Designed with a modern **Web3-style frontend** and a lightweight **Flask backend**.  

---

## 🚀 Features  
- 📄 Upload resumes in **PDF or DOCX** format.  
- 📝 Enter any **Job Description** in the UI.  
- ⚡ Generates a **match score (%)** using NLP techniques.  
- 🎨 Sleek **Web3-inspired UI** with glassmorphism and gradient styling.  
- 🔍 Fast and lightweight — built with **Flask + Vanilla JS**.  

---

## 🖼️ Demo Preview  
*(You can add a screenshot or GIF here once you run it locally)*  

Example UI:  
```
Job Description: Looking for a Python Developer with Flask, APIs, and SQL skills.  

Resume Uploaded: JohnDoe.pdf  

Output → Match Score: 78%
```

---

## 📂 Project Structure  
```
resume-analyzer/
│── backend/
│   ├── app.py               # Flask backend
│   ├── utils.py             # Resume parsing + similarity logic
│   ├── requirements.txt     # Python dependencies
│
│── frontend/
│   ├── index.html           # UI
│   ├── style.css            # Styling (Web3 inspired)
│   ├── script.js            # Frontend logic
│
│── uploads/                 # Uploaded resumes
```

---

## ⚙️ Installation & Setup  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer/backend
```

### 2️⃣ Create Virtual Environment & Install Dependencies  
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate    # On Windows

pip install -r requirements.txt
```

### 3️⃣ Run the Flask Server  
```bash
python app.py
```
Server runs at: `http://127.0.0.1:5000`  

### 4️⃣ Open Frontend  
Visit `http://127.0.0.1:5000` in your browser.  

---

## 🛠️ Tech Stack  
- **Backend** → Python, Flask  
- **Frontend** → HTML, CSS (Glassmorphism, Gradients), JavaScript  
- **NLP** → TF-IDF, Cosine Similarity  
- **Parsing** → PyPDF2, python-docx  

---

## 🌟 Future Improvements  
- 🔑 Highlight missing **skills/keywords** in the resume.  
- 📊 Show a detailed **skill match breakdown**.  
- 🌐 Deploy on **Heroku / Vercel** for live demo.  

---

## 🤝 Contributing  
Contributions are welcome! Feel free to fork this repo, create a branch, and submit a PR.  

---

## 📜 License  
This project is licensed under the **MIT License**.  
