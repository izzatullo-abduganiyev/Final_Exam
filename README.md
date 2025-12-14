# 🍽 Food Order Backend

Ovqat buyurtma qilish tizimi uchun yozilgan **Django REST API** backend loyiha.

---

## 🚀 Texnologiyalar
- Python
- Django
- Django REST Framework
- JWT Authentication
- drf-spectacular (Swagger)
- SQLite (development)

---

## 🔐 Auth
- Register
- Login
- JWT (access & refresh token)

---

## 📦 Funksiyalar
- Foydalanuvchi ro‘yxatdan o‘tadi va login qiladi
- Taomlar ro‘yxatini ko‘radi
- Kategoriya bo‘yicha filter
- Pagination (10 tadan)
- Buyurtma beradi
- Buyurtmalar tarixini ko‘radi
- Admin taom qo‘shadi / o‘chiradi

---

## 📡 API Endpoints

### 🔐 Authentication
POST /api/auth/register/  
POST /api/auth/login/

---

### 🍔 Foods
GET /api/foods/  
GET /api/foods/?category=fast_food  
GET /api/foods/?page=1  

POST /api/foods/add/ (admin)

---

### 🛒 Orders
POST /api/orders/create/  
GET  /api/orders/history/
