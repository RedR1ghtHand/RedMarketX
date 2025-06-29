from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from item.models import ItemType, Material, Enchantment
from django.shortcuts import get_object_or_404


class OrderMetadataView(APIView):
    def get(self, request):
        item_type_slug = request.query_params.get('item_type')

        if not item_type_slug or item_type_slug.strip() == "":
            return Response(
                {"error": "Query parameter 'item_type' is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        item_type = get_object_or_404(ItemType, slug=item_type_slug)
        materials = Material.objects.filter(applicable_to=item_type).values('id', 'name')
        enchantments = Enchantment.objects.filter(applicable_to=item_type).values('id', 'name', 'max_level')

        return Response({
            "materials": list(materials),
            "enchantments": list(enchantments)
        })
