# Generated by Django 4.1.1 on 2022-11-19 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='useraccount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserDetailSpec', to=settings.AUTH_USER_MODEL),
        ),
    ]