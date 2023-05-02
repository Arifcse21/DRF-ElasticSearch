from ecomm.models import Discount
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry


@registry.register_document
class DiscountDocument(Document):

    class Index:
        name = "discounts"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }

    class Django:
        model = Discount
        fields = [
            "id",
            "name",
            "desc",
            "discount_percent",
            "active"
        ]
