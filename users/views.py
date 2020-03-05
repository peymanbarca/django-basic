from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from users.models import UserCo


def findOneUserIdByLogin(login):
    queryset = UserCo.objects.filter(username=login)
    return queryset.values_list('id', flat=True)[0]


def findRoleByUserId(userId):
    queryset = UserCo.objects.filter(id=userId)
    print(queryset,'***')
    return queryset.values_list('role',flat=True).values_list('role_name',flat=True)