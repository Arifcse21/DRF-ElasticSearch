from ecomm.models import Cart
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry


@registry.register_document
class CartDocument(Document):

    user = fields.NestedField(
        properties={
            "id": fields.IntegerField(),
            "first_name": fields.TextField(),
            "last_name": fields.TextField(),
            "username": fields.TextField()
        }
    )

    product = fields.NestedField(
        properties={
            "id": fields.IntegerField(),
            "title": fields.TextField(),
            "desc": fields.TextField(),
            "SKU": fields.TextField(),
            "stock": fields.TextField(),
            "price": fields.FloatField(),
            "currency": fields.TextField()
        }
    )

    class Index:
        name = "cart"
        settings = {
            "number_of_shards": 2,
            "number_of_replicas": 1
        }

    class Django:
        model = Cart
        fields = [
            "id",
            "quantity",
        ]
