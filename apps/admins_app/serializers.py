from django.contrib import admin
from django.db import models
from rest_framework.serializers import ModelSerializer
from .models import AdminUser, Function, Skill

class AdminLoginSerializer(ModelSerializer):
    admin_role = models.CharField(default='super_admin')

    class Meta:
        model = AdminUser
        fields = ('email', 'password', 'admin_role')


class AdminUserDetailSerializer(ModelSerializer):

    class Meta:
        model = AdminUser
        exclude = ('active', 'created', 'modified', 'password')


class ChangePasswordSerializer(ModelSerializer):
    old_password = models.CharField(required=True)
    new_password = models.CharField(required=True)

    class Meta:
        model = AdminUser
        fields = ('old_password', 'new_password',)



class FunctionSerializer(ModelSerializer):
    name = models.CharField(source='tag_name')

    class Meta:
        model = Function
        fields = ('id', 'name')


class SkillSerializer(ModelSerializer):
    name = models.CharField(source='tag_name')

    class Meta:
        model = Skill
        fields = ('id', 'name', 'function')


class SkillListingSerializer(ModelSerializer):
    name = models.CharField(source='tag_name')
    function = models.CharField(source='function.tag_name')

    class Meta:
        model = Skill
        fields = ('id', 'name', 'function')


class AdminProfileUpdateSerializer(ModelSerializer):

    class Meta:
        model = AdminUser
        fields = ('profile_pic', 'description', 'phone', 'first_name', 'last_name', 'country_code',)

class AdminSerializer(ModelSerializer):
    
    class Meta:
        model = AdminUser
        fields = ('id', 'email', 'first_name', 'last_name', 'phone', 'level', 'skills', 'roles', 'published',
                  'functions', 'country_code', 'active_projects')
        read_only_fields = ('id',)

