from rest_framework import serializers
import json
from .models import Hero



class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias','age')


# ----------------------- custom serializers -----------------

class HerosElements:
    def __init__(self, id,name, age):
        self.name = name
        self.id = id
        self.age = age

class getAllHerosResponse:
    def __init__(self, content):
        self.content = content

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)