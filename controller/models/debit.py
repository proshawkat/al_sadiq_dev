from django.db import models
from rest_framework import serializers
from admin_settings.models.month import Month
from admin_settings.models.member import Member
from admin_settings.models.per_member import PerMember

class Debit(models.Model):
    id = models.BigAutoField(primary_key=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    source =  models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.source)

class DebitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debit
        fields = '__all__'