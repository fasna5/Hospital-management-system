from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index,name ='home'),
    path('about/',views.about,name ='about'),
    path('bookings/',views.bookings,name='bookings'),
    path('doctors/',views.doctors,name='doctors'),
    path('contact/', views.contact,name='contact'),
    path('departments/',views.departments,name='departments'),

]