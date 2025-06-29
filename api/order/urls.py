from django.urls import path
from order.views import OrderCreateView, OrderDetailView, OrderMetadataView


urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('metadata/', OrderMetadataView.as_view(), name='order_metadata'),
    path('<slug:slug>/', OrderDetailView.as_view(), name='order_list_by_type'),
]
