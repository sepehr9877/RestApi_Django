# Generated by Django 4.1.1 on 2022-11-21 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_alter_accountuser_useraccount'),
        ('Content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='user_content',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Account.accountuser'),
        ),
    ]
