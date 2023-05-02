from ecomm.models import Product
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry


@registry.register_document
class ProductDocument(Document):

    category = fields.NestedField(
        properties={
            "id": fields.IntegerField(),
            "title": fields.TextField(),
            "desc": fields.TextField()
        }
    )
    discount = fields.NestedField(
        properties={
            "id": fields.IntegerField(),
            "name": fields.TextField(),
            "desc": fields.TextField(),
            "discount_percent": fields.FloatField(),
            "active": fields.BooleanField()
        }
    )

    class Index:
        name = "products"
        settings = {
            "number_of_shards": 2,
            "number_of_replicas": 1
        }

    class Django:
        model = Product
        fields = [
            "id",
            "title",
            "desc",
            "SKU",
            "stock",
            "price",
            "currency"
        ]

