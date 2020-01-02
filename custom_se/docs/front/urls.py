from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.QueryPageView.as_view(), name='docs_view')
]
