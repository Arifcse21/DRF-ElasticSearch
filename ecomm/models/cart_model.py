from django.db import models
from .product_inventory_model import ProductInventory


class Cart(models.Model):
    product = models.ForeignKey(ProductInventory, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.id}"
    
