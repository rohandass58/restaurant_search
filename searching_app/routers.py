from rest_framework.routers import DefaultRouter

from searching_app.viewsets import (
    RestaurantsViewSet,
)

router = DefaultRouter()

router.register(r"restaurant", RestaurantsViewSet, basename="restaurant")
