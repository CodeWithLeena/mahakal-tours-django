
# 🕉️ Mahakal Tour & Travels — Django Website

## Website Features
- Full animated homepage (particle effects, scroll reveal, counter animations)
- Mahakal/saffron theme with dark background
- All 9 vehicles listed with prices
- 4 services section  
- About us section with floating Om animation
- Contact form (Django backend se connected)
- WhatsApp floating button
- Mobile responsive
- Smooth navbar on scroll

---

## Project Structure

```
mahakal_tours/
├── manage.py
├── requirements.txt
├── mahakal_tours/          ← Main project folder
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── home/                   ← App folder
    ├── views.py
    ├── urls.py
    ├── models.py
    └── templates/home/
        └── index.html      ← Main HTML (sab kuch isme hai)
```

---

## Kaise Chalayein (How to Run)

### Step 1: Python aur pip check karein
```bash
python --version   # Python 3.8+ chahiye
```

### Step 2: Dependencies install karein
```bash
pip install -r requirements.txt
```

### Step 3: Database setup
```bash
python manage.py migrate
```

### Step 4: Server chalayein
```bash
python manage.py runserver
```

### Step 5: Browser mein kholein
```
http://127.0.0.1:8000
```

---

## Production Ke Liye (Optional)

### settings.py mein ye changes karein:
```python
DEBUG = False
ALLOWED_HOSTS = ['aapka-domain.com']
SECRET_KEY = 'koi-secret-key-rakhein'
```

### Static files collect karein:
```bash
python manage.py collectstatic
```

---

## Phone Number Change Karna Ho To

`home/views.py` file mein ye line update karein:
```python
'phone': '9109282779',  ← Apna number daalein
```

---

## 🙏 Har Har Mahakal!
=======
# mahakal-tours-django
Travel and tour booking website built using Django.

