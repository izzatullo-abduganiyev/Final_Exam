from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import *

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),

    path('foods/', FoodListView.as_view()),
    path('foods/add/', FoodCreateView.as_view()),

    path('orders/create/', OrderCreateView.as_view()),
    path('orders/history/', OrderHistoryView.as_view()),
]
