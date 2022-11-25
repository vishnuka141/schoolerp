
from django.urls import path

from main import views
urlpatterns = [
   
    path('login/',views.signin,name='signin'),
    path('logout/',views.signout,name='signout'),
    path('academic/year/create/',views.academic_year_create,name='academic_year'),
    path('academic/year/delete/<pk>/',views.acdemic_delete,name='academic_delete')
]