from django.db import models
from item.models import Enchantment
from .order import Order


class OrderEnchantment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    enchantment = models.ForeignKey(Enchantment, on_delete=models.CASCADE)
    level = models.PositiveIntegerField(default=1)
