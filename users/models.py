from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models

# Create your models here.

class Roles(models.Model):
    id = models.IntegerField(primary_key=True)
    role_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"schm2"."roles"'

class UserCo(AbstractBaseUser):

    REQUIRED_FIELDS = ('password',)
    USERNAME_FIELD = ('username')

    id = models.IntegerField(primary_key=True,unique=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=150,unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    role = models.ManyToManyField(Roles, through='UserRoles')

    objects = UserManager()
    class Meta:
        managed = False
        db_table = '"schm2"."user_co"'



class UserRoles(models.Model):
    user = models.ForeignKey(UserCo,on_delete=models.CASCADE,db_column='user_co_id')
    role = models.ForeignKey(Roles,on_delete=models.CASCADE,db_column='role_id')

    class Meta:
        managed = False
        db_table = '"schm2"."user_roles"'



