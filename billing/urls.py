from django.urls import path
from .views import bill


urlpatterns = [
    # path('',OrderView.as_view(),name='view_order'),
    path('',bill,name='user_bill'),
    # path('add_order/',AddOrder,name='add_order'),
]