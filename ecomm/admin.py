from django.contrib import admin
from ecomm.models import (
    User,
    Product,
    ProductCategory,
    Cart,
    Discount
)
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "uuid",
        "username",
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_superuser",
        "is_active",
        "last_login"
    ]
    list_display_links = ["id", "username"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "SKU",
        "category",
        "stock",
        "price",
        "currency",
        "discount",
        "created_at",
        "modified_at"
    ]
    list_display_links = ['title']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "product",
        "quantity",
        "created_at",
        "modified_at"
    ]


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "desc",
        "discount_percent",
        "active",
        "created_at",
        "modified_at"
    ]


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "desc",
        "created_at",
        "modified_at"
    ]
