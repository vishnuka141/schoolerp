from django.urls import path

from . import views
urlpatterns = [
   
    path('all/',views.all_payment,name='all_payment'),
    path('new/',views.add_payment,name='add_payment'),
    path('type/',views.payment_type_create,name='payment_type'),
    path('type/delete/<pk>/',views.payment_type_delete,name='pt_delete')


]