from flask import Flask, request, Response
from pdf_service import generate_pdf  # Vi använder din funktion från tidigare

app = Flask(__name__)

@app.route("/generate_pdf", methods=["POST"])
def handle_generate_pdf():
    data = request.get_json()
    text = data.get("text", "")

    print("📥 Text mottagen:", text)
    pdf_bytes = generate_pdf(text)

    return Response(pdf_bytes, mimetype="application/pdf")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
