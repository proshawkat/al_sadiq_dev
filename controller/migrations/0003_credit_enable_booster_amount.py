# Generated by Django 4.0.2 on 2024-07-13 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0002_credit_created_at_credit_paid_at_credit_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='enable_booster_amount',
            field=models.BooleanField(default=False),
        ),
    ]
