# 🍽 Food Order API

Ovqat buyurtma qilish tizimi uchun yaratilgan backend REST API.
Loyiha Django Rest Framework, JWT authentication, Swagger dokumentatsiya,
Linux server, Gunicorn + Nginx, SSL sertifikat bilan deploy qilingan.

🌍 Live URLs
API Base URL:
https://foodordergo.space/

Swagger API Docs:
https://foodordergo.space/api/docs/

🔐 Authentication (JWT)
POST /api/auth/register/  — Foydalanuvchi ro‘yxatdan o‘tish
POST /api/auth/login/     — Login va JWT token olish

Himoyalangan endpointlar uchun:
Authorization: Bearer <ACCESS_TOKEN>

🍔 Foods (Ovqatlar)
GET  /api/foods/                      — Barcha ovqatlar (pagination + filter)
GET  /api/foods/?category=fast_food   — Category bo‘yicha filter

🔐 Admin-only Foods
POST   /api/foods/add/                — Ovqat qo‘shish
PATCH  /api/foods/<id>/update/        — Ovqatni tahrirlash (price, status)
DELETE /api/foods/<id>/delete/        — Ovqatni o‘chirish

Update misoli:
{
  "price": 30000,
  "is_available": false
}

📦 Orders (Buyurtmalar)
POST /api/orders/create/   — Buyurtma yaratish
GET  /api/orders/history/  — Foydalanuvchi buyurtmalari

Buyurtma yaratish misoli:
{
  "items": [
    { "food": 1, "quantity": 2 },
    { "food": 3, "quantity": 1 }
  ]
}

🔐 Admin Permissions
Adminlik Django User modeli orqali belgilanadi:
user.is_staff = True

Admin-only endpointlar custom IsAdmin permission orqali himoyalangan.

🛠 Technologies
Python 3.10
Django 4.2
Django Rest Framework
SimpleJWT
drf-spectacular (Swagger)
Gunicorn
Nginx
Let’s Encrypt SSL
Linux (Ubuntu)

🚀 Deployment
Loyiha production holatda deploy qilingan:
Gunicorn + systemd
Nginx reverse proxy
HTTPS (SSL)
Domen ulangan

✅ Project Status
JWT authentication
Admin permissions
CRUD foods (Create, Update, Delete)
Orders system
Swagger documentation
Production deployment
