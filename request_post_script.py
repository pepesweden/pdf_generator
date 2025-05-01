import requests

url = "http://localhost:5002/generate_pdf"

headers = {
    "Content-Type": "application/json",
}

data = {
    "text": "PDF-test från Patrick via requests"
}

# ⛔ requests.get → fel metod
# ✅ Vi ska använda POST och skicka json-data
response = requests.post(url, json=data, headers=headers)

# Spara PDF:en om det gick bra
if response.status_code == 200:
    with open("test_from_requests.pdf", "wb") as f:
        f.write(response.content)
    print("✅ PDF sparad från Python!")
else:
    print("❌ Något gick fel:", response.status_code)
    print(response.text)
