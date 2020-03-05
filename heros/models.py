from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'heros'

    def __str__(self):
        return self.name
