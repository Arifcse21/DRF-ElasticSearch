from .paginated_elasticsearch_viewset import PaginatedElasticSearchViewSet
from ecomm.serializers import DiscountSerializer
from ecomm.documents import DiscountDocument
from elasticsearch_dsl import Q


class SearchDiscountViewSet(PaginatedElasticSearchViewSet):

    serializer_class = DiscountSerializer
    document_class = DiscountDocument

    def get_q_expression(self, query):
        return Q(
            'multi_match',
            query=query,
            fields=[
                "name",
                "desc",
            ],
            fuzziness='auto'
        )
