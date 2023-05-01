from django.db import models


def maintain_serial():
    last_entry = Discount.objects.all().order_by('id').last()
    if last_entry:
        return last_entry.id + 1
    return last_entry


class Discount(models.Model):

    id = models.AutoField(unique=True, primary_key=True, default=maintain_serial, editable=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    desc = models.TextField(max_length=2000, null=True, blank=True)
    discount_percent = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

