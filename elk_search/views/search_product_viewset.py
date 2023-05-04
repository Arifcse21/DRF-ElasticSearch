from .paginated_elasticsearch_viewset import PaginatedElasticSearchViewSet
from ecomm.serializers import ProductSerializer
from ecomm.documents import ProductDocument
from elasticsearch_dsl import Q


class SearchProductViewSet(PaginatedElasticSearchViewSet):

    serializer_class = ProductSerializer
    document_class = ProductDocument

    def get_q_expression(self, query):
        return Q(
            'multi_match',
            query=query,
            fields=[
                "title",
                "SKU",
                "currency"
            ]
        )
