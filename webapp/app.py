from flask import Flask, render_template, request, Response
import requests

app = Flask(__name__)

PDF_SERVICE_URL = "http://localhost:5001/generate_pdf"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    text = request.form.get("text", "")

    res = requests.post(PDF_SERVICE_URL, json={"text": text})
    
    if res.status_code == 200:
        return Response(
            res.content,
            mimetype="application/pdf",
            headers={"Content-Disposition": "inline; filename=generated.pdf"}
        )
    else:
        return f"Fel från pdf-tjänsten: {res.status_code}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
