from django.db import models
from rest_framework import serializers

class Month(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Month
        fields = '__all__'