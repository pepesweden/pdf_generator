# Automation Project Scaffold 🚀

Detta är en mall för att snabbt starta nya automationsprojekt.  
Innehåller grundstruktur för:

- Backend (Flask-baserad server)
- Webapp (HTML + CSS + JS)
- Infrastruktur (Terraform templates)

---

## 🛠️ Struktur

```bash
automation-project_template/
├── backend/
│   ├── main.py        # Startar appen
│   ├── config.py      # Konfiguration
│   ├── models/        # Backend-modeller
│   ├── utils/         # Hjälpfunktioner
│   └── requirements.txt
├── webapp/
│   ├── static/        # CSS och JS
│   └── templates/     # HTML-filer
├── infrastructure/    # Terraform-filer
└── README.md
```

---

## 🚀 Hur skapar jag ett nytt projekt?

1. Klicka på **"Use this template"** ovanför.
2. Välj nytt namn och skapa nytt repo.
3. Klona ditt nya repo till din dator:
   ```bash
   git clone https://github.com/ditt-användarnamn/ditt-nya-repo.git
   cd ditt-nya-repo
   ```
4. Starta backend-servern:
   ```bash
   cd backend
   python3 main.py
   ```

---

## 📋 Kom ihåg

- Lägg till eventuella Python-paket i `requirements.txt`
- Skapa `.env`-fil om du använder hemliga nycklar (och ignorera med `.gitignore`)
- Du kan fritt ändra strukturen efter behov!

---

## 📢 Tips

- Använd `url_for('static', filename='style.css')` i dina HTML-filer.
- Håll varje tjänst (`models/`, `utils/`) modulariserad för skalbarhet.

---

# 🚀 Happy Building!
