# 🍽 Food Order API

Ovqat buyurtma qilish tizimi uchun yaratilgan backend REST API.  
Loyiha **Django Rest Framework**, **JWT authentication**, **Swagger dokumentatsiya**,  
**Linux server**, **Gunicorn + Nginx**, **SSL sertifikat** bilan deploy qilingan.

---

## 🌍 Live URLs

- 🔗 **API Base URL:**  
  https://foodordergo.space/api/

- 📘 **Swagger API Docs:**  
  https://foodordergo.space/api/docs/

---

## 🔐 Authentication

- **Register:** `POST /api/auth/register/`
- **Login:** `POST /api/auth/login/`
- JWT orqali himoyalangan endpointlar mavjud

---

## 🍔 Foods

- `GET /api/foods/` — barcha ovqatlar (pagination + filter)
- `POST /api/foods/add/` — ovqat qo‘shish (admin)

---

## 📦 Orders

- `POST /api/orders/create/` — buyurtma yaratish
- `GET /api/orders/history/` — buyurtmalar tarixi

---

## 🛠 Technologies

- Python 3.10
- Django 4.2
- Django Rest Framework
- SimpleJWT
- drf-spectacular (Swagger)
- Gunicorn
- Nginx
- Let’s Encrypt SSL
- Linux (Ubuntu)

---

## 🚀 Deployment

Loyiha real serverga deploy qilingan:
- Gunicorn + systemd
- Nginx reverse proxy
- HTTPS (SSL) yoqilgan
- Domen ulangan

---
