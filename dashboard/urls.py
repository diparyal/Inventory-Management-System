from django.urls import path
from .views import home,statusupdate

urlpatterns = [
    path('home/', home, name='home'),
    path('order_request/',statusupdate, name="status_change"),

]
