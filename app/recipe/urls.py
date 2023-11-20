"""
URL mapping for the recipe app.
"""
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
# router create new endpoint api/recipes and it assings
# all of the different endpoint from recipe viewset to this endpoint.
# Recipe viewset it goint to have auto generated URLs depending on
# the functionalitiy that is enabled on the view set.
# Thanls to Model ViewSet it is going to support all methods for
# create, read, update and delete i.e HTTP get, post, put, patch, delete
router.register('recipes', views.RecipeViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
