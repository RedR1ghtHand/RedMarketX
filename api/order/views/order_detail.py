from rest_framework import generics, permissions, filters
from rest_framework.renderers import JSONRenderer
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from order.models import Order
from item.models import ItemType
from order.serializers import OrderListSerializer


class OrderDetailView(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = OrderListSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['material']
    ordering_fields = ['price', 'quantity']
    ordering = ['-created_at']

    def get_queryset(self):
        item_type = get_object_or_404(ItemType, slug=self.kwargs['slug'])
        return (
            Order.objects
            .filter(item_type=item_type, deleted_at__isnull=True)
            .select_related('material', 'item_type', 'created_by')
            .prefetch_related('orderenchantment_set__enchantment')
        )