from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import index,map_view,ResourceViewSet, EventViewSet

router = DefaultRouter()
router.register(r"resources", ResourceViewSet)
router.register(r"events", EventViewSet)
urlpatterns = [
    path("",index,name="index"),
    path("map/",map_view,name="map"),
    path("api", include(router.urls)),
]