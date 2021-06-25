import os
import re
import shutil
import tempfile
import uuid

from django.contrib.sites.shortcuts import get_current_site
from . models import AdminUser, Function, Skill
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.utils.encoding import force_bytes, force_text
from PIL import Image
from rest_framework.parsers import FormParser, MultiPartParser
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.exceptions import ObjectDoesNotExist
from . serializers import AdminLoginSerializer, AdminUserDetailSerializer, ChangePasswordSerializer, FunctionSerializer, \
    SkillSerializer, SkillListingSerializer, AdminProfileUpdateSerializer, AdminSerializer

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from apps.admins_app.user_management import get_fed_url
from apps.admins_app.models import AdminUser
from apps.admins_app.serializers import AdminLoginSerializer, AdminUserDetailSerializer


def reset_page(request, role='super_admin', uid=None, token=None):
    fed_url = get_fed_url([role])
    message = []
    if request.method == 'GET':
        validlink = False
        if uid and token:
            try:
                token_obj = Token.objects.get(uid=uid, token=token)
                if token_obj.status is not True:
                    validlink = True
            except:
                pass
    else:
        password1 = request.POST.get('new_password1')
        password2 = request.POST.get('new_password2')
        if re.match(password_regex, password1) is None:
            validlink = True
            message.append('Your password must contain at least 6 and maximum 15 characters')

        else:
            message.append('Your password must contain at least one lowercase letter, one uppercase letter, one numeric\
             digit, and one special character')
            if password1 == password2:
                user_id = force_text(urlsafe_base64_decode(uid))
                try:
                    token_obj = Token.objects.get(uid=uid, token=token)
                    if token_obj.status is True:
                        validlink = False
                    else:
                        user = AdminUser.objects.get(id=user_id)
                        user.set_password(password1)
                        user.save()
                        token_obj.status = True
                        token_obj.save()
                        subject = 'Honeybees password reset request done'
                        template = 'reset_password.html'
                        recipients = [user.email]
                        context = {
                            'username': user.first_name,
                            'frontend_url': fed_url
                        }
                        email_send(subject, template, recipients, context)
                        return render(request, 'password_reset_complete.html', {'frontend_url': fed_url})
                except:
                    validlink = False
            else:
                validlink = True
                message.append('Passwords did not match')
    return render(request, 'password_reset_confirm.html', {'validlink': validlink, 'message': message})


class AdminLoginAPI(ModelViewSet):
    serializer_class = AdminLoginSerializer

    @staticmethod
    def login(request):
        email = request.data.get('email')
        password = request.data.get('password')
        role = request.data.get('admin_role')
        check_invalid([email, password, role])
        user = admin_authenticate(email, password, role)
        if user:
            payload = jwt_payload_handler(user, role)
            user.last_login = timezone.now()
            user.active = True
            user.save()
            context = {
                'token': jwt_encode_handler(payload),
                'user': AdminUserDetailSerializer(user).data
            }
            return Response(context)
        return Response(message_response(login_failed), status=400)

