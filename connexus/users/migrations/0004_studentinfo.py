# Generated by Django 2.1.2 on 2018-10-02 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20181002_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_number', models.PositiveIntegerField(null=True)),
                ('house', models.CharField(choices=[('C', 'Challengers'), ('P', 'Pioneers'), ('E', 'Explorers'), ('V', 'Voyagers')], default='C', max_length=1)),
            ],
        ),
    ]
