from django.urls import path
from .views import ProductView,ProductAdd

urlpatterns = [
    path('',ProductView.as_view(),name='view_product'),
    path('add_product/',ProductAdd,name='add_product'),
]
