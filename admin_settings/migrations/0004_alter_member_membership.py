# Generated by Django 4.0.2 on 2024-07-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_settings', '0003_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='membership',
            field=models.IntegerField(),
        ),
    ]
