from django.urls import path
from .views import SignUpView,home

urlpatterns = [
    # path('',ProductView.as_view(),name='view_product'),
    path('', SignUpView, name='signup'),
    path('home/', home, name='home'),
]
