from django.db import  models


class ProductCategory(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField(max_length=2000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

