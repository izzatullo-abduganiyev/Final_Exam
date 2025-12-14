from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Food, Order, OrderItem


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['food', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'items']

    def create(self, validated_data):
        items = validated_data.pop('items')
        order = Order.objects.create(user=self.context['request'].user)

        for item in items:
            OrderItem.objects.create(
                order=order,
                food=item['food'],
                quantity=item['quantity'],
                price=item['food'].price
            )

        return order
