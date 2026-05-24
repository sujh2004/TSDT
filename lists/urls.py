
from django.urls import path,re_path
from lists import views

urlpatterns = [
    path('new',views.new_list,name='new_list'),
    re_path(r'^lists/(\d+)/$',views.view_list, name= 'view_list'),
    re_path(r'^lists/(\d+)/add_item$',views.add_item, name= 'add_item'),
]