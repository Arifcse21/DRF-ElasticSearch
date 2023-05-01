from django.db import models
from django.contrib.auth import get_user_model
from .product_model import Product


def maintain_serial():
    last_entry = Cart.objects.all().order_by('id').last()
    if last_entry:
        return last_entry.id + 1
    return last_entry


class Cart(models.Model):

    id = models.AutoField(unique=True, primary_key=True, default=maintain_serial, editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.id}"
    
