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
