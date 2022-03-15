"""vue_todo URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

from todo_app.views import TaskViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'todo_app', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
