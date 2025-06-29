from rest_framework import serializers
from order.models import Order, OrderEnchantment
from item.models import Enchantment


class EnchantmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enchantment
        fields = ['id', 'name']


class OrderEnchantmentSerializer(serializers.ModelSerializer):
    enchantment = EnchantmentSerializer()

    class Meta:
        model = OrderEnchantment
        fields = ['enchantment', 'level']


class OrderListSerializer(serializers.ModelSerializer):
    enchantments = OrderEnchantmentSerializer(many=True, source='orderenchantment_set')
    material = serializers.StringRelatedField()
    item_type = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField(source='created_by.mc_username')

    class Meta:
        model = Order
        fields = ['id', 'item_type', 'material', 'quantity', 'price', 'created_at', 'enchantments', 'created_by']
