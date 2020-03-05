import psycopg2
from django.conf import settings
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework import viewsets
from django.core import serializers
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer

from Utils.NativeQueryUtil import NativeQueryUtil
from Utils.AuthenticationUtils import AuthenticationUtils
from .serializers import *
from .models import Hero
from django.http import JsonResponse
import json
from users import views as uv


conn_dict = settings.DB_CREDENTIALS
conn1 = psycopg2.connect(dbname=conn_dict['NAME'] , user=conn_dict['USER'],
                  password=conn_dict['PASSWORD'] , host=conn_dict['HOST'])
cursor=conn1.cursor()


class HeroViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


class getAllHerosV1_0(generics.ListCreateAPIView):
    permission_classes = ()
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer




@api_view()
def getAllHerosV1_1(request):
    query = 'select id,name,age from heros order by id desc'
    nqu = NativeQueryUtil(cursor)
    data = nqu.queryExecutor(query)
    contents = []
    for i in data:
        item = HerosElements(i[0],i[1],i[2])
        contents.append(item)
    res = getAllHerosResponse(contents)
    currentUserLogin = AuthenticationUtils(request).validateAndGetCurrentUserLogin()
    currentUserId = uv.findOneUserIdByLogin(currentUserLogin)
    currentUserRole = uv.findRoleByUserId(currentUserId)
    print(currentUserId,currentUserLogin,currentUserRole)
    return JsonResponse(json.loads(res.toJSON()))


