from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('', views.homepage),
    re_path(r'^accounts/', include('accounts.urls')),
    re_path(r'^timer/', include('timer.urls')),
    re_path(r'^lightthemes/', include('lightthemes.urls')),
    re_path(r'^adddevice/', include('adddevice.urls')),
]

urlpatterns += staticfiles_urlpatterns()
