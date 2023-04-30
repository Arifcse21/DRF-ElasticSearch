from django.db import models
from ecomm.utils.SkuGeneratorUtil import generate_sku
from .product_category_model import ProductCategory
from .product_inventory_model import ProductInventory
from .discount_model import Discount


class Product(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    desc = models.TextField(max_length=2000, null=True, blank=True)
    SKU = models.CharField(max_length=8, default=generate_sku, null=True, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, blank=True)
    inventory = models.ForeignKey(ProductInventory, on_delete=models.CASCADE, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    currency = models.CharField(max_length=3, null=True, blank=True)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_at = models.DateTimeField(auto_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

