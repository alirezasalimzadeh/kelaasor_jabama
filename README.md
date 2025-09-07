# 🏝️ Kelaasor-jabama
A Django-based booking and transaction API that reads hotel, reservation, and payment data from JSON files, calculates reservation status using Jalali/Hijri dates, and returns structured JSON responses for easy integration with front‑end applications.


# 🚀 Features
Dynamic Data Loading – Reads hotels, reservations, and transactions from JSON files inside the project.

Date Handling – Uses jdatetime and hijridate to work with Jalali and Hijri dates.

Reservation Status – Marks reservations as past, present, or future automatically.

JSON API – Returns clean, structured JSON for easy consumption by front‑end apps.

Modular Structure – Static data is separated from logic for maintainability.

# 📌 Endpoints
hotels/ – List of hotels

reservations/ – List of reservations with status

transactions/ – List of transactions


# 📦 Installation
Before running the project, make sure you have the essential dependencies installed. These packages handle the Django framework and date conversions for Jalali and Hijri calendars.

🔹 Create & Activate Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
.venv\Scripts\activate      # Windows
```

🔹 Install Required Packages
```bash
pip install Django==5.2.6
pip install django-jalali==7.4.0 django-jalali-date==2.0.0
pip install jdatetime==5.2.0
pip install hijri-converter==2.3.2.post1 hijridate==2.3.0
```

# 💡 Tip
You can also install all dependencies (including secondary ones) from requirements.txt:
```bash
pip install -r requirements.txt
```
