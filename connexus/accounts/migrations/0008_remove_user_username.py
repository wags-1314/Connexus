# Generated by Django 2.1.2 on 2018-10-02 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_user_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
