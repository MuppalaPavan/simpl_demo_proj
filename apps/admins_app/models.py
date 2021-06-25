from django.contrib.auth.hashers import make_password, check_password
from django.contrib.postgres.fields import ArrayField
from django.db import models

class Function(models.Model):
    tag_name = models.CharField(max_length=50, unique=True)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tag_name


class Skill(models.Model):
    function = models.ForeignKey(Function, on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=50, unique=True)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tag_name

class AdminUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.TextField()
    country_code = models.CharField(max_length=5, default='91')
    profile_pic = models.URLField(null=True)
    description = models.TextField(blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    functions = models.ManyToManyField(Function, blank=True)
    roles = ArrayField(models.CharField(max_length=11))
    last_login = models.DateTimeField(null=True, blank=True)
    published = models.BooleanField(default=True)
    read_notifications = ArrayField(models.PositiveIntegerField(blank=True), blank=True, default=list)
    active_projects = models.PositiveIntegerField(default=0)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        def setter(raw_password):
            self.set_password(raw_password)
            self._password = None
            self.save(update_fields=["password"])

        return check_password(raw_password, self.password, setter)

    def save(self, *args, **kwargs):
        make_title = (self, ['first_name', 'last_name'])
        make_lower = (self, ['email'])
        super(AdminUser, self).save(*args, **kwargs)

