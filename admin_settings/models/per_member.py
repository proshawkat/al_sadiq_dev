from django.db import models
from rest_framework import serializers

class PerMember(models.Model):
    id = models.BigAutoField(primary_key=True)
    monthly_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    booster_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)

    def __str__(self):
        return str(self.monthly_amount)

class PerMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerMember
        fields = '__all__'