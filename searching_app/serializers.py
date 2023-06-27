
from rest_framework import serializers
from searching_app.models import Restaurants
from rest_framework import serializers
class RestaurantsSerializer(serializers.ModelSerializer):


    class Meta:
        model = Restaurants
        fields = ["id",
                  "name",
                  "location",
                  "items",]

