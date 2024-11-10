from flask import Flask, render_template, request, jsonify, send_file
import openai
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_resume(job_description):
    # OpenAI API call to generate resume
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Create a resume based on the following job description:\n\n{job_description}"}
        ],
        max_tokens=500
    )
    return response.choices[0].message.content.strip()

def create_pdf(resume_text):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Add title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 50, "Generated Resume")

    # Add resume content
    c.setFont("Helvetica", 12)
    text = c.beginText(50, height - 100)
    text.setLeading(14)
    text.textLines(resume_text)
    c.drawText(text)
    c.save()

    buffer.seek(0)
    return buffer

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_resume", methods=["POST"])
def generate_resume_route():
    job_description = request.form.get("job_description")
    if not job_description:
        return jsonify({"error": "Job description is required."}), 400

    try:
        resume = generate_resume(job_description)
        return jsonify({"resume": resume})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/download_pdf", methods=["POST"])
def download_pdf():
    job_description = request.form.get("job_description")
    if not job_description:
        return jsonify({"error": "Job description is required."}), 400

    resume_text = generate_resume(job_description)
    pdf_buffer = create_pdf(resume_text)
    return send_file(pdf_buffer, as_attachment=True, download_name="generated_resume.pdf", mimetype="application/pdf")

if __name__ == "__main__":
    app.run(debug=True)
