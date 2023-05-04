from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from abc import abstractmethod
from rest_framework.response import Response


class PaginatedElasticSearchViewSet(APIView, LimitOffsetPagination):

    serializer_class = None
    document_class = None

    @abstractmethod
    def get_q_expression(self, query):
        """This method must be overridden and return a q expression"""

    def get(self, request, query):
        try:

            q = self.get_q_expression(query)
            search = self.document_class.search().query(q)
            response = search.execute()

            print(f"found {response.hits.total.value} hit(s) for query: {query}")

            results = self.paginate_queryset(response, request, view=self)
            print(f"results: {response}")
            serializer = self.serializer_class(response, many=True)

            print(f"serializer data = {serializer}")
            return self.get_paginated_response(serializer.data)

        except Exception as e:
            return Response(str(e), status=500)

