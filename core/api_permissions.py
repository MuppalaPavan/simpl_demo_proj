from rest_framework.permissions import BasePermission

from apps.admins_app.models import AdminUser
from apps.candidate.models import Candidate
from .encryption import (jwt_decode_handler, crypto_decode)

# from user_app.models import AppUser


class AppUserAuthentication(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        try:
            user_id = crypto_decode(
                    jwt_decode_handler(
                        request.META['HTTP_AUTHORIZATION']
                    )['ai']
            )
            pwd = crypto_decode(
                    jwt_decode_handler(
                        request.META['HTTP_AUTHORIZATION']
                    )['bi']
            ) if jwt_decode_handler(
                        request.META['HTTP_AUTHORIZATION']
                    )['bi'] != '' else ''
            print(pwd)
            request.user = Candidate.objects.get(id=int(user_id), password=pwd, active=True)
            request.role = 'Candidate'
            return True
        except:
            return False


class AdminAuthentication(BasePermission):
    """
    Allows access only to authenticated admins.
    """

    def has_permission(self, request, view):
        try:
            user_id = crypto_decode(
                    jwt_decode_handler(
                        request.META['HTTP_AUTHORIZATION']
                    )['ai']
            )
            pwd = crypto_decode(
                    jwt_decode_handler(
                        request.META['HTTP_AUTHORIZATION']
                    )['bi']
            ) if jwt_decode_handler(
                        request.META['HTTP_AUTHORIZATION']
                    )['bi'] != '' else ''
            role = jwt_decode_handler(request.META['HTTP_AUTHORIZATION']).get('ci', '')
            request.user = AdminUser.objects.get(id=int(user_id), password=pwd, active=True, published=True,
                                                 roles__contains=[role])
            request.role = role
            return True
        except:
            return False

