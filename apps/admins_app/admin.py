from django.contrib import admin

from . models import AdminUser, Function, Skill

admin.site.register(AdminUser)
admin.site.register(Function)
admin.site.register(Skill)

