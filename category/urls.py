from django.urls import path
from .views import AddCategory
urlpatterns = [
    path('addcategory/',AddCategory,name='addcategory')
]