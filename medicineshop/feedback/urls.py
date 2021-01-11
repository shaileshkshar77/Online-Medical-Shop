from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

app_name='feedback'

urlpatterns = [

    path('',views.ck,name="feedbacks"),
    path('gvfdk/',views.gvfdk,name="feedbacks"),
    
]
