from django.urls import path
from . import views

app_name = 'adddevice'

urlpatterns = [
    path('', views.adddevice_view, name="adddevicehome"),
    path('', views.devices_view, name="deviceslist"),
]
