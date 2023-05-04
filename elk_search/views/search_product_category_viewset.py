from .paginated_elasticsearch_viewset import PaginatedElasticSearchViewSet
from ecomm.serializers import ProductCategorySerializer
from ecomm.documents import ProductCategoryDocument
from elasticsearch_dsl import Q


class SearchProductCategoryViewSet(PaginatedElasticSearchViewSet):

    serializer_class = ProductCategorySerializer
    document_class = ProductCategoryDocument

    def get_q_expression(self, query):
        return Q(
            'multi_match',
            query=query,
            fields=[
                'title',
            ],
            fuzziness='auto'
        )
