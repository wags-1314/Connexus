# Generated by Django 2.1.2 on 2018-10-02 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181002_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentuser',
            name='info',
        ),
        migrations.DeleteModel(
            name='StudentInfo',
        ),
    ]