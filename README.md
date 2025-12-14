# 🍽 Food Order API

Ovqat buyurtma qilish tizimi uchun yaratilgan **backend REST API**.  
Loyiha **Django Rest Framework**, **JWT authentication**, **Swagger dokumentatsiya**,  
**Gunicorn + Nginx**, **SSL sertifikat** bilan **production** muhitda deploy qilingan.

---

## 🌍 Live URLs

🔗 **API Base URL**  
https://foodordergo.space/

📘 **Swagger API Docs**  
https://foodordergo.space/api/docs/

---

## 🔐 Authentication (JWT)

POST /api/auth/register/ — Foydalanuvchi ro‘yxatdan o‘tish  
POST /api/auth/login/ — Login va JWT token olish  

Himoyalangan endpointlar uchun header:  
Authorization: Bearer <ACCESS_TOKEN>

---

## 🍔 Foods

### 🔓 Public Endpoints

GET /api/foods/ — Barcha ovqatlar (pagination + filter)  
GET /api/foods/?category=fast_food — Category bo‘yicha filter  

---

### 🔐 Admin-only Endpoints

⚠️ Quyidagi endpointlar **faqat admin (is_staff=True)** uchun.

POST /api/foods/add/ — Ovqat qo‘shish  
PATCH /api/foods/<id>/update/ — Ovqatni tahrirlash (price, status)  
DELETE /api/foods/<id>/delete/ — Ovqatni o‘chirish  

Update request misoli:  
price: 30000  
is_available: false  

---

## 📦 Orders

POST /api/orders/create/ — Buyurtma yaratish  
GET /api/orders/history/ — Foydalanuvchi buyurtmalari  

Buyurtma yaratish misoli:  
items:  
- food: 1, quantity: 2  
- food: 3, quantity: 1  

---

## 🔐 Admin Permissions

Adminlik Django User modeli orqali belgilanadi:  
user.is_staff = True  

Admin endpointlar **custom IsAdmin permission** bilan himoyalangan.

---

## 🛠 Technologies

Python 3.10  
Django 4.2  
Django Rest Framework  
SimpleJWT  
drf-spectacular (Swagger)  
Gunicorn  
Nginx  
Let’s Encrypt SSL  
Linux (Ubuntu)

---

## 🚀 Deployment

Loyiha **production** muhitda deploy qilingan:  
Gunicorn + systemd  
Nginx reverse proxy  
HTTPS (SSL)  
Domen ulangan  

---

## ✅ Project Status

✔ JWT Authentication  
✔ Admin Permissions  
✔ CRUD Foods (Create / Update / Delete)  
✔ Orders System  
✔ Swagger Documentation  
✔ Production Deployment  
