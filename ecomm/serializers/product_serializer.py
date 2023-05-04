from ecomm.models import Product
from rest_framework.serializers import ModelSerializer


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "desc",
            "SKU",
            "currency"
        ]
