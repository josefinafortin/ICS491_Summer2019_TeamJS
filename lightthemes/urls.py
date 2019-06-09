from django.urls import path, re_path
from . import views

app_name = 'lightthemes'

urlpatterns = [
    path('', views.lighttheme_list, name="lighthome"),
    path('firetheme', views.fire_theme, name="firetheme" ),
    path('raintheme', views.rain_theme, name="raintheme"),
    path('suntheme', views.sun_theme, name="suntheme"),
    path('on', views.light_on, name="on"),
    path('off', views.light_off, name="off"),
]
