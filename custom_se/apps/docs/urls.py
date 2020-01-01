from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.docs_view, name='docs_view')
]