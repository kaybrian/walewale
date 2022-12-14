# Generated by Django 3.2.15 on 2022-08-06 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='balance')),
                ('account_name', models.CharField(max_length=250, verbose_name='account name')),
                ('account_number', models.CharField(max_length=100, verbose_name='account number')),
                ('bank', models.CharField(max_length=100, verbose_name='bank')),
                ('phone_number', models.CharField(max_length=15, verbose_name='phone number')),
                ('password', models.CharField(max_length=200, verbose_name='password')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
