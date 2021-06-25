from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import AdminLoginAPI, reset_page

router = DefaultRouter()
router.register(r'function', FunctionAPI, basename='function'),
router.register(r'skill', SkillAPI, basename='skill'),

urlpatterns = [
    path('login/', AdminLoginAPI.as_view({'post': 'login'})),
    url('', include(router.urls)),
]