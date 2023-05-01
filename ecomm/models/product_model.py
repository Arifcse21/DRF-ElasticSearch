from django.db import models
from ecomm.utils import SkuGeneratorUtil
from .product_category_model import ProductCategory
from .discount_model import Discount


def maintain_serial():
    last_entry = Product.objects.all().order_by('id').last()
    if last_entry:
        return last_entry.id + 1
    return last_entry


class Product(models.Model):

    id = models.AutoField(unique=True, primary_key=True, default=maintain_serial, editable=False)
    title = models.CharField(max_length=255, null=True, blank=True)
    desc = models.TextField(max_length=2000, null=True, blank=True)
    SKU = models.CharField(max_length=8, default=SkuGeneratorUtil.generate_sku, null=True, blank=True, editable=False)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, blank=True)
    stock = models.PositiveIntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    currency = models.CharField(max_length=3, null=True, blank=True)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

