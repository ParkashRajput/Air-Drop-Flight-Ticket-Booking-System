# ✈️ Flight Ticket Booking System

A full-featured **Flight Ticket Booking System** built using **Django**, allowing users to search, book, and manage flight tickets. The system also provides an **admin interface** to manage flights, bookings, and users efficiently.

---

## 🗂️ Project Structure

```
FLIGHT-TICKET-BOOKING-MASTER/
│
├── capstone/                # Main project configuration
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── utils.py
│   └── wsgi.py
│
├── Data/                    # Flight and airport datasets
│   ├── add_places.py
│   ├── airports.csv
│   ├── domestic_flights.csv
│   └── international_flights.csv
│
├── flight/                  # Core Django app
│   ├── admin.py
│   ├── apps.py
│   ├── constant.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   ├── views.py
│   ├── migrations/
│   ├── static/              # CSS, JS, images
│   └── templates/flight/    # HTML Templates
│       ├── index.html
│       ├── login.html
│       ├── register.html
│       ├── search.html
│       ├── book.html
│       ├── bookings.html
│       ├── payment.html
│       ├── payment_process.html
│       └── layout.html
│
└── manage.py
```

---

## 🚀 Features

✅ **User Side:**
- ✈️ Flight search (domestic & international)
- 🧳 Ticket booking and payment simulation
- 📜 View and manage booking history
- 🔐 User login & registration

✅ **Admin Side:**
- 🧩 Add, update, or delete flight details
- 🧾 Manage user bookings
- ✅ Accept or deny booking requests

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/flight-ticket-booking.git
cd flight-ticket-booking
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate       # For Windows
# OR
source venv/bin/activate    # For Linux/Mac
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser (Admin Panel Access)
```bash
python manage.py createsuperuser
```

### 6️⃣ Start the Server
```bash
python manage.py runserver
```

---

## 🌐 Access

- **User Interface:** http://127.0.0.1:8000  
- **Admin Panel:** http://127.0.0.1:8000/admin

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | HTML, CSS, Bootstrap |
| **Backend** | Django (Python) |
| **Database** | SQLite3 |
| **Data** | CSV datasets (Flights & Airports) |

---

## 📸 Screenshots

| Page | Description |
|------|--------------|
| 🏠 Home Page | Flight search and listings |
| 🔐 Login / Register | User authentication |
| ✈️ Booking Page | Select and confirm flight tickets |
| 💳 Payment Page | Simulated payment process |
| 🧾 Admin Dashboard | Manage flights and users |

---

## 📂 Dataset Information

The project uses three CSV files stored in the `/Data` folder:
- `airports.csv` – Airport details
- `domestic_flights.csv` – Domestic flight data
- `international_flights.csv` – International flight data

These files are used for dynamic flight search and display functionality.

---

## 💡 Future Enhancements

- 🪙 Real payment gateway integration
- 📱 Mobile-responsive UI
- 🛰️ Live flight tracking API integration
- 📤 Email notifications for booking confirmation

---

## 👨‍💻 Author

**Developed by:** [Parkash Rajput]  
**GitHub:** [@ParkashRajput](https://github.com/ParkashRajput)  
**Tech Stack:** Django | Python | HTML | CSS | SQLite

---

## 🏁 License

This project is licensed under the **MIT License** – feel free to use and modify it.
