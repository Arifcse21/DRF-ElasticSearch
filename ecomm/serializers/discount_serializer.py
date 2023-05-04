from rest_framework.serializers import ModelSerializer
from ecomm.models import Discount


class DiscountSerializer(ModelSerializer):

    class Meta:
        model = Discount
        fields = [
            "id",
            "name",
            "desc",
            "discount_percent",
            "active"
        ]
