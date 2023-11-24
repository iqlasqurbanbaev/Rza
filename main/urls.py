from django.urls import path
from . import views
app_name = 'main'


urlpatterns = [
    path('menu/category/<str:slug>', views.menu, name='category'),
    path('main/', views.mainpage, name='main'),
    path('login/', views.user_login, name='login'),
    path('register/', views.registration, name='register'),
    path('menu/', views.menu, name='menu'),
    path('', views.homepage, name='home'),

    path('product_list/', views.admin_product_list, name='product_list'),
    path('product_add/', views.product_add, name='product_add'),
    path('update_product/<str:product_id>/', views.update_product, name='update_product'),

]

