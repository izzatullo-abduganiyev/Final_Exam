from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Food, Order
from .serializers import (
    RegisterSerializer,
    FoodSerializer,
    OrderSerializer
)
from .permissions import IsAdmin


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class FoodListView(generics.ListAPIView):
    queryset = Food.objects.filter(is_available=True)
    serializer_class = FoodSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


class FoodCreateView(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAdmin]


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderHistoryView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
