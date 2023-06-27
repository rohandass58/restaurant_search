from rest_framework import mixins, viewsets
from rest_framework.response import Response
from searching_app.serializers import RestaurantsSerializer
from searching_app.models import Restaurants
from django.db.models import CharField
from django.db.models.functions import Cast

class RestaurantsViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer

    def list(self, request):
        search_query = request.query_params.get('search_query', None)

        queryset = self.get_queryset()

        if search_query:

            queryset = Restaurants.objects.annotate(
                items_text=Cast('items', output_field=CharField())
            ).filter(items_text__contains=search_query)
        

        serializer = RestaurantsSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)