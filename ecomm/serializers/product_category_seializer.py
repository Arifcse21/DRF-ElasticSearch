from rest_framework.serializers import ModelSerializer
from ecomm.models import ProductCategory


class ProductCategorySerializer(ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = [
            "id",
            "title",
            "desc"
        ]
