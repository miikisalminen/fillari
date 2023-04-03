from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from fillari import views

router = routers.DefaultRouter()
router.register(r'stations', views.StationView, 'station')

urlpatterns = [
    path('admin/', admin.site.urls),
     path("", views.front, name="front"),
    path('api/', include(router.urls)),
]