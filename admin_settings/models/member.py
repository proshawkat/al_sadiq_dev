from django.db import models
from rest_framework import serializers

class Member(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50,  blank=True)
    membership = models.IntegerField()

    def __str__(self):
        return str(self.name)

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'