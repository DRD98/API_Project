from django.urls import re_path
from mainApp import views

urlpatterns = [
    re_path(r'^first-app/get', views.get_car, name = 'get'),
    re_path(r'^first-app/get/?', views.get_car, name = 'gettwo'),
    re_path(r'^first-app/post/', views.post_car, name = 'post'),
    re_path(r'^first-app/post-raw/', views.post_car_raw, name = 'postraw'),
    re_path(r'^first-app/post-form/', views.post_car_form, name = 'postform'),
    re_path(r'^first-app/del/', views.del_car, name = 'del'),
    re_path(r'^first-app/put/', views.put_car, name = 'put'),
    re_path(r'^first-app/patch/', views.patch_car, name = 'patch')
]