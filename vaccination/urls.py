from django.urls import path
from vaccination import views
from django.contrib import admin

urlpatterns = [
    path('',views.home,name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('login/userdashboard/', views.userdashboard_view, name='userdashboard'),
    path('login/admindashboard/', views.admindashboard_view, name='admindashboard'),
    path('registervaccination/', views.registervaccination_view, name='registervaccination'),
    path('apply/', views.apply_view, name='apply'),
    path('login/admin_login/', views.admin_login_view, name='admin_login'),
    path('add_centre/', views.add_centre_view, name='add_centre'),
    path('get_dosage_details/', views.get_dosage_details_view, name='get_dosage_details'),
    path('remove_centre/', views.remove_centre_view, name='remove_centre'),
    path('logout/home/', views.logout_view, name='logout'),
    path('admin/', admin.site.urls),
]