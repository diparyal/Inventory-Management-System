from django.urls import path
from .views import SignUpView,UserView,UserList,StaffApproved,StaffList

urlpatterns = [
    # path('',ProductView.as_view(),name='view_product'),
    path('', SignUpView, name='signup'),
    path('users/',UserView.as_view(),name='view_user'),
    # path('all_users/',UserList.as_view(),name='all_users'),
    path('all_users/',UserList,name='all_users'),
    path('staff_list/',StaffList, name="staff_list"),
    path('staff_request/<str:pk>/',StaffApproved, name="staff_request"),


]
