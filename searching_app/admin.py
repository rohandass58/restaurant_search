from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Restaurants


class RestaurantsResource(resources.ModelResource):
    class Meta:
        model = Restaurants


@admin.register(Restaurants)
class RestaurantAdmin(ImportExportModelAdmin):
    resource_classes = (RestaurantsResource,)

    search_fields = [
        "id",
        "name",
        "location",
        "items"
    ]

    list_display = [
        "id",
        "name",
        "location",
        "items"
    ]

    
    class Meta:
        verbose_name = "Restauant"
        verbose_name_plural = "Restaurants"
