from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('make_reservation', views.make_reservation, name='make_reservation'),
    path('user-panel', views.userPanel, name='userPanel'),
    path('user-update/<int:id>', views.userUpdate, name='userUpdate'),
    path('editbooking/<int:id>', views.editbooking, name='editbooking'),
    path('mybookings', views.mybookings, name='mybookings'),
]
