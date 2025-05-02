# 🧾 Microservice PDF Generator – Dockerized Demo Project  

Projekt för att ffa lära sig containersering och kommunikation mellan microtjänster med Docker compose  

## 📦 Projektstruktur

```
.
├── backend/                # Reservdel från tidigare struktur – ej aktiv i Compose
├── pdf_service/            # Flask-app som genererar PDF från text
│   ├── Dockerfile
│   ├── app.py
│   ├── pdf_service.py
│   └── requirements.txt
├── webapp/                 # Flask-webbapp med HTML-formulär
│   ├── Dockerfile
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   │   └── style.css (valfritt)
│   └── requirements.txt
├── infrastructure/         # Innehåller Docker Compose och framtida infra (Terraform, etc.)
│   └── docker-compose.yml
└── README.md               # Denna fil
```

---

## 🚀 Så kör du projektet

1. Skapa ett nätverk och starta tjänsterna med Compose:
```bash
cd infrastructure
docker compose up --build
```

2. Gå till `http://localhost:5001/` i webbläsaren  
3. Fyll i text → klicka på **Skapa PDF** → PDF genereras av `pdf_service`

---

## 🐳 Mikrotjänster

| Tjänst       | Port     | Beskrivning                            |
|--------------|----------|-----------------------------------------|
| `webapp`     | `5001`   | HTML-gränssnitt + skickar text till PDF |
| `pdf_service`| `5002`   | Tar emot text och returnerar PDF       |

---

## 🧪 Utvecklartips

- Ändringar i koden kräver rebuild:  
  ```bash
  docker compose up --build
  ```
- Loggar:
  ```bash
  docker compose logs -f
  ```
- Stoppa allt:
  ```bash
  docker compose down
  ```

---

## 🧠 Lärdomar

- Flask i mikroformat
- Kommunikation mellan containrar
- Docker Compose som orkestrator
- HTTP mellan backend-tjänster
- Miljö utan extern server

---

## 🛠️ Nästa steg

- 🧾 Lägga till volymer för att spara genererade PDF:er
- 🔐 Hantera miljövariabler
- 📦 Paketera för produktion
- 🐘 Lägg till databas eller andra mikrotjänster

---

Byggt med ❤️ av Patrick.
