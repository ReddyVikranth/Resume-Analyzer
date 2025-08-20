import os
from flask import Flask, request, jsonify, send_from_directory
from utils import extract_text_from_pdf, extract_text_from_docx, clean_text, calculate_similarity

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    job_desc = request.form['job_description']
    file = request.files['resume']

    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Extract text
    if file.filename.endswith(".pdf"):
        resume_text = extract_text_from_pdf(file_path)
    elif file.filename.endswith(".docx"):
        resume_text = extract_text_from_docx(file_path)
    else:
        return jsonify({"error": "Only .pdf and .docx allowed"}), 400

    # Clean & compare
    score = calculate_similarity(clean_text(job_desc), clean_text(resume_text))
    return jsonify({"match_score": score})

@app.route('/')
def serve_frontend():
    return send_from_directory('../frontend', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('../frontend', path)

if __name__ == '__main__':
    app.run(debug=True)
