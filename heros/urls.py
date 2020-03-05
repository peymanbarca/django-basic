# myapi/urls.py
from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/v1.0/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('api/v1.0/heros/getAll', views.getAllHerosV1_0.as_view(), name='getAllHerosV1.0'),
    url('api/v1.1/heros/getAll', views.getAllHerosV1_1, name='getAllHerosV1.1'),
]