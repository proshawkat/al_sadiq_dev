# Generated by Django 4.0.2 on 2024-07-12 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_settings', '0004_alter_member_membership'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('must_pay', models.CharField(editable=False, max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('booster_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_settings.member')),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_settings.month')),
            ],
        ),
    ]
