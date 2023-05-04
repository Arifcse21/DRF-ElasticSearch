from ecomm.models import ProductCategory
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry


@registry.register_document
class ProductCategoryDocument(Document):

    class Index:
        name = 'product_categories'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = ProductCategory
        fields = [
            'id',
            'title',
            'desc'
        ]

