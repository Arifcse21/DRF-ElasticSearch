from .paginated_elasticsearch_viewset import PaginatedElasticSearchViewSet
from ecomm.serializers import CartSerializer
from ecomm.documents import CartDocument
from elasticsearch_dsl import Q


class SearchCartViewSet(PaginatedElasticSearchViewSet):

    serializer_class = CartSerializer
    document_class = CartDocument

    def get_q_expression(self, query):
        return Q(
            'multi_match',
            query=query,
            fields=[
                "user",
            ],
            fuzziness='auto'
        )
