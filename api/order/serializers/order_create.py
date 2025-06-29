from rest_framework import serializers
from order.models import Order, OrderEnchantment
from item.models import Enchantment


class OrderEnchantmentCreateSerializer(serializers.Serializer):
    enchantment_id = serializers.PrimaryKeyRelatedField(queryset=Enchantment.objects.all(), source='enchantment')
    level = serializers.IntegerField(min_value=1)


class OrderCreateSerializer(serializers.ModelSerializer):
    enchantments = OrderEnchantmentCreateSerializer(many=True, required=False)

    class Meta:
        model = Order
        fields = ['item_type', 'material', 'quantity', 'price', 'enchantments']

    def create(self, validated_data):
        enchantments = validated_data.pop('enchantments', [])
        order = Order.objects.create(created_by=self.context['request'].user, **validated_data)

        for ench in enchantments:
            OrderEnchantment.objects.create(order=order, **ench)

        return order
