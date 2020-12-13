from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

app_name='src'

urlpatterns = [
    path('',views.home),

    path('signup/',views.signup_view,name="signup"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
   
    url(r'^custform/', views.custform, name="custform"),
    url(r'^custforminsert/', views.custforminsert, name="custforminsert"),
    url(r'^custformupdate(?P<foo>[0-9]+)/', views.custformupdate, name="custformupdate"),
    url(r'^custformview(?P<foo>[0-9]+)/', views.custformview, name="custformview"),
    url(r'^custformdelete(?P<foo>[0-9]+)/', views.custformdelete, name="custformdelete"),
    url(r'^custtable/', views.custtable, name='custtable'),

    url(r'^medform/', views.medform, name="medform"),
    url(r'^medforminsert/', views.medforminsert, name="medforminsert"),
    url(r'^medformupdate(?P<foo>[0-9]+)/', views.medformupdate, name="medformupdate"),
    url(r'^medformview(?P<foo>[0-9]+)/', views.medformview, name="medformview"),
    url(r'^medformdelete(?P<foo>[0-9]+)/', views.medformdelete, name="medformdelete"),
    url(r'^medtable/', views.medtable, name='medtable'),

    
]
