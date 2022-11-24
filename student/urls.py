from django.urls import path
from student import views


urlpatterns = [
    path('add/',views.add_student, name='add'),
    path('list/',views.sutdent_list, name='list'),
    path('detail/',views.detail,name='detail')
    
    
]