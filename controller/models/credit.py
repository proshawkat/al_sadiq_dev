from django.db import models
from rest_framework import serializers
from admin_settings.models.month import Month
from admin_settings.models.member import Member
from admin_settings.models.per_member import PerMember

class Credit(models.Model):
    id = models.BigAutoField(primary_key=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    must_pay = models.CharField(max_length=50,editable=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    enable_booster_amount = models.BooleanField(default=False)
    booster_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)
    paid_at = models.DateTimeField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.member)

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                per_member = PerMember.objects.get(id=self.member.id)
                total = per_member.monthly_amount * self.member.membership
            except PerMember.DoesNotExist:
                total = 0
            self.must_pay = total
        super().save(*args, **kwargs)

class CreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        fields = '__all__'