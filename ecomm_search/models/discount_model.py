from django.db import models


class Discount(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    desc = models.TextField(max_length=2000, null=True, blank=True)
    discount_percent = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

