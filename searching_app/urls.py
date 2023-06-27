from django.urls import include, path

from searching_app.routers import router

urlpatterns = [
    path("", include(router.urls)),
]
