from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('',views.hello_world, name='shop'),
    path('about/',views.about,name='about'),
    path('logout/',views.logout_user,name='logout'),
    path('login/',views.login_user,name='login'),
]
