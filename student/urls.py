from django.urls import path
from student import views


urlpatterns = [
    path('add/',views.add_student, name='add'),
    path('list/',views.sutdent_list, name='list'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<str:id>/', views.update, name='update'),
    
    
]