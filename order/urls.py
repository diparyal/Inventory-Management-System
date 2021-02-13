from django.urls import path
from .views import OrderView,AllOrder,AddOrder

urlpatterns = [
    path('',OrderView.as_view(),name='view_order'),
    path('display/',AllOrder,name='all_order'),
    path('add_order/',AddOrder,name='add_order'),
]
