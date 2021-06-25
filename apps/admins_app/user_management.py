from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from apps.admins_app.models import AdminUser, Skill, Function

from honeybee_project.settings import FrontEndUrl, FED_BD_URL, FED_ADMIN_URL, FED_RECRUITER_URL

def get_fed_url(roles):
    if 'bd' in roles:
        return FED_BD_URL
    elif 'admin' in roles:
        return FED_ADMIN_URL
    elif 'recruiter' in roles:
        return FED_RECRUITER_URL
    else:
        return FrontEndUrl