from django.urls import include, path
from rest_framework import routers
from .api import PageViewSets

router = routers.DefaultRouter()
router.register(r'pages', PageViewSets, basename='page')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]