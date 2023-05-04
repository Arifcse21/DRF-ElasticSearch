from .paginated_elasticsearch_viewset import PaginatedElasticSearchViewSet
from ecomm.serializers import UserSerializer
from ecomm.documents import UserDocument
from elasticsearch_dsl import Q


class SearchUserViewSet(PaginatedElasticSearchViewSet):
    serializer_class = UserSerializer
    document_class = UserDocument

    def get_q_expression(self, query):          # implementing the abstractmethod of parent class
        return Q(
            'bool',
            should=[            # contain the query either in the 'username' or 'first_name' or 'last_name;
                Q('match', username=query),
                Q('match', first_name=query),
                Q('match', last_name=query)
            ],
            minimum_should_match=1
        )
